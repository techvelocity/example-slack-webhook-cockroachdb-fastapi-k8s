import json
import os
import requests
from fastapi import FastAPI, Form, Request, Depends
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
SLACK_WEBHOOK_URL = os.environ.get('SLACK_WEBHOOK_URL')
DATABASE_URI = f'postgresql://jeff:{POSTGRES_PASSWORD}@apex-whale-2860.g95.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full'
engine = create_engine(DATABASE_URI)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    device_type = Column(String)

# Create the table in the database
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/api/sign-up")
def create_user(request: Request):
    device_type = request.headers._list[9][1].decode('utf-8')
    payload = json.dumps({'sign_up_from': device_type})
    requests.post(SLACK_WEBHOOK_URL,data=payload)
    with SessionLocal() as session:
        user = User(device_type=device_type)
        session.add(user)
        session.commit()
        return user

@app.get("/api/users")
def get_users():
    with SessionLocal() as session:
        r = session.query(User).all()
        return r


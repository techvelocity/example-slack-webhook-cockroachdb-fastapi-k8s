# slack-webhook-cockroachdb-fastapi-k8s

1. Create Webhook in Slack
2. Sign up for CockroachDB / Create a DB
   - Update contents of `root.crt` with your downloaded values
3. Run the commands below to start the application in Kubernetes

```
kubectl create secret generic cockroachdb-credentials --from-literal=password=<password>
kubectl create secret generic slack-webhook-url --from-literal=url=<url>
helm template . -f values.yaml | kubectl apply -f -
```


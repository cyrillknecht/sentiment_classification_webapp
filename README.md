# Sentiment Classification Web App

A web app that classifies the sentiment of a given text.
Access the app at http://http://34.118.124.220/.
Hosted on Google Cloud Platform.
Using docker and kubernetes.
Docker image hosted on Docker Hub.

## Run the app locally with docker

```bash
    docker build -t sentiment-classification-web-app .
    docker run -p 4040:4040 sentiment-classification-web-app
```

## Run the app locally with kubernetes

### Run the app
Run the following commands to deploy the app to a local kubernetes cluster.
```bash
    kubectl apply -f deployment.yaml
    kubectl apply -f service.yaml
```
Wait for approximately 5 minutes for the service to be ready.
You can check the status of the service with the following command.
```bash
    kubectl get pods -l app=sentiment-webapp
```
```bash
  kubectl describe pod <pod-name>
```
Once the service is ready, run the following command to forward the service to localhost.
```bash
    kubectl port-forward service/sentiment-webapp-service 8080:80
```

Access the app at http://localhost:8080.

### Delete the app
Run the following commands to delete the app from the local kubernetes cluster.
```bash
    kubectl delete -f deployment.yaml
    kubectl delete -f service.yaml
```

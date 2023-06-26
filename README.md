# Sentiment Classification Web App

## Run the app locally with docker

```bash
    docker build -t sentiment-classification-web-app .
    docker run -p 4040:4040 sentiment-classification-web-app
```

## Run the app locally with kubernetes (does not work yet)

```bash
    kubectl apply -f deployment.yaml
    kubectl apply -f service.yaml
    kubectl port-forward service/sentiment-webapp-service 8080:80
```

Access the app at http://localhost:8080.

![App UI](/static/assets/webapp_ui.png)


[![Build Docker Image and Push to Docker Hub](https://github.com/cyrillknecht/sentiment_classification_webapp/actions/workflows/docker-build-push.yaml/badge.svg)](https://github.com/cyrillknecht/sentiment_classification_webapp/actions/workflows/docker-build-push.yaml)
[![Google Kubernetes Engine Deployment](https://github.com/cyrillknecht/sentiment_classification_webapp/actions/workflows/gke-deploy.yaml/badge.svg)](https://github.com/cyrillknecht/sentiment_classification_webapp/actions/workflows/gke-deploy.yaml)

**A simple web app that classifies the sentiment of a given text snippet as positive or negative.
Access the running app by clicking the icon below.
(Can be offline due to cluster maintenance)**


[<img src="static/assets/favicon.ico" alt="Icon" width="60" height="60">](http://34.118.61.212/)



## The App
The Sentiment Classification Webapp is a simple Flask Webapp using a pre-trained
Sentiment Classification Model to classify the sentiment of a given text snippet as positive or negative.


The goal of this project was not to create a state-of-the-art sentiment classification model,
but rather to create a simple web app using **Docker** and **Kubernetes** to get familiar with these technologies.
The app was then hosted on **Google Cloud** using **Google Kubernetes Engine** which also allowed me to get familiar
with these cloud technologies.

Furthermore, I implemented a simple CI/CD pipeline using **GitHub Actions** to automatically build and deploy the app.
The pipeline is triggered whenever a new commit is pushed to the master branch of this repository and builds a new 
docker image that is then pushed to **Docker Hub**. The image is then afterwards automatically pulled from Docker Hub and deployed to the
Google Kubernetes Engine cluster. There it replaces the old deployment and the new version of the app is available. 

I am of course completely aware that this is probably not the most efficient way to
deploy such a simple web app. However, I wanted to get familiar with these technologies and this was a fun way to do so.


## Development
Instructions for running the app locally.

### Run the app locally with docker

```bash
    docker build -t sentiment-classification-web-app .
    docker run -p 4040:4040 sentiment-classification-web-app
```

### Run the app locally with kubernetes

#### Run the app
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

#### Delete the app
Run the following commands to delete the app from the local kubernetes cluster.
```bash
    kubectl delete -f deployment.yaml
    kubectl delete -f service.yaml
```

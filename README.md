# Behavioral Management



## Link to Product Backlog
https://trello.com/b/a7TfCO5r/backlog

## Link to Figma Design
https://www.figma.com/file/2l9kirQYo5fYv5o7du1QE1/Prism?type=design&node-id=0%3A1&t=jeWrcx99quajtOFZ-1

## Trello Backlog Link
https://trello.com/invite/nksem1/ATTI3b69ea4d08aff1cc37d25482d145566d547C253D

# Frontend

## Project setup

```
yarn install
```

### Compiles and hot-reloads for development

```
yarn dev
```
The program should be open on port 3000

### Compiles and minifies for production

```
yarn build
```

### Lints and fixes files

```
yarn lint
```

### Customize configuration

See [Configuration Reference](https://cli.vuejs.org/config/).


# Backend

## Go to the correct directory
`cd backend`

## Run the backend
`python manage.py runserver`

The program should run on port 8000

## backend/mosaic/
Keeps the setting files for configurations here
`urls.py` controls the routing once the request hits the backend server.

## backend/questionnaire/
Keeps the database and views for questionnaire and its details.



# Docker
You can run the docker using `sudo docker-compose up -d build`. You will need to have docker installed.
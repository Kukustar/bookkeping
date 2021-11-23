# Bookkeeping


# First setup
- backend

```docker-compose build```

```docker-compose run --rm app python manage.py migrate```

```docker-compose run --rm app python manage.py createsuperuser```

```docker-compose run --rm app python manage.py shell < init.py``` - add balance and purchase type

```docker-compose up -d``` - run docker

- frontend

```cd ui```

```npm i```

```npm run serve```


# run migrations after add model

```docker-compose run --rm app python manage.py makemigrations```

```docker-compose run --rm app python manage.py migrate```

# About docker

```docker-compose down``` fall down the docker

```docker volume ls``` Contains

```docker volume rm "volume_name"``` Deleting a container

```docker ps``` List of enabled dockers
```docker exec -it <  id of container  > sh```Enter the container

# Bookkeeping


# First setup
- backend

```docker-compose build```

```docker-compose run --rm app python manage.py migrate```

```docker-compose run --rm app python manage.py createsuperuser```

```docker-compose up -d```

- frontend

```cd ui```

```npm i```

```npm run serve```


# run migrations after add model

```docker-compose run --rm app python manage.py makemigrations```
```docker-compose run --rm app python manage.py migrate```
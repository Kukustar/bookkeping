# bookkeeping


# first setup
`docker-compose build`
`docker-compose run --rm app python manage.py migrate`
`docker-compose run --rm app python manage.py createsuperuser`
`docker-compose up -d`

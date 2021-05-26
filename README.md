# bookkeeping


# first setup
`docker-compose build`
`docker-compose run --rm app python app/manage.py migrate`
`docker-compose run --rm app python app/manage.py createsuperuser`
`docker-compose up -d`

run:
	@python manage.py runserver

migrate:
	@python manage.py makemigrations
	@python manage.py migrate

test:
	@python manage.py test


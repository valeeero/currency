SHELL := /bin/bash

manage_py := python ./app/manage.py

runserver:
	$(manage_py) runserver 0:8000

makemigrations:
	$(manage_py) makemigrations

migrate:
	$(manage_py) migrate

shell:
	$(manage_py) shell_plus --print-sql

worker:
	cd app && celery -A settings worker -l info --autoscale=10,2

createsuperuser:
	$(manage_py) createsuperuser

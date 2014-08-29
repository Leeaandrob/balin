clean:
	find . -name "*.pyc" -delete

requirements: clean
	pip install -r requirements.txt

setup: requirements
	python manage.py syncdb --migrate

migrate:
	python manage.py migrate

run:
	python manage.py runserver

.PHONY: clean requirements setup migrate run

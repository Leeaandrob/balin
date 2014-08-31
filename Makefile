clean:
	find . -name "*.pyc" -delete

requirements: clean
	pip install -r requirements.txt

setup: requirements
	python manage.py syncdb --migrate

makemessages:
	sh scripts/makemessages.sh

compilemessages:
	sh scripts/compilemessages.sh

migrate:
	python manage.py migrate

run:
	python manage.py runserver

.PHONY: clean requirements setup makemessages compilemessages migrate run

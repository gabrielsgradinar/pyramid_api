run-serve:
	gunicorn --paste development.ini

run-celery:
	celery -A pyramid_api.tasks worker --ini development.ini

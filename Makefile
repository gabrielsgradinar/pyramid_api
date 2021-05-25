run-serve:
	pserve development.ini --reload

run-celery:
	celery -A pyramid_api.tasks worker --ini development.ini

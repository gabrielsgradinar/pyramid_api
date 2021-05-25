from pyramid_celery import celery_app as app

@app.task()
def reverse(self, text):
    return text[::-1]
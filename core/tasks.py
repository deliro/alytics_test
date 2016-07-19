import json

from project import celery_app


@celery_app.task(bind=True, queue='get')
def get(self, instance):
    process.delay(instance)
    return instance


@celery_app.task(bind=True, queue='process')
def process(self, instance):
    try:
        d = json.loads(instance.input)
        result = {'result': sum(chunk['a'] + chunk['b'] for chunk in d)}
        instance.result = result
        return result
    except Exception as e:
        instance.exception = str(e)
    finally:
        save.delay(instance)


@celery_app.task(bind=True, queue='save')
def save(self, instance):
    instance.save()

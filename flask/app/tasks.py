from app import celery
from time import sleep

@celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 5 seconds.
    sender.add_periodic_task(5.0, test.s('HELLO FLASK_CELERY IS WORKING'), name='test every 5')


@celery.task()
def test(arg):
    print(arg)

@celery.task()
def make_file(fname, content):
    with open(fname, "w") as f:
        f.write(content)
    return fname, content


@celery.task()
def complex_task(text):
    sleep(15)
    return text
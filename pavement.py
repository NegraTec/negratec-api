from paver.easy import task
from paver.shell import sh
from paver.tasks import needs


@task
@needs('migration')
def test():
    sh('python ./manage.py test')


@task
@needs('migration')
def server():
    sh('python ./manage.py runserver')


@task
def migration():
    sh('python ./manage.py makemigrations; python ./manage.py migrate')

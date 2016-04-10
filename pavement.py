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
    sh('python ./manage.py migrate')

@task
@needs('test')
def ci():
    sh('flake8 negratec')

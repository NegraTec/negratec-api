from paver.easy import task
from paver.shell import sh


@task
def test():

    sh('python ./manage.py test')

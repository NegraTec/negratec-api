from factory.django import DjangoModelFactory
from django.contrib.auth.models import User


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = 'fulana'
    password = 'senha'
    email = 'fulana@email.com'

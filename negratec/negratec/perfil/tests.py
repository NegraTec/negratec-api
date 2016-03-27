from django.test import TestCase
from negratec.perfil.factories import PerfilFactoryResource


class Perfil(TestCase):

    def test_criar_um_perfil(self):
        expected_perfil = PerfilFactoryResource()

        print(expected_perfil)
        response = self.client.post('/v1/perfil', expected_perfil)

        print(response)

        self.assertEqual(201, response.status_code)


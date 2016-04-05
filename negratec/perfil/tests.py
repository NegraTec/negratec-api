from django.test import TestCase
from negratec.perfil.factories import PerfilFactoryResource


class PerfilTest(TestCase):

    def test_criar_um_perfil(self):
        expected_perfil = PerfilFactoryResource()

        response = self.client.post('/v1/perfil', expected_perfil)

        self.assertEqual(201, response.status_code, response.data)


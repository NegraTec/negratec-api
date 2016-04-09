from negratec.perfil.tests import helper_photo
from rest_framework.test import APITestCase
from negratec.perfil.factories import PerfilFactoryResource


class PerfilTest(APITestCase):

    def test_criar_um_perfil(self):
        expected_perfil = PerfilFactoryResource()

        expected_perfil['imagem'] = helper_photo.photo_base64()
        response = self.client.post('/v1/perfil', expected_perfil)

        self.assertEqual(201, response.status_code, response.data)


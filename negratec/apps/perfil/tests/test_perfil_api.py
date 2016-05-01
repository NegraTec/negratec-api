from negratec.apps.perfil.tests import helper_photo
from rest_framework.test import APITestCase
from negratec.apps.perfil.tests.factories import PerfilFactoryResource
from negratec.apps.usuaria.factories import UserFactory


class PerfilTest(APITestCase):

    def test_criar_um_perfil(self):
        usuaria = UserFactory()
        expected_perfil = PerfilFactoryResource(usuaria=usuaria.pk)

        expected_perfil['imagem'] = helper_photo.photo_base64()
        response = self.client.post('/v1/perfil', expected_perfil)

        self.assertEqual(201, response.status_code, response.data)

    def test_somente_criar_um_perfil_com_uma_usuaria_cadastrada(self):
        expected_perfil = PerfilFactoryResource()
        expected_perfil['imagem'] = helper_photo.photo_base64()
        del expected_perfil['usuaria']

        response = self.client.post('/v1/perfil', expected_perfil)

        self.assertEqual(400, response.status_code, response.data)
        self.assertDictEqual({'usuaria': ['This field is required.']}, response.data)

    def test_campos_de_redes_sociais_e_outras_infos_nao_devem_ser_obrigatorios(self):
        usuaria = UserFactory()
        expected_perfil = PerfilFactoryResource(
          usuaria=usuaria.pk,
          twitter='',
          github='',
          linkedin='',
          outras_redes='',
          lutas='',
          stacks='',
          eventos=''
        )
        expected_perfil['imagem'] = helper_photo.photo_base64()

        response = self.client.post('/v1/perfil', expected_perfil)

        self.assertEqual(201, response.status_code, response.data)

        del expected_perfil['imagem']
        del response.data['imagem']
        del response.data['id']
        self.assertDictEqual(expected_perfil, response.data)

    def test_campo_para_descricao_nao_deve_ser_obrigatorio(self):
        usuaria = UserFactory()
        expected_perfil = PerfilFactoryResource(
          usuaria=usuaria.pk,
          descricao='sobre mim.'
        )

        expected_perfil['imagem'] = helper_photo.photo_base64()
        response = self.client.post('/v1/perfil', expected_perfil)

        self.assertEqual(201, response.status_code, response.data)
        self.assertEqual(expected_perfil['descricao'], response.data['descricao'])

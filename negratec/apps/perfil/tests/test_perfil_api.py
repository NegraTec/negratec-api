from negratec.apps.perfil.tests import helper_photo
from rest_framework.test import APITestCase
from negratec.apps.perfil.tests.factories import PerfilFactoryResource, PerfilFactory
from negratec.apps.usuaria.factories import UserFactory
from django.core.files.base import ContentFile
import base64
from negratec.apps.perfil.models import Perfil


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

    def test_permiti_deletar_um_perfil(self):
        usuaria = UserFactory()
        img = self.trata_imagem(helper_photo.photo_base64())
        expected_perfil = PerfilFactory(
          usuaria=usuaria,
          descricao='sobre mim.',
          imagem=img
        )

        response = self.client.delete('/v1/perfil/{}/'.format(expected_perfil.pk))

        self.assertEqual(204, response.status_code)

        perfil_no_db = Perfil.objects.filter(pk=expected_perfil.pk)
        self.assertEqual(0, perfil_no_db.count())

    def trata_imagem(self, data):
        format, imgstr = data.split(';base64,')  # format ~= data:image/X,
        ext = format.split('/')[-1]  # guess file extension
        data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
        return data

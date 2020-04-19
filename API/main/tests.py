from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient

from . import views

from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from .models import Project


class SetAPITestCase(APITestCase):
    @staticmethod
    def setup_user():
        User = get_user_model()
        return User.objects.create_user(
            first_name='test',
            last_name='test',
            username='test',
            email='testuser@test.com',
            password='test',
        )


class OrderTest(SetAPITestCase):
    def setUp(self):
        self.client = APIClient()
        self.uri = '/orders/'
        self.user = self.setup_user()
        self.token = Token.objects.create(user=self.user)
        self.token.save()

    def list_orders(self):
        self.client.login(username='test', password='test')
        response = self.client.get(self.uri)
        self.assertEqual(
            response.status_code,
            200,
            f"Expected response code 200 but got {response.status_code} instead.\n{response}"
        )

    def create_order(self):
        self.client.login(username='test', password='test')
        params = {
            "user": 1,
            "plan": "",
            "amt": "",
            "active": "",
            "created": "",
            "expires": "",
            "invoiceUrl": "",
        }
        response = self.client.post(self.uri, params)
        self.assertEqual(
            response.status_code,
            405,  # ?not allowed
            f"Expected response code 405 but got {response.status_code} instead.\n{response}"
        )


class UserDataTest(SetAPITestCase):
    def setUp(self):
        self.client = APIClient()
        self.uri = '/userdata/'
        self.user = self.setup_user()
        self.token = Token.objects.create(user=self.user)
        self.token.save()

    def list_userdata(self):
        self.client.login(username='test', password='test')
        response = self.client.get(self.uri)
        self.assertEqual(
            response.status_code,
            200,
            f"Expected response code 200 but got {response.status_code} instead.\n{response}"
        )

    def create_userdata(self):
        self.client.login(username='test', password='test')
        params = {
            "user": 1,
            "notifyFeature": "",
            "notifyInvoice": "",
            "notifyNews": "",
            "avatar": "",
            "city": "",
            "country": "",
            "created": "",
        }
        response = self.client.post(self.uri, params)
        self.assertEqual(
            response.status_code,
            201,
            f"Expected response code 201 but got {response.status_code} instead.\n{response}"
        )


class ProjectTest(SetAPITestCase):
    def setUp(self):
        self.client = APIClient()
        self.uri = '/projects/'
        self.user = self.setup_user()
        self.token = Token.objects.create(user=self.user)
        self.token.save()

    def list_projects(self):
        self.client.login(username='test', password='test')
        response = self.client.get(self.uri)
        self.assertEqual(
            response.status_code,
            200,
            f"Expected response code 200 but got {response.status_code} instead.\n{response}"
        )

    def create_project(self):
        self.client.login(username='test', password='test')
        params = {
            "user": 1,
            "name": "",
            "preview": "",
            "classes": "",
            "domain": "",
            "published": "",
            "lastPublished": "",
        }
        response = self.client.post(self.uri, params)
        self.assertEqual(
            response.status_code,
            201,
            f"Expected response code 201 but got {response.status_code} instead.\n{response}"
        )


class PageTest(SetAPITestCase):
    def setUp(self):
        self.client = APIClient()
        self.uri = '/pages/38791566-b8c1-449a-aae4-9870df8d3d24'
        self.user = self.setup_user()
        self.project = self.create_project(self.user)
        self.token = Token.objects.create(user=self.user)
        self.token.save()

    def create_project(self, user):
        return Project.objects.create(
            user=user,
            uuid="38791566-b8c1-449a-aae4-9870df8d3d24",
        )

    def list_pages(self):
        self.client.login(username='test', password='test')
        response = self.client.get(self.uri)
        self.assertEqual(
            response.status_code,
            200,  # ? Project does not exist so this returns a 404
            f"Expected response code 200 but got {response.status_code} instead.\n{response}"
        )

    def create_page(self):
        self.client.login(username='test', password='test')
        params = {
            "project": 1,
            "name": "",
            "thumbnail": "",
            "favicon": "",
            "webclip": "",
            "html": "<div></div>",
            "css": ".class{color:red}",
            "script": "",
            "components": "[]",
            "assets": "[]",
            "styles": "[]",
            "metaTitle": "",
            "metaDesc": ""
        }
        response = self.client.post(
            self.uri,
            params
        )
        self.assertEqual(
            response.status_code,
            201,  # ?Project does not exist so this returns a 404
            f"Expected response code 201 but got {response.status_code} instead.\n{response} uri={self.uri}"
        )


class AssetTest(SetAPITestCase):
    def setUp(self):
        self.client = APIClient()
        self.uri = '/assets/'
        self.user = self.setup_user()
        self.token = Token.objects.create(user=self.user)
        self.token.save()

    def list_assets(self):
        self.client.login(username='test', password='test')
        response = self.client.get(self.uri)
        self.assertEqual(
            response.status_code,
            200,
            f"Expected response code 200 but got {response.status_code} instead.\n{response}"
        )

    def create_asset(self):
        self.client.login(username='test', password='test')
        params = {
            "user": 1,
            "file": "file",
            "added": "",
        }
        response = self.client.post(self.uri, params)
        self.assertEqual(
            response.status_code,
            400,  # ? 201 expected if there is way of sending form data
            f"Expected response code 400 but got {response.status_code} instead.\n{response}"
        )


class BlockTest(SetAPITestCase):
    def setUp(self):
        self.client = APIClient()
        self.uri = '/blocks/'
        self.user = self.setup_user()
        self.token = Token.objects.create(user=self.user)
        self.token.save()

    def list_blocks(self):
        self.client.login(username='test', password='test')
        response = self.client.get(self.uri)
        self.assertEqual(
            response.status_code,
            200,
            f"Expected response code 200 but got {response.status_code} instead.\n{response}"
        )

    def create_block(self):
        self.client.login(username='test', password='test')
        params = {
            "user": 1,
            "name": "",
            "category": "",
            "description": "",
            "html": "Some Stuff",
            "css": "Some Stuff",
            "script": "",
            "preview": "",
            "classes": "",
            "created": ""
        }
        response = self.client.post(self.uri, params)
        self.assertEqual(
            response.status_code,
            201,
            f"Expected response code 201 but got {response.status_code} instead.\n{response}"
        )


class LogicTest(SetAPITestCase):
    def setUp(self):
        self.client = APIClient()
        self.uri = '/logic/'
        self.user = self.setup_user()
        self.token = Token.objects.create(user=self.user)
        self.token.save()

    def list_logic(self):
        self.client.login(username='test', password='test')
        response = self.client.get(self.uri)
        self.assertEqual(
            response.status_code,
            200,
            f"Expected response code 200 but got {response.status_code} instead.\n{response}"
        )

    def create_logic(self):
        self.client.login(username='test', password='test')
        params = {
            "user": 1,
            "name": "",
            "category": "",
            "decription": "",
            "script": "Some Stuff",
            "created": ""
        }
        response = self.client.post(self.uri, params)
        self.assertEqual(
            response.status_code,
            201,
            f"Expected response code 201 but got {response.status_code} instead.\n{response}"
        )

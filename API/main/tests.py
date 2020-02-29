from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient

from . import views

from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

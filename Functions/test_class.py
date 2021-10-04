from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from messagging.factorie import MessageFactory
from users.models import User
from users.tests.factories import UserFactory


class TestClass(APITestCase):
    def setUp(self):
        for i in range(2, 6):
            setattr(self, f'user{i}', UserFactory())

        self.user = User.objects.create_superuser(email='x@g.com', username='ali', password='password')
        self.user.confirmed = True
        self.user.save()

        client = APIClient()
        res = client.post('/api/v1/login/', {'username': self.user.username, 'password': 'password'})
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        token = res.data['token']
        client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
        self.client = client

        for i in range(6):
            m = MessageFactory()
            # m.channel = self.user.channel_set.first()
            # m.save()

    def test_one(self):
        assert self.user
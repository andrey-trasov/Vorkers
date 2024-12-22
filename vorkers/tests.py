from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from vorkers.models import Vorkers


class VorkersTestCase(APITestCase):

    def setUp(self):
        """
        создаем бд
        """
        self.vorkers = Vorkers.objects.create(
            full_name="Иванов",
            team_number="1",
            salary="10000",
            specialization="Черновая отделка",
        )

    def test_VorkersRetrieveAPIView(self):
        """
        Проверяем получение мастера
        """
        url = reverse("api:vorker", args=(self.vorkers.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["full_name"], self.vorkers.full_name)
        self.assertEqual(response.data["specialization"], self.vorkers.specialization)

    def test_TeamVorkersListAPIView(self):
        """
        Проверяем получение списка работников в бригаде
        """
        url = reverse("api:team_vorkers", args=(self.vorkers.team_number,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

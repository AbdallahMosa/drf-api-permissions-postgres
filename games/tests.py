from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import  status
# Create your tests here.
from django.contrib.auth import get_user_model
from .models import Game,Movie

from django.urls import reverse

class ThingTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()

        testuser2 = get_user_model().objects.create_user(
            username="testuser2", password="pass"
        )
        testuser2.save()

        test_thing = Game.objects.create(
            title="test1",
            purchaser=testuser1,
            description="description for testing",
            img_url='no image'
        )
        test_thing.save()


    def setUp(self):
        self.client.login(username='testuser1', password="pass")




    def test_games_model(self):
        game = Game.objects.get(id=1)
        actual_owner = str(game.purchaser)
        actual_name = str(game.title)
        actual_description = str(game.description)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_name, "test1")
        self.assertEqual(
            actual_description, "description for testing"
        )

    def test_get_game_list(self):
        url = reverse("game_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        things = response.data
        self.assertEqual(len(things), 1)
        

    def test_auth_required(self):
        self.client.logout()
        url = reverse("game_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_only_owner_can_delete(self):
        self.client.logout()
        self.client.login(username='testuser2', password="pass")
        url = reverse("game_detail", args=[1])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
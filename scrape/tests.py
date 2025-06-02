from django.test import TestCase
from django.urls import reverse


class ScorepageTests(TestCase): 

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/score/")
        self.assertEqual(response.status_code, 200)

    
    def test_url_available_by_name(self):
        response = self.client.get(reverse("score"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  # new
        response = self.client.get(reverse("scrape"))
        self.assertTemplateUsed(response, "score.html")






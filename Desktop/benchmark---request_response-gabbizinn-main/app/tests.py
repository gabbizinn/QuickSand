from django.test import SimpleTestCase
from http.server import SimpleHTTPRequestHandler
from urllib import response

# Create your tests here.

#Last2
class TestLast2(SimpleTestCase):
    def test_last_2_0(self):
        response = self.client.get("/warmup-2/last_2/0")
        self.assertContains(response, "0")

    def test_last_2_1(self):
        response = self.client.get("/warmup-2/last_2/1")
        self.assertContains(response, "0")

    def test_last_2_2(self):
        response = self.client.get("/warmup-2/last_2/2")
        self.assertContains(response, "0")

#Other End
class TestOtherEnd(SimpleTestCase):
    def test_end_other_abc(self):
        response = self.client.get("/string-2/end_other/abc")
        self.assertContains(response, True)

    def test_end_other_ab(self):
        response = self.client.get("/string-2/end_other/ab")
        self.assertContains(response, True)

    def test_end_other_ba(self):
        response = self.client.get("/string-2/end_other/ba")
        self.assertContains(response, True)

#Lone Sum
class TestLoneSum(SimpleTestCase):
    def test_lone_sum_123(self):
        response = self.client.get("/logic-2/lone_sum/1/2/3")
        self.assertContains(response, "6")

    def test_lone_sum_323(self):
        response = self.client.get("/logic-2/lone_sum/3/2/3")
        self.assertContains(response, "2")

    def test_lone_sum_333(self):
        response = self.client.get("/logic-2/lone_sum/3/3/3")
        self.assertContains(response, "0")
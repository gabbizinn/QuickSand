from django.test import SimpleTestCase
from http.server import SimpleHTTPRequestHandler
from urllib import response

# Create your tests here.

#Last2
class TestLast2(SimpleTestCase):
    def test_last_2_hixxhi(self):
        response = self.client.get("/warmup-2/last_2/hixxhi")
        self.assertContains(response, "1")

    def test_last_2_xaxxaxaxx(self):
        response = self.client.get("/warmup-2/last_2/xaxxaxaxx")
        self.assertContains(response, "1")

    def test_last_2_axxxaaxx(self):
        response = self.client.get("/warmup-2/last_2/axxxaaxx")
        self.assertContains(response, "2")

#Other End
class TestOtherEnd(SimpleTestCase):
    def test_end_other_abc(self):
        response = self.client.get("/string-2/end_other/abc/Hiabc")
        self.assertContains(response, True)

    def test_end_other_AbC(self):
        response = self.client.get("/string-2/end_other/AbC/HiaBc")
        self.assertContains(response, True)

    def test_end_other_abXabc(self):
        response = self.client.get("/string-2/end_other/abXabc/abc")
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
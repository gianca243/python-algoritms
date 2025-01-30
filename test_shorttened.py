import unittest
from shorttened import short_url, return_previous_url
class TestShorttened(unittest.TestCase):
    t_url = "www.google.com"
    expected_prefix_result = "www.mydomain.com/"
    def test_success_short_url(self):
        response = short_url(self.t_url)
        self.assertIn(self.expected_prefix_result, response.get("url", None))
        self.assertIn(200, response.get("status", None))

    def test_success_return_previous_url(self):
        url = return_previous_url(f"{self.expected_prefix_result}12331424")
        self.assertEqual(url, "www.google.com")

    def test_success(self):
        url = short_url(self.t_url)
        self.assertIn(self.expected_prefix_result, url)
        first_url = return_previous_url(url)
        self.assertEqual(self.t_url, first_url)
    

    def test_non_existing_url(self):
        url = return_previous_url(f"{self.expected_prefix_result}1233omg24")
        self.assertEqual(url, "www.google.com")


    
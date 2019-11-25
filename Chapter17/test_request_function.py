import unittest
from requests_function import github_api

class TestGithubAPI(unittest.TestCase):
    """test the github api"""

    def setUp(self):
        """set up the env to test github"""
        self.r = github_api()

    def test_github_api(self):
        """test the github api"""
        self.assertEqual(self.r.status_code, 200)

    def test_github_items_amount(self):
        """test the amount is more than 10"""
        self.assertGreater(self.r.json()['total_count'], 100)


if __name__ == '__main__':
    unittest.main()
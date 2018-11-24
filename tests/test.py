import unittest
from app import app


class AppTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client();

    def test_index(self):
        pass

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()

from unittest import TestCase

from app import app
from forex_python.converter import CurrencyRates, CurrencyCodes

# Make Flask errors be real errors, not HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


class CurrencyFormTestCase(TestCase):
    """Test Whose Currency Form."""

    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        """Make sure information is in the session and HTML is displayed"""

        with self.client as client:
            response = client.get('/')
            html = response.get_data(as_text=True)

            # test that you're getting a template
            self.assertIn('<div class="ms-3 me-3">',
                          html
                          )
            self.assertEqual(response.status_code, 200)

    # def test_api_new_game(self):
    #     """Test starting a new game."""

    #     with self.client as client:
    #         response = client.post('/api/new-game')
    #         data = response.get_json()

    #         # write a test for this route
    #         self.assertEqual(type(data["gameId"]), str)
    #         self.assertEqual(type(data["board"]), list)  # this is failing
    #         self.assertEqual(type(data["board"].pop()), list)
    #         self.assertNotEqual(data["board"], [])
    #         self.assertNotEqual(data["board"], [[]])

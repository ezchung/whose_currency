import app as app_module
from app import app
from unittest import TestCase
from forex_python.converter import CurrencyRates, CurrencyCodes

# Make Flask errors be real errors, not HTML pages with error info
app.config['TESTING'] = True

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
            resp = client.get('/')
            html = resp.get_data(as_text=True)
            print(resp.status_code)
            self.assertIn("Testing Currency Form", html)
            self.assertEqual(resp.status_code, 200)

            # response = client.get('/')
            # html = response.get_data(as_text=True)
            # print("____________im here html________________", html)

            # # test that you're getting a template
            # self.assertIn('<div class="ms-3 me-3">',
            #               html
            #               )
            # self.assertEqual(response.status_code, 200)

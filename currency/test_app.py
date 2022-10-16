import app as app_module
from app import app
from unittest import TestCase

from flask import session

from forex_python.converter import CurrencyRates, CurrencyCodes

# Make Flask errors be real errors, not HTML pages with error info
app.config['TESTING'] = True

app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

test_currency_code = "USD"


class CurrencyFormTestCase(TestCase):
    """Test Whose Currency Form."""

    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        """Test to see correct HTML is displayed """

        with self.client as client:
            resp = client.get('/')
            html = resp.get_data(as_text=True)

            self.assertIn("Testing Currency Form", html)
            self.assertEqual(resp.status_code, 200)

    # def test_results(self):
    #     """ Test to see if returning correct information"""

    #     answers = dict(
    #         curr_symbol="$",
    #         conversion=1
    #     )

    #     with self.client as client:
    #         resp = client.get('/results', curr_symbol="$",
    #                           conversion=1)
            #html = resp.get_data(as_text=True)
            #print(html, "___________html_______")

            # self.assertIn("Testing Results HTML", html)
            # self.assertEqual(resp.status_code, 200)

    def test_currency(self):
        """Test currency that returns true or none based on whether symbol exists"""
        assert is_currency_code("USD") == True

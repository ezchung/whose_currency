
from app import app, is_currency_code, is_num
from unittest import TestCase

from flask import session

from forex_python.converter import CurrencyRates, CurrencyCodes

app.config['TESTING'] = True

app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

test_currency_code = "USD"


class CurrencyFormTestCase(TestCase):
    """Test Whose Currency Form."""

    def test_homepage(self):
        """Test to see correct HTML is displayed """

        with app.test_client() as client:
            resp = client.get('/')
            html = resp.get_data(as_text=True)

            self.assertIn("Testing Currency Form", html)
            self.assertEqual(resp.status_code, 200)

    def test_results_page(self):
        """ 
            Test to see if results page is shown and data presented in results 
            page is expected data
        """

        answers = {
            "amount": 1,
            "currency_from": "USD",
            "currency_to": "USD"
        }

        with app.test_client() as client:
            response = client.get('/results',
                                  query_string=answers)
            body = response.get_data(as_text=True)

            self.assertIn("Testing Results HTML", body)
            self.assertEqual(response.status_code, 200)
            self.assertIn("The result is $ 1.00.", body)

    def test_is_currency_code(self):
        """ 
            Unit test to check if function is_currency_code returns 
            expected result
        """

        successResult = is_currency_code("USD")
        failResult = is_currency_code("GDP")
        self.assertEqual(successResult, True)
        self.assertEqual(failResult, None)

    def test_is_num(self):
        """ 
            Unit test to check if function is_num returns 
            expected result
        """

        successResult = is_num("10.5")
        failResult = is_num("one")
        self.assertEqual(successResult, True)
        self.assertEqual(failResult, False)

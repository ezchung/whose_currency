from flask import Flask, request, render_template, jsonify, flash

from flask_debugtoolbar import DebugToolbarExtension

from forex_python.converter import CurrencyRates, CurrencyCodes

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

currency_rates = CurrencyRates()
currency_codes = CurrencyCodes()


@app.get("/")
def homepage():
    """Show form"""
    # print("------------date obj----------", date_obj)
    print(currency_rates)
    print("---expected code to not exist-----",
          currency_codes.get_symbol('usd'))  # expected None, got none
    print("---check if code is real-----", currency_codes.get_symbol('USD'))
    return render_template("currency_form.html")


@app.get("/results")
def get_results():
    """Get results of form"""
    result = request.args
    amount = result["amount"]
    currency_from = result["currency_from"].upper()
    currency_to = result["currency_to"].upper()

    msg = {}
    if not is_currency_code(currency_from):
        flash(f"Not a valid code: {currency_from}")
        msg["currency_from"] = True
    if not is_currency_code(currency_to):
        flash(f"Not a valid code: {currency_to}")
        msg["currency_to"] = True
    if not is_num(amount):
        flash(f"Not a valid amount: {amount}")
        msg["amount"] = True

    if msg:
        return render_template("currency_form.html")

    conversion = currency_rates.convert(
        currency_from,
        currency_to,
        float(amount)
    )

    rounded_conversion = format(round(conversion, 2), '.2f')

    curr_symbol = currency_codes.get_symbol(currency_to)

    return render_template(
        "/results.html",
        curr_symbol=curr_symbol,
        conversion=rounded_conversion,
    )


"""
    Receive currency code and check if currency code exists in the dictionary
    Input: currency code. Output: true/false
"""


def is_currency_code(code):

    if currency_codes.get_symbol(code):
        return True
    return None


"""
    Pass in the amount as a string. If amount is not a number, returns false. 
    Otherwise, returns true.
    Input: amount       Output: boolean
"""


def is_num(amount):
    if not (amount.upper() == amount.lower()):
        return False

    converted_amount = float(amount)
    if (isinstance(converted_amount, float)):
        return True
    return False

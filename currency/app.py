from flask import Flask, request, render_template, jsonify, flash

#from stories import silly_story, excited_story
from flask_debugtoolbar import DebugToolbarExtension

from forex_python.converter import CurrencyRates, CurrencyCodes
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

currency_codes = CurrencyRates()
currency_check = CurrencyCodes()


@app.get("/")
def homepage():
    """Show form"""
    # print("------------date obj----------", date_obj)
    print(currency_codes)
    print("---expected code to not exist-----",
          currency_check.get_symbol('usd'))  # expected None, got none
    print("---check if code is real-----", currency_check.get_symbol('USD'))
    return render_template("currency_form.html")


@app.get("/results")
def get_results():
    """Get results of form"""
    result = request.args
    amount = result["amount"]
    currency_from = result["currency_from"]
    currency_to = result["currency_to"]
    print(is_currency_code(currency_to), "expect true or false-------")
    # if both currencies are true, return true
    #convert_rate = currency_codes.get_rate(currency_from, currency_to)
    #print(convert_rate, "convert-rate----------------------------")

    return render_template("/results.html")


"""
    Recieve currency code and check if currency code exists in the dictionary
    Input: currency code. Output: true/false
"""


def is_currency_code(code):
    # if this is truthy, return True
    if currency_check.get_symbol(code):
        return True
    return False

# story_types_dict = {
#     "silly_story": silly_story,
#     "excited_story": excited_story
# }

# @app.get('/<story_type>')
# def send_story_prompts(story_type):
#     """ get the story prompts form """
#     try:
#         s = story_types_dict[story_type]
#         prompts = s.prompts

#         if story_type in story_types_dict:
#             return render_template("questions.html", prompts=prompts,
#                                    story_type=story_type)
#     except:
#         return f"{story_type} route does not exist!"

# @app.get('/results')
# def handle_story_submit(story_type):
#     """ create the story from the template and prompts """
#     s = story_types_dict[story_type]

#     story = s.generate(request.args)

#     return render_template("results.html", story=story)

from flask import Flask, request, render_template, jsonify, flash

#from stories import silly_story, excited_story
from flask_debugtoolbar import DebugToolbarExtension

from forex_python.converter import CurrencyRates
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

currency_codes = CurrencyRates()


@app.get("/")
def homepage():
    """Show form"""
    # print("------------date obj----------", date_obj)
    # print(currency_codes.get_rates('USD'))
    print
    return render_template("currency_form.html")


@app.get("/results")
def get_results():
    """Get results of form"""
    result = request.args
    amount = result["amount"]
    currency_from = result["currency_from"]
    currency_to = result["currency_to"]
    convert_rate = currency_codes.get_rate(currency_from, currency_to)
    print(convert_rate, "convert-rate----------------------------")

    return render_template("/results.html")

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

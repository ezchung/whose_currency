
from flask import Flask, request, render_template, jsonify
from forex_python.converter import CurrencyRates

app = Flask(__name__)
app.config["SECRET_KEY"] = "this-is-secret"

from flask import Flask, render_template
from flask_zurb_foundation import Foundation
app = Flask(__name__)
Foundation(app)
from app import routes


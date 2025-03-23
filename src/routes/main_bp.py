from flask import Flask, Blueprint, render_template
import os


TEMPLATE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__),"..","templates"))

main_bp = Blueprint(
    'main_bp',
    __name__,
    template_folder=TEMPLATE_DIR
)

@main_bp.route('/')
def home():
    return render_template('index.html')
from flask import render_template
from . import gallery


@gallery.route('/')
def index():
    return render_template('gallery/index.html')

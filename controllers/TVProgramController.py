# -*- coding: utf-8 -*-
"""
Onyx Project
https://onyxlabs.fr
Software under licence Creative Commons 3.0 France
http://creativecommons.org/licenses/by-nc-sa/3.0/fr/
You may not use this software for commercial purposes.
"""

from tvprogram_skill.index import tvprogram
from flask_login import login_required
from flask import render_template

from tvprogram_skill.api import *


@tvprogram.route('/' , methods=['GET','POST'])
@login_required
def index():
    return render_template('tvprogram/index.html')

@tvprogram.route('/config' , methods=['GET','POST'])
@login_required
def config():
    return render_template('tvprogram/config.html')

@tvprogram.route('/widget')
@login_required
def widget():
    return render_template('tvprogram/widget.html')

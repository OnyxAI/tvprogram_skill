# -*- coding: utf-8 -*-
"""
Onyx Project
https://onyxlabs.fr
Software under licence Creative Commons 3.0 France
http://creativecommons.org/licenses/by-nc-sa/3.0/fr/
You may not use this software for commercial purposes.
"""

import os
import glob

__all__ = [os.path.basename(f)[:-3] for f in glob.glob(os.path.dirname(__file__) + "/*.py")]


from flask import Blueprint

tvprogram = Blueprint('tvprogram', __name__, url_prefix='/tvprogram', template_folder='templates')

from tvprogram_skill.controllers import *

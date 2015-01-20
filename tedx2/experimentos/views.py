# -*- coding: utf-8 -*-
'''Public section, including homepage and signup.'''
from flask import (Blueprint, request, render_template, flash, url_for,
                   redirect, session)
from flask.ext.login import login_user, login_required, logout_user

from tedx2.extensions import login_manager
from tedx2.user.models import User
from tedx2.public.forms import LoginForm
from tedx2.user.forms import RegisterForm
from tedx2.utils import flash_errors
from tedx2.database import db

blueprint = Blueprint('experimentos', __name__,
                      static_folder="../static", url_prefix='/experimentos')

@blueprint.route("/", methods=["GET", "POST"])
def home():
    return "hola"

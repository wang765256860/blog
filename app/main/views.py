from flask import render_template
from . import main
from .forms import NameForm
from ..models import User
from .. import db


@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User(username=form.name.data)
        db.session.add(user)
        db.session.commit()
    return render_template('index.html', form=form)
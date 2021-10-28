from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from flask_babel import _, lazy_gettext as _l
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField(_l('Title'), validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField(_l('Submit'))
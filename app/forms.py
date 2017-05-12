from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, BooleanField, SelectField, TextAreaField, RadioField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email, EqualTo


class ContactForm(FlaskForm):
    first_name = StringField('first_name', render_kw={'autocomplete':'given-name'})
    last_name = StringField('last_name', render_kw={'autocomplete':'family-name'})
    email = EmailField('email', validators=[DataRequired(), EqualTo('confirm_email', message='Emails Need to Match')], render_kw={'required':'required', 'autocomplete':'email'})
    confirm_email = EmailField('confirm_email', validators=[DataRequired()], render_kw={'required':'required', 'autocomplete':'email'})
    state = SelectField(u'State', validators=[DataRequired()], render_kw={'required':'required', 'autocomplete': 'region'})
    county = StringField(u'County', validators=[DataRequired()], render_kw={'required':'required'})
    position = RadioField('Position', choices=[('cnty_chair','County Chair'),('pct_chair','Precinct Chair'),('prty_member','Party Member')])
    message = TextAreaField('message')
    # recaptcha = RecaptchaField()
    # View code: {{ contact.recaptcha }}

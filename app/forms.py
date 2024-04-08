from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, IPAddress

class ServerForm(FlaskForm):
    name = StringField('Server Name', validators=[DataRequired(message="Server name is required")])
    ip_address = StringField('IP Address', validators=[DataRequired(message="IP address is required"), IPAddress(message="Invalid IP address")])
    is_selected = BooleanField('Select for command')
    submit = SubmitField('Submit')
    vendor = StringField('Vendor')
    description = TextAreaField('Description')

class UploadForm(FlaskForm):
    file = FileField('Excel File', validators=[
        FileRequired(),
        FileAllowed(['xlsx'], 'Excel files only!')
    ])
    submit = SubmitField('Upload')
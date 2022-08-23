from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, TextAreaField,SubmitField
from wtforms.validators import DataRequired, Email

csrf = CSRFProtect()

class FormMensagem(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    mensagem = TextAreaField ('Digite sua mensagem', validators=[DataRequired()])
    botao_submit_enviar = SubmitField('Enviar Mensagem')
    submit = SubmitField("Enviar")
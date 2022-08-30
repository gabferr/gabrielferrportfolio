from forms import FormMensagem, csrf
from flask import Flask, render_template, request, redirect, flash
from flask_mail import Mail, Message
from password import password

app = Flask(__name__)


app.config['SECRET_KEY'] = '85bfb1d10b5c624add777301e572f4a5'

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'goodgamesbrazil@gmail.com'
app.config['MAIL_PASSWORD'] = password
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail()
mail.init_app(app)


@app.route('/')
def home():
    return render_template("exp.html")


@app.route('/experiencia')
def experiencia():
    return render_template("exp.html")


@app.route('/formacao')
def formacao():
    return render_template("formacao.html")


@app.route('/success')
def success():
    return render_template('exp.html')


@app.route('/contato', methods=['POST', 'GET'])
def contato():
    form = FormMensagem()
    if form.validate_on_submit():
        print('-------------------------')
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['subject'])
        print(request.form['message'])       
        print('-------------------------')
        send_message(request.form)
        flash("Mensagem Enviada")
        
    return render_template('contato.html', form=form)


def send_message(message):
    print(message.get('name'))

    msg = Message(message.get('subject'), sender = message.get('email'),
            recipients = ['gabrielferrandin@hotmail.com'],
            body= message.get('message')
    )  
    mail.send(msg)

if __name__ == '__main__':
    app.run(debug=True)

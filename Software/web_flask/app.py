from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

user = 'admin'
# pas = b'$2b$12$ig03bafYI2mXQGNl5j48j.MaWVDCmWHhi4/MTzkrwhQbVQIbVgnhS'
pas = 'password'
user_pas = ''


class General(db.Model):
    cc = db.Column(db.Integer, primary_key=True)
    user_type = db.Column(db.Integer, default=0)
    id_user = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<General %r>' % self.id


class Bibliotecas(db.Model):
    id_req = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, nullable=False)
    id_book = db.Column(db.Integer, nullable=False)
    number_book = db.Column(db.Integer, default=1)
    number_biblio = db.Column(db.Integer, default=1)
    current_use = db.Column(db.Integer, default=1)

    def __repr__(self):
        return '<Bibliotecas %r>' % self.id


class Bicicletas(db.Model):
    id_req = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, nullable=False)
    id_bici = db.Column(db.Integer, nullable=False)
    pto_prestamo = db.Column(db.Integer, default=1)
    damage = db.Column(db.Integer, default=0)
    current_use = db.Column(db.Integer, default=1)

    def __repr__(self):
        return '<Bicicletas %r>' % self.id


class Comedores(db.Model):
    id_req = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, nullable=False)
    comedor_sel = db.Column(db.Integer, default=1)
    franja = db.Column(db.Integer, default=1)
    menu_sel = db.Column(db.Integer, default=1)
    turno_disp = db.Column(db.Integer, default=1)
    wait_time = db.Column(db.Integer, default=0)
    menu_disp = db.Column(db.Integer, default=1)
    turno_act = db.Column(db.Integer, default=1)
    ind_arrive = db.Column(db.Integer, default=1)

    def __repr__(self):
        return '<Comedores %r>' % self.id


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')


@app.route('/admin', methods=['POST', 'GET'])
def admin():
    global user_pas

    if not confirm_login():
        if request.method == 'POST':
            inp_user = request.form['user']
            inp_pas = request.form['pass']
            if inp_user == user and inp_pas == pas:
                user_pas = inp_pas
                return render_template('message.html', msg='Correct login.', category='success')
            else:
                return render_template('message.html', msg='Incorrect password.', category='error')
        return render_template('admin.html')
    else:
        return render_template('message.html', msg='Correct login.', category='success')


@app.route('/cliente', methods=['POST', 'GET'])
def cliente():
    if request.method == 'POST':
        cc = request.form['cc']
        return redirect('/cliente/{}'.format(cc))
    else:
        return render_template('cliente.html')


@app.route('/cliente/<int:cc>')
def cliente_activo(cc):
    try:
        bibliotecas = Bibliotecas.query.filter_by(id_user=cc)
        bicicletas = Bicicletas.query.filter_by(id_user=cc)
        comedores = Comedores.query.filter_by(id_user=cc)
        return render_template('cliente_activo.html', msg='', bibliotecas=bibliotecas,
                               bicicletas=bicicletas, comedores=comedores)
    except:
        return render_template('message.html', msg='Error al acceder a base de datos.', category='error')


def confirm_login():
    return user_pas == pas


if __name__ == "__main__":
    try:
        # bib = Bibliotecas(id_user=1032508596, id_book=85361)
        bic = Bicicletas(id_user=1032508596, id_bici=1456)
        # com = Comedores(student_id=1032508596)

        # db.session.add(bib)
        db.session.add(bic)
        # db.session.add(com)
        db.session.commit()
    except:
        print("Error adding data to database.")

    app.run(debug=True)

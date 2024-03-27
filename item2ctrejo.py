from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# Configuración de la aplicación Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuarios.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicialización de la extensión SQLAlchemy
db = SQLAlchemy(app)

# Definición del modelo de usuario
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

# Función para registrar un nuevo usuario
def registrar_usuario(nombre, apellido, username, password):
    password_hash = generate_password_hash(password)
    nuevo_usuario = Usuario(nombre=nombre, apellido=apellido, username=username, password_hash=password_hash)
    db.session.add(nuevo_usuario)
    db.session.commit()

# Función para validar el usuario y contraseña
def validar_credenciales(username, password):
    usuario = Usuario.query.filter_by(username=username).first()
    if usuario and check_password_hash(usuario.password_hash, password):
        return True
    return False

# Ruta para registrar un nuevo usuario
@app.route('/registrar', methods=['POST'])
def registrar():
    datos = request.json
    nombre = datos.get('nombre')
    apellido = datos.get('apellido')
    username = datos.get('username')
    password = datos.get('password')
    registrar_usuario(nombre, apellido, username, password)
    return 'Usuario registrado correctamente'

# Ruta para validar credenciales
@app.route('/login', methods=['POST'])
def login():
    datos = request.json
    username = datos.get('username')
    password = datos.get('password')
    if validar_credenciales(username, password):
        return 'Inicio de sesión exitoso'
    else:
        return 'Credenciales incorrectas'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(port=8500)

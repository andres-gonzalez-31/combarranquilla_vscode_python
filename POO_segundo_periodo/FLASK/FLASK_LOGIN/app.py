from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector

# Crear aplicación Flask
app = Flask(__name__)
app.secret_key = "clave_secreta"   # Necesario para manejar sesiones

# Configuración Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

# Conexión a MySQL
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",        # 👈 pon tu usuario MySQL
        password="",        # 👈 pon tu contraseña MySQL
        database="flask_login_db"
    )

# Clase User requerida por Flask-Login
class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

# Cargar usuario por id (Flask-Login)
@login_manager.user_loader
def load_user(user_id):
    con = get_db_connection()
    cur = con.cursor(dictionary=True)
    cur.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user_db = cur.fetchone()
    cur.close()
    con.close()
    if user_db:
        return User(user_db["id"], user_db["username"], user_db["password"])
    return None

# Ruta pública
@app.route("/")
def home():
    return render_template("home.html")

# Ruta login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        con = get_db_connection()
        cur = con.cursor(dictionary=True)
        cur.execute("SELECT * FROM users WHERE username = %s", (username,))
        user_db = cur.fetchone()
        cur.close()
        con.close()

        if user_db and check_password_hash(user_db["password"], password):
            user = User(user_db["id"], user_db["username"], user_db["password"])
            login_user(user)
            return redirect(url_for("protegido"))
        else:
            return "Usuario o contraseña incorrectos"

    return render_template("login.html")

# Ruta protegida
@app.route("/protegido")
@login_required
def protegido():
    return render_template("protegido.html", username=current_user.username)

# Ruta logout
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))

# Ejecutar aplicación
if __name__ == "__main__":
    app.run(debug=True)

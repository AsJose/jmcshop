from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__)

# Función para verificar usuario
def verificar_usuario(username, password):
    try:
        conn = psycopg2.connect(
            host="localhost",
            dbname="paginaweb",
            user="postgres",
            password="thinkyt2022."  
        )
        cur = conn.cursor()
        cur.execute("SELECT * FROM usuarios WHERE username=%s AND password=%s", (username, password))
        user = cur.fetchone()
        cur.close()
        conn.close()
        return user
    except Exception as e:
        print("Error al conectar con la base de datos:", e)
        return None

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if verificar_usuario(username, password):
        return redirect(url_for('home', user=username))
    else:
        return "Credenciales incorrectas"

@app.route('/home')
def home():
    user = request.args.get('user', 'Invitado')
    return render_template('home.html', usuario=user)

if __name__ == '__main__':
    app.run(debug=True)

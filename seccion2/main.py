# Escriba una aplicación Flask que implemente autenticación básica
# utilizando un middleware. La aplicación debe tener una ruta protegida
# que solo pueda ser accesible después de autenticarse.

from flask import Flask, request, Response
import sqlite3

app = Flask(__name__)

class AuthMiddleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        auth = request.authorization
        if not auth or not self.check_auth(auth.username, auth.password):
            return self.require_auth()
        return self.app(environ, start_response)

    def check_auth(self, username, password):
        try:
            conn = sqlite3.connect('base.sqlite')
            cursor = conn.cursor()

            cursor.execute("SELECT username, password FROM users WHERE username=?, password=?", (username, password))
            user_auth = cursor.fetchone()

            if user_auth:
                return True
            else:
                return False
        finally:
            if conn:
                conn.close()

    def require_auth(self):
        return Response('Acceso no autorizado', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})

app.wsgi_app = AuthMiddleware(app.wsgi_app)

@app.route('/ruta_protegida')
def ruta_protegida():
    return 'Acceso autorizado.'

if __name__ == '__main__':
    app.run(debug=True)

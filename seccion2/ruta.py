# Escriba una ruta en Flask que acepte una solicitud GET
# con un parámetro de consulta 'user_id' y devuelva la información 
# del usuario desde una base de datos SQLite.

from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/user_info', methods=['GET'])
def get_user_info():
    user_id = request.args.get('user_id')

    if not user_id:
        return jsonify({'error': 'user_id es requerido'}), 400

    try:
        conn = sqlite3.connect('base.sqlite')
        cursor = conn.cursor()

        cursor.execute("SELECT user_id, username, email FROM users WHERE user_id=?", (user_id,))
        user_info = cursor.fetchone()

        if user_info:
            user_dict = {
                'user_id': user_info[0],
                'username': user_info[1],
                'email': user_info[2]
            }
            return jsonify(user_dict), 200
        else:
            return jsonify({'error': 'user_id inexistente'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify, send_from_directory
import sqlite3
import hashlib
import jwt
from datetime import datetime, timedelta
from functools import wraps
import os

# Nastavení cesty k složce s webovými soubory
current_dir = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, static_url_path='', static_folder=current_dir)
app.config['SECRET_KEY'] = 'PJExpedisWMS2024'

# Konfigurace pro CORS
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Obsluha základních routů pro statické soubory
@app.route('/')
def serve_login():
    return send_from_directory(current_dir, 'login.html')

@app.route('/index.html')
def serve_index():
    return send_from_directory(current_dir, 'index.html')

@app.route('/content/<path:path>')
def serve_content(path):
    return send_from_directory(os.path.join(current_dir, 'content'), path)

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({'error': 'Chybí přihlašovací údaje'}), 400
    
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE username = ?', 
                       (username,)).fetchone()
    conn.close()
    
    if user and verify_password(password, user['password_hash']):
        token = generate_token(dict(user))
        return jsonify({
            'token': token,
            'username': user['username'],
            'name': user['name']
        })
    
    return jsonify({'error': 'Nesprávné přihlašovací údaje'}), 401

def verify_password(password, password_hash):
    return hashlib.sha256(password.encode()).hexdigest() == password_hash

def generate_token(user):
    payload = {
        'user_id': user['id'],
        'username': user['username'],
        'exp': datetime.utcnow() + timedelta(days=1)
    }
    return jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')

# Middleware pro ověření tokenu
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        
        if not token:
            return jsonify({'error': 'Token chybí'}), 401
        
        try:
            token = token.split(" ")[1]  # Odstranění "Bearer " z tokenu
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        except:
            return jsonify({'error': 'Neplatný token'}), 401
            
        return f(*args, **kwargs)
    return decorated

# Testovací endpoint pro ověření přihlášení
@app.route('/api/protected', methods=['GET'])
@token_required
def protected():
    return jsonify({'message': 'Tento endpoint je chráněný, přístup povolen'})

if __name__ == '__main__':
    app.run(debug=True, port=8080)
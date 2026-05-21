import os
from flask import Flask, jsonify
import pymysql

app = Flask(__name__)

def get_db_connection():
    return pymysql.connect(
        host=os.environ.get('MYSQL_HOST', 'mysql-service'),
        user=os.environ.get('MYSQL_USER', 'admin'),
        password=os.environ.get('MYSQL_PASSWORD', 'admin123'),
        database=os.environ.get('MYSQL_DATABASE', 'appdb'),
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route('/')
def health():
    return jsonify({"status": "healthy", "message": "Flask app is running!"})

@app.route('/db-status')
def db_status():
    try:
        conn = get_db_connection()
        conn.ping()
        conn.close()
        return jsonify({"database": "connected"})
    except Exception as e:
        return jsonify({"database": "error", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

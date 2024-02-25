from flask import Flask, request, jsonify
from cryptography.fernet import Fernet

app = Flask(__name__)

@app.route('/encrypt', methods=['POST'])
def encrypt():
    key = request.form['key']
    message = request.form['message']
    cipher_suite = Fernet(key)
    encrypted_message = cipher_suite.encrypt(message.encode())
    return jsonify({'encrypted_message': encrypted_message.decode()})

@app.route('/decrypt', methods=['POST'])
def decrypt():
    key = request.form['key']
    encrypted_message = request.form['encrypted_message']
    cipher_suite = Fernet(key)
    decrypted_message = cipher_suite.decrypt(encrypted_message.encode())
    return jsonify({'decrypted_message': decrypted_message.decode()})

if __name__ == '__main__':
    app.run(debug=True)


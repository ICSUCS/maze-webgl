from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder='Build')  # 默认WebGL导出文件夹名叫 Build

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def serve_file(path):
    return send_from_directory('.', path)

if __name__ == '__main__':
    print("🔵 WebGL server running at http://localhost:5000")
    app.run(host='0.0.0.0', port=5000)
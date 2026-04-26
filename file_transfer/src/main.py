from dotenv import load_dotenv
load_dotenv()
import os
from flask import Flask
from routes.files import files_bp

app = Flask(__name__)

# Подключаем роуты
app.register_blueprint(files_bp)

HOST = os.getenv('HOST', "127.0.0.1")
PORT = int(os.getenv('PORT', 3000))
DEBUG = os.getenv("DEBUG", "true").lower() == "true"

if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=DEBUG)
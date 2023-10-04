import os
from flask import Flask
from flask import Response
from flask import request

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    return 'OK'

@app.route("/")
def hello():
    ENV = os.environ.get("ENV")  # Read the environment variable
    VERSION = os.environ.get("VERSION")  #Read the version variable

    if ENV == "prod":
        return f"This is production environment (Version: {VERSION})"
    elif ENV == "stage":
        return f"This is staging environment with (Version: {VERSION})"
    else:
        return f"This is an unknown environment with (Version: {VERSION})"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)


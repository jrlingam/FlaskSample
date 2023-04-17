from flask import Flask
from flask import render_template
import os

app = Flask(__name__)
__version_info__ = ('1', '0', '3')
__version__ = '.'.join(__version_info__)

@app.route("/")
def home():
    return render_template('index.html', appVersion = __version__)

@app.route('/app')
def blog():
    return "Hello, from Flask App !!     Version:" + __version__

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8081))
    app.run(debug=True,host='0.0.0.0',port=port)
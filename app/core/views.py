from app import app
from flask import render_template, send_from_directory

@app.route("/")
def index():
    """
    Just index
    """
    return render_template('index.html')

@app.route('/docs/', defaults={'filename': 'index.html'})
@app.route('/docs/<path:filename>')
def documentation(filename):
    print(app.static_folder + filename)
    return send_from_directory(app.static_folder + 'html',filename)
from flask import Flask, render_template, request, send_from_directory
from serve_files import serve
import sys
import os
import datetime
import actions

app = Flask(__name__)
app.register_blueprint(serve)

logger = actions.OverWatch_Logger()


@app.route('/', methods = ['GET'])
def home():
	return render_template('index.html')


##### using library to send logs to CloudWatch ####
@app.route('/send_log', methods = ['GET'])
def library_action():
	print("ERERE")
	user = "El Jeffe"
	filename = "malware.dll"
	logger.monitor_event("CRITICAL", "OverWatch Demo Echo", "FILE UPLOAD", f"User {user} has uploaded the file: f{filename}")
	return "blah"

@app.route('/favicon.ico', methods = ['GET'])
def favicon():
	return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')


if __name__ == "__main__":
	app.run(host="0.0.0.0", port=80, debug=True)


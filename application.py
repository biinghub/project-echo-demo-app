from flask import Flask, render_template, request, send_from_directory
import sys
import os
import datetime
import actions

application = app = Flask(__name__)

logger = actions.OverWatch_Logger()

@application.route('/', methods = ['GET'])
def home():
	return render_template('index.html')

##### using library to send logs to CloudWatch ####
@application.route('/send_log', methods = ['GET'])
def library_action():
	user = "El Jeffe"
	filename = "malware.dll"
	logger.monitor_event("CRITICAL", "OverWatch Demo Echo", "FILE UPLOAD", f"User {user} has uploaded the file: {filename}")
	return "blah"

@application.route('/favicon.ico', methods = ['GET'])
def favicon():
	return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@application.route('/b3ff_jez0s_secr3t_s4uce.txt', methods = ["GET"])
def serve_file1():
	return send_from_directory(os.path.join(serve.root_path, 'static'), 'list/b3ff_jez0s_secr3t_s4uce.txt')

@application.route('/file2.db', methods = ["GET"])
def serve_file2():
	return send_from_directory(os.path.join(serve.root_path, 'static'), 'list/file2.txt')

@application.route('/file3.bat', methods = ["GET"])
def serve_file3():
	return send_from_directory(os.path.join(serve.root_path, 'static'), 'list/file3.txt')

@application.route('/malware.dll', methods = ["GET"])
def serve_file4():
	return send_from_directory(os.path.join(serve.root_path, 'static'), 'list/file4.txt')


if __name__ == "__main__":
	application.run(debug=True)

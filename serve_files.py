from flask import Flask, send_from_directory, Blueprint, request
import os

serve = Blueprint('serve', __name__)

@serve.route('/file1.txt', methods = ["GET"])
def serve_file1():
	return send_from_directory(os.path.join(serve.root_path, 'static'), 'list/file1.txt')

@serve.route('/file2.db', methods = ["GET"])
def serve_file2():
	return send_from_directory(os.path.join(serve.root_path, 'static'), 'list/file2.txt')

@serve.route('/file3.bat', methods = ["GET"])
def serve_file3():
	return send_from_directory(os.path.join(serve.root_path, 'static'), 'list/file3.txt')

@serve.route('/malware.dll', methods = ["GET"])
def serve_file4():
	return send_from_directory(os.path.join(serve.root_path, 'static'), 'list/file4.txt')

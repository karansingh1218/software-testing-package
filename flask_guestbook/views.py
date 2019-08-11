from flask import Blueprint, render_template, request

main = Blueprint('main', __name__)

@main.route('/', methods=['POST'])
def result():
	print(request.form['foo'])
	return 'Received'


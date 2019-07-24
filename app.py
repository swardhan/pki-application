from flask import Flask, render_template, request, jsonify
from pki_cert import sign_cert
from pki_revoke import revoke_cert

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/create')
def create():
	return render_template('create.html')

@app.route('/revoke')
def revoke():
	return render_template('revoke.html')

@app.route('/revoke_cert', methods=['POST'])
def revoke_certificate():
	content = request.get_json()
	url = content["url"]
	print(url)
	revoke_cert(url)
	return jsonify({'result': 'Revoked'})


@app.route('/create_cert', methods=['POST'])
def create_certificate():
	content = request.get_json()
	url = content["url"]
	passphrase = content["passphrase"]
	domain = url.split('.')[0]
	print(url, domain, passphrase)
	sign_cert(url, domain, passphrase)

	return jsonify({'result': 'Created'})

if __name__ == '__main__':
	app.run(port=5000, debug=True)
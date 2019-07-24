import os

OPENSSL_CONFIG_TEMPLATE = """
prompt = no
distinguished_name = req_distinguished_name
req_extensions = v3_req
[ req_distinguished_name ]
C                      = US
ST                     = IL
L                      = Chicago
O                      = Example
OU                     = Examplel Software Authority
CN                     = %(domain)s
emailAddress           = example@abc.com
[ v3_req ]
# Extensions to add to a certificate request
basicConstraints = CA:FALSE
keyUsage = nonRepudiation, digitalSignature, keyEncipherment
subjectAltName = @alt_names
[ alt_names ]
DNS.1 = %(domain)s
DNS.2 = *.%(domain)s
"""

MYDIR = os.path.abspath(os.path.dirname(__file__))

def create_cert(url, domain, passphrase):
	os.system('openssl req -new -config domains/'+domain+'.conf -out certs/'+url+'.csr -keyout certs/'+url+'.key -passout pass:'+passphrase)
	os.system('openssl ca -batch -config etc/signing-ca.conf  -in certs/'+url+'.csr  -out certs/'+url+'.crt  -extensions server_ext -passin pass:qwer1234')
	print('Cert Created')
	return {'result': 'Cert Created for '+url}

def sign_cert(url, domain, passphrase):
	if not os.path.isfile(os.path.join(MYDIR, 'certs',url+'.crt')):
		config = open(os.path.join(MYDIR, 'domains', domain+'.conf'), 'w')
		config.write(OPENSSL_CONFIG_TEMPLATE % {'domain': url})
		config.close()
		create_cert(url, domain, passphrase)
	else:
		print('Already Exists')
		return {'result': 'Already Exists'}
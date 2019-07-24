import os

def revoke_cert(url):
	os.system('openssl ca -config etc/signing-ca.conf -revoke certs/'+url+'.crt -passin pass:qwer1234')
	print('Certificate Revoked')
	return {'result': 'Certificate Revoked for '+ url}
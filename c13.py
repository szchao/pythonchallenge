import xmlrpc.client

proxy = xmlrpc.client.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
resp = proxy.phone('Bert')
print(resp)
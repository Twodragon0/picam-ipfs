import ipfshttpclient
import sys

# Share TCP connections using a context manager
with ipfshttpclient.connect() as client:
	hash = client.add('data', recursive=True)[-1]['Hash']
        print(hash)
        sys.stdout = open('data/ipfs_hash.txt','a')
        print(hash)

# Share TCP connections until the client session is closed
class SomeObject:
	def __init__(self):
		self._client = ipfshttpclient.connect(session=True)

	def do_something(self):
		hash = self._client.add('data',recursive=True)[-1]['Hash']
		print(self._client.stat(hash))
		sys.stdout = open('data/ipfs_hash.txt','a')
		print(self._client.stat(hash))

	def close(self):  # Call this when your done
		self._client.close()

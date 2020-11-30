# Script hash_func to be used in main.da and client.da
#
import hashlib

def hash_func(name, m):
	hash = int(hashlib.sha1(name.encode('utf-8')).hexdigest(), 16)
	hash_val = hash % 2**m
	return hash_val
# Script hash_func to be used in main.da and client.da
#
import hashlib
import zlib
import configparser
from passlib.context import CryptContext


def hash_func(name, m):
    return int(zlib.crc32(bytes(name.encode('utf-8')))) % 2 ** m
    # config = configparser.ConfigParser()
    # config.read('config.ini')
    # if "adler32" in config.get("DEFAULT", "HASH_FX"):
    #     return int(zlib.crc32(bytes(name.encode('utf-8')))) % 2 ** m

    # if type == 1:
    #     return int(hashlib.sha1(name.encode('utf-8')).hexdigest(), 16) % 2 ** m
    # elif type == 2:
    #     return int(hashlib.sha256(name.encode('utf-8')).hexdigest(), 16) % 2 ** m
    # elif type == 3:
    #     return int(zlib.adler32(bytes(name.encode('utf-8')))) % 2 ** m
    # elif type == 4:

# def hash_sha1(name, m):
#     hash =
#     hash_val = hash
#     return hash_val
#
#
# def hash_sha256(name, m):
#     hash =
#     hash_val = hash % 2 ** m
#     return hash_val
#
#
# def adler32(name, m):
#     print("name = "+str(name))
#     print("name = "+str(m))
#     hash = int(zlib.adler32(bytes(name.encode('utf-8'))))
#     hash_val = hash % 2 ** m
#     return hash_val
#
#
# def crc32(name, m):
#     hash = int(zlib.crc32(bytes(name.encode('utf-8'))))
#     hash_val = hash % 2 ** m
#     return hash_val

import hashlib


md5 = hashlib.md5()

md5.update('123456')

print md5.hexdigest()
import hashlib
from simplecrypt import encrypt,decrypt
n="Devik:hello"
def SHA256():
    result=hashlib.sha256(n.encode())
    print("SH256 encrypted data:",result.hexdigest())
    SHA256()
    
def MD5():
    result =hashlib.md5(n.encode())
    print("SH256 encrypted data:",result.hexdigest())
    MD5
    
    message ="Devik:hello"
    hex_string='' 
    

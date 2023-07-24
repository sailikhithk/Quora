#Cryptography
from cryptography.fernet import Fernet

encrypt_key=b'secret message!'

def encrypt(data):
    data = data.encode()
    f = Fernet(encrypt_key)
    return f.encrypt(data).decode('utf-8')

def decrypt(data):
    data = data.encode()
    f = Fernet(encrypt_key)
    return f.decrypt(data).decode('utf-8')

def obj_to_list(data):
    list_dicts = []
    for obj in data:
        temp_dic = obj.__dict__
        temp_dic.pop("_sa_instance_state", None)
        list_dicts.append(temp_dic)
    return list_dicts
import pickle
from cryptography.fernet import Fernet
import getpass
import os

def save_as_pkl(filepath, obj):
    with open(filepath, 'wb') as f:
        pickle.dump(obj, f)

def load_from_pkl(filepath):
    with open(filepath, 'rb') as f:
        obj = pickle.load(f)
    return obj


# 先保存一个pkl文件（注意，后缀可以是任意的，不一定是pkl）
save_path = r'D:\@git\sign_simulate\bladder_stone\data\data.ainimal'
save_as_pkl(save_path, [1, 2, 3, 4, 5])


# 生成密钥并保存到文件
key = Fernet.generate_key()
with open(r'D:\@git\sign_simulate\bladder_stone\data\secret.key', 'wb') as key_file:
    key_file.write(key)

# 使用密钥加密文件
if True:
    f = Fernet(key)
    # 读取文件内容
    with open(save_path, 'rb') as file:
        file_data = file.read()

    # 加密文件
    encrypted_data = f.encrypt(file_data)

    # 写入加密数据到文件
    with open(save_path+'.raw ', 'wb') as file:
        file.write(encrypted_data)



# 使用密钥解密文件
if True:
    key = input('Please input your key: ')
    f = Fernet(key)
    # 读取文件内容
    with open(save_path+'.raw ', 'rb') as file:
        encrypted_data = file.read()

    # 解密文件
    decrypted_data = f.decrypt(encrypted_data)

    # 写入解密数据到文件
    with open(save_path+'.read', 'wb') as file:
        file.write(decrypted_data)

# 读取解密后的文件
data = load_from_pkl(save_path+'.read')
print(data)

# 删除解密后的文件
os.remove(save_path+'.read')
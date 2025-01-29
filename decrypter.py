import os
import pyaes
import sys

if len(sys.argv) != 3:
    print("Os nomes dos arquivos nao foram dados. Use: python decrypter.py <filename-encrypted> <filename-decrypted>")
    sys.exit(1)  # Indicate an error


## abrir o arquivo criptografado
file_name = sys.argv[1]
file = open(file_name, "rb")
file_data = file.read()
file.close()

## chave para descriptografia
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

## remover o arquivo criptografado
os.remove(file_name)

## criar o arquivo descriptografado
new_file = sys.argv[2]
new_file = open(f'{new_file}', "wb")
new_file.write(decrypt_data)
new_file.close()

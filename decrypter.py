import os
import pyaes

encrypted_file = "arquivo_secreto.txt.ransomware"

with open(encrypted_file, "rb") as file:
    encrypted_data = file.read()

key = b"chave_secreta_123"
aes = pyaes.AESModeOfOperationCTR(key)
decrypted_data = aes.decrypt(encrypted_data)

os.remove(encrypted_file)

decrypted_file = "arquivo_secreto.txt"
with open(decrypted_file, "wb") as file:
    file.write(decrypted_data)

print(f"Arquivo '{decrypted_file}' restaurado com sucesso.")

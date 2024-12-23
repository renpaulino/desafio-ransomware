import os
import pyaes


def decrypt_file(file_name, key):
    # Verificar se o arquivo existe
    try:
        # Abrir o arquivo criptografado
        with open(file_name, "rb") as file:
            file_data = file.read()
    except FileNotFoundError:
        print(f"Erro: O arquivo '{file_name}' não foi encontrado.")
        return

    # Inicializar AES
    aes = pyaes.AESModeOfOperationCTR(key)

    # Descriptografar os dados
    decrypt_data = aes.decrypt(file_data)

    # Remover o arquivo criptografado
    os.remove(file_name)

    # Criar o arquivo descriptografado
    original_file_name = file_name.replace(".ransomwaretroll", "")
    with open(original_file_name, "wb") as new_file:
        new_file.write(decrypt_data)

    print(f"Arquivo '{file_name}' descriptografado com sucesso como '{original_file_name}'.")


if __name__ == "__main__":
    # Nome do arquivo e chave de descriptografia
    file_name = "teste.txt.ransomwaretroll"
    key = b"testeransomwares"

    # Chamar a função para descriptografar o arquivo
    decrypt_file(file_name, key)

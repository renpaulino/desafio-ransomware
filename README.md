# Entendendo um Ransomware na Prática

## Ferramentas

- Kali Linux
- Python
- Pacote pyaes

## Instalando Pyaes no Kali Linux
```bash
sudo apt update
sudo apt install python3-pyaes
```
### Desafio
Exibindo o conteúdo do diretório:
- Script de descriptografia em python
- Script de criptografia em python
- Arquivo com um texto comum
![Alt text](./prints/1etapa.png "conteúdo do diretório: decrypter.py, encrypter.py, teste.txt")

Conteúdo do teste.txt
![Alt text](./prints/conteudotxt1.png "Mensagem do arquivo: Hello World")

Criptografando a mensagem
Por causa do Script, o nome do arquivo foi alterado para teste.txt.ransonwaretroll
![Alt text](./prints/2etapa.png)

Conteúdo do teste.txt.ransonwaretroll
![Alt text](./prints/conteudotxt2.png "Mensagem do arquivo: são vários simbolos aleatórios")

Descriptografando a mensagem
O nome do arquivo foi alterado para o seu título original (teste.txt)
![Alt text](./prints/3etapa.png)

Verificação da descriptografia
A mensagem Hello World é legível agora
![Alt text](./prints/conteudotxt3.png)


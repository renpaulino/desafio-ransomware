*Simulando um ataque de Ransomware*
----
***Objetivo:***
- Criptografar e Descriptografar arquivos.
  
***Tecnologias:***
- Python:
  - com a biblioteca pyaes que implementa o algoritmo de criptografia AES (Advanced Encryption Standard), um dos algoritmos mais seguros e utilizados.
    
- Necessária a sua instalação:
``apt install python3-pyaes``

***Resultados***

https://github.com/user-attachments/assets/eaf475b7-22c6-4149-999e-f40abc6e37d5

![pj-3](https://github.com/user-attachments/assets/70b4121c-caf9-4186-ba0a-f81741b834d4)

***Texto criptografado***
-----
![pj-2](https://github.com/user-attachments/assets/478c4705-eea5-4c97-a32d-6fffb6a59f35)

***Projeto DIO - Instrutor Cassiano***
-----
***Funcionamento:***
-----
- Seleção do Arquivo: O script seleciona um arquivo txt específico para criptografar.
- Criptografia: O conteúdo do arquivo é criptografado utilizando o algoritmo AES com uma chave secreta.
- Remoção do Arquivo Original: O arquivo original é removido para simular a exclusão dos dados.
- Criação do Arquivo Criptografado: Um novo arquivo com a extensão ".ransomwaretroll" é criado, contendo os dados criptografados
- Descriptografia: A descriptografia foi realizada utilizando o mesmo algoritmo (AES) e a chave fornecida pelo atacante. O processo consistiu na inversão da criptografia, revertendo a transformação dos dados para sua forma original.

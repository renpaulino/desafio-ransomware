# Ransomware Simples (Para Estudos)

Este projeto é um **simulador de ransomware educacional** que criptografa e descriptografa arquivos em uma pasta específica. Foi desenvolvido para **fins didáticos** e **experimentos em segurança da informação**, demonstrando como funciona a criptografia AES no modo CTR.

⚠️ **ATENÇÃO**: Este projeto é estritamente para aprendizado. Não utilize para fins maliciosos ou ilegais. O uso inadequado pode resultar em implicações legais.

---

## 🚀 Funcionalidades

1. **Criptografia**:
   - Criptografa todos os arquivos em uma pasta usando uma chave AES.
   - Remove os arquivos originais e os substitui pelos arquivos criptografados.
   - Exibe um pop-up (no Windows) informando que os arquivos foram criptografados.

2. **Descriptografia**:
   - Descriptografa os arquivos que foram previamente criptografados pelo script.
   - Substitui os arquivos criptografados pelos originais.

---

## 📁 Estrutura do Projeto

ransomware_project/
│
├── encrypt.py        # Script para criptografar arquivos
├── decrypt.py        # Script para descriptografar arquivos
├── pasta/            # Pasta com arquivos de texto para teste
│   ├── copia.txt
│   ├── copia1.txt
│   ├── copia2.txt
│   ├── copia3.txt
│   ├── copia4.txt
│   ├── copia5.txt
│   ├── copia6.txt
│   ├── copia7.txt
│   ├── copia8.txt
│   ├── copia9.txt
│   └── copia10.txt
└── README.md         # Este arquivo de documentação

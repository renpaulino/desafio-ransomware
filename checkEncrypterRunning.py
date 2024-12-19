import psutil

# Nome do arquivo ou script malicioso
malicious_name = "criptografar.py"

def check_malicious_execution():
    for process in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            # Verifica se o nome ou comando do processo coincide com o nome do script malicioso
            if malicious_name in process.info['name'] or \
               (process.info['cmdline'] and malicious_name in process.info['cmdline']):
                print(f"⚠️ Processo suspeito detectado: {process.info}")
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            # Ignora processos inacessíveis
            continue
    print("✅ Nenhum processo suspeito detectado.")
    return False

if __name__ == "__main__":
    if check_malicious_execution():
        print("Processo malicioso em execução!")

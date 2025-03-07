import os
import unicodedata

def remover_acentos(texto):
    # Normaliza o texto e remove os acentos
    return ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn')

def detectar_baidunetdisk():
    # Definir os caminhos comuns de instalação
    caminhos = [
        r"C:\Program Files\BaiduNetdisk",
        r"C:\Program Files (x86)\BaiduNetdisk",
        os.path.expanduser(r"~\AppData\Roaming\BaiduNetdisk"),
        os.path.expanduser(r"~\BaiduNetdisk")
    ]

    # Verificar se o executável principal existe
    executaveis = [
        "BaiduNetdisk.exe",
        "BaiduNetdiskApp.exe"  # Caso haja outras versões executáveis
    ]
    
    encontrado = False
    log_msg = ""  # Variável para armazenar as mensagens de log

    for caminho in caminhos:
        # Verificar se a pasta de instalação existe
        if os.path.exists(caminho):
            log_msg += f"Pasta encontrada: {caminho}\n"
            
            # Verificar a presença do executável principal
            for exe in executaveis:
                exe_path = os.path.join(caminho, exe)
                if os.path.exists(exe_path):
                    log_msg += f"Executável encontrado: {exe_path}\n"
                    encontrado = True
                    break

            # Verificar pastas de configuração e cache
            config_path = os.path.join(caminho, "Config")
            cache_path = os.path.join(caminho, "Cache")
            logs_path = os.path.join(caminho, "Logs")
            resources_path = os.path.join(caminho, "Resources")

            if os.path.exists(config_path):
                log_msg += f"Pasta de Configuração encontrada: {config_path}\n"
            if os.path.exists(cache_path):
                log_msg += f"Pasta de Cache encontrada: {cache_path}\n"
            if os.path.exists(logs_path):
                log_msg += f"Pasta de Logs encontrada: {logs_path}\n"
            if os.path.exists(resources_path):
                log_msg += f"Pasta de Recursos encontrada: {resources_path}\n"

    if encontrado:
        # Remover os acentos do log
        log_msg = remover_acentos(log_msg)

        # Salvar o log no arquivo de log
        log_path = r"C:\Windows\Temp\Baidu_Detector.txt"
        try:
            with open(log_path, 'w') as log_file:
                log_file.write(log_msg)
            print(f"Log salvo em: {log_path}")
        except Exception as e:
            print(f"Erro ao salvar o log: {e}")

# Chamar a função para verificar o BaiduNetDisk
detectar_baidunetdisk()

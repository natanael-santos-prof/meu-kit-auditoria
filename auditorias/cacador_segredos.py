import os
import time

# Termos proibidos que indicam que o programador esqueceu uma credencial no código
termos_perigosos = ["senha =", "password =", "api_token =", "api_key =", "secret ="]

print("--- INICIANDO INSPEÇÃO AUTOMÁTICA DE ARQUIVOS (DEVSECOPS) ---")
print("Vasculhando o diretório atrás de arquivos de código e senhas expostas...\n")
time.sleep(1.0)

vulnerabilidade_encontrada = False

# O robô lista todos os arquivos que existem na pasta atual de trabalho
# (Quando roda no GitHub Actions, ele varre a pasta do repositório)
arquivos_na_pasta = os.listdir('.')

for nome_arquivo in arquivos_na_pasta:
    # O robô filtra para ler APENAS arquivos de código Python (ignorando manuais e o próprio script)
    if nome_arquivo.endswith('.py') and nome_arquivo != 'cacador_segredos.py':
        print(f"🔍 Inspecionando arquivo real encontrado: [{nome_arquivo}]")
        
        try:
            # Abre o arquivo real em modo de leitura externa
            with open(nome_arquivo, 'r', encoding='utf-8', errors='ignore') as arquivo_codigo:
                
                # Lê o arquivo linha por linha direto do disco
                for numero_linha, linha_texto in enumerate(arquivo_codigo, start=1):
                    linha_minuscula = linha_texto.lower()
                    
                    # Procura os termos perigosos dentro da linha atual
                    for termo in termos_perigosos:
                        if termo in linha_minuscula:
                            print(f"  🚨 [ALERTA] Credencial Exposta no arquivo [{nome_arquivo}] -> Linha {numero_linha}!")
                            print(f"  💥 Trecho Flagrado: \"{linha_texto.strip()}\"\n")
                            vulnerabilidade_encontrada = True
                            
        except Exception as e:
            print(f"⚠️ Erro ao tentar ler o arquivo {nome_arquivo}: {e}")

if not vulnerabilidade_encontrada:
    print("🔒 Seguro: Nenhum arquivo do projeto possui senhas ou chaves expostas. Aprovado!")

print("\n--- INSPEÇÃO DE CÓDIGO CONCLUÍDA ---")

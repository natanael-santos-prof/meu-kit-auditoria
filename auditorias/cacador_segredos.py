import os
import time

# Termos proibidos que indicam credenciais esquecidas no código
termos_perigosos = ["senha =", "password =", "api_token =", "api_key =", "secret ="]

print("--- INICIANDO INSPEÇÃO PROFUNDA E RECURSIVA (DEVSECOPS) ---")
print("O Cão Farejador está vasculhando todas as pastas e subpastas do projeto...\n")
time.sleep(1.0)

vulnerabilidade_encontrada = False

# TÉCNICA AVANÇADA: os.walk vai caminhar por TODAS as subpastas automaticamente
# 'raiz' descobre onde estamos, 'pastas' mapeia subdiretórios e 'arquivos' lista os códigos
for raiz, pastas, arquivos in os.walk('.'):
    
    for nome_arquivo in arquivos:
        # Filtra para analisar apenas arquivos de código Python, ignorando o próprio caçador
        if nome_arquivo.endswith('.py') and nome_arquivo != 'cacador_segredos.py':
            
            # Descobre o caminho completo do arquivo (ex: ./projeto_novo/site.py)
            caminho_completo = os.path.join(raiz, nome_arquivo)
            print(f"🔍 Farejando arquivo: {caminho_completo}")
            
            try:
                # Abre o arquivo para ler as linhas de texto por fora
                with open(caminho_completo, 'r', encoding='utf-8', errors='ignore') as arquivo_codigo:
                    
                    for numero_linha, linha_texto in enumerate(arquivo_codigo, start=1):
                        linha_minuscula = linha_texto.lower()
                        
                        # Caça termos proibidos dentro da linha atual
                        for termo in termos_perigosos:
                            if termo in linha_minuscula:
                                print(f"  🚨 [ALERTA DE SEGURANÇA] Credencial Exposta!")
                                print(f"  📂 Arquivo: {caminho_completo}")
                                print(f"  📍 Linha: {numero_linha}")
                                print(f"  💥 Trecho Flagrado: \"{linha_texto.strip()}\"\n")
                                vulnerabilities_encontrada = True
                                
            except Exception as e:
                print(f"⚠️ Erro ao tentar ler o arquivo {caminho_completo}: {e}")

if not vulnerabilidade_encontrada:
    print("🔒 Perfeito! O Cão Farejador vasculhou todas as subpastas e o projeto está 100% SEGURO.")
else:
    print("❌ REPROVADO: Foram encontrados segredos expostos na estrutura de pastas.")

print("\n--- VARREDURA RECURSIVA CONCLUÍDA ---")

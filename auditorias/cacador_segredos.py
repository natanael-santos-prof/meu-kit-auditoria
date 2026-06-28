import time

# Simulação de um arquivo de código real que um programador da empresa escreveu (site_vendas.py)
# Olhe com atenção: o programador cometeu o erro gravíssimo de deixar senhas expostas no texto!
codigo_do_desenvolvedor = [
    "import os",
    "print('Inicializando sistema de vendas v1.0')",
    "banco_dados_url = 'mongodb://localhost:27017'",
    "usuario_admin = 'root'",
    "senha_secreta = 'SuperSenhaBanco2026!'", # 🚨 ERRO GRAVE: Senha exposta na linha 5!
    "def conectar_banco():",
    "    api_token = 'api_key_xyz1234567890abcdef'", # 🚨 ERRO GRAVE: Chave de acesso exposta!
    "    return 'Conectado com sucesso'"
]

# Termos proibidos que indicam que o programador esqueceu uma credencial no código
termos_perigosos = ["senha =", "password =", "api_token =", "api_key =", "secret ="]

print("--- INICIANDO INSPEÇÃO DE SEGURANÇA NO CÓDIGO (DEVSECOPS) ---")
print("Vasculhando linhas de programação atrás de senhas e segredos expostos...\n")
time.sleep(1.0)

vulnerabilidade_encontrada = False

# O robô fiscal analisa o código linha por linha, como se estivesse revisando uma redação
for numero_linha, linha_texto in enumerate(codigo_do_desenvolvedor, start=1):
    
    # Passa o texto para letras minúsculas para não deixar passar nada (ex: Senha, SENHA, senha)
    linha_minuscula = linha_texto.lower()
    
    # Verifica se algum dos termos proibidos está presente nesta linha
    for termo in termos_perigosos:
        if termo in linha_minuscula:
            print(f"🚨 [ALERTA DE SEGURANÇA] Credencial Exposta Detectada na Linha {numero_linha}!")
            print(f"💥 Trecho do Código Flagrado: \"{linha_texto.strip()}\"")
            print(f"📊 Risco: Um hacker pode ler esse arquivo e roubar o acesso ao nosso sistema.\n")
            vulnerabilidade_encontrada = True

if not vulnerabilidade_encontrada:
    print("🔒 Seguro: Nenhuma senha ou chave secreta foi encontrada exposta no código. Aprovado!")

print("--- INSPEÇÃO DE CÓDIGO CONCLUÍDA ---")

import time

# Simulação de um arquivo de configuração real de um servidor na nuvem (AWS/Azure)
# O engenheiro de nuvem cometeu falhas graves ao configurar as regras de acesso!
configuracao_servidor = {
    "nome_servidor": "servidor-producao-clientes",
    "firewall_ativo": False,                     # 🚨 ERRO GRAVE: Firewall desligado!
    "porta_banco_dados": "publica",              # 🚨 ERRO GRAVE: Banco de dados exposto para a internet!
    "criptografia_discos": True,                 # Correto: Arquivos estão criptografados
    "acesso_remoto_ssh": "apenas_ips_da_empresa" # Correto: Acesso remoto trancado
}

print("--- INICIANDO AUDITORIA DE INFRAESTRUTURA COMO CÓDIGO (DEVSECOPS) ---")
print("Analisando as plantas digitais dos servidores antes da ativação na nuvem...\n")
time.sleep(1.0)

infraestrutura_segura = True

# 1. Teste do Firewall Principal
if not configuracao_servidor["firewall_ativo"]:
    print("🚨 [ALERTA CRÍTICO] Falha de Configuração de Rede!")
    print(f"💥 O Firewall do servidor [{configuracao_servidor['nome_servidor']}] está DESLIGADO.")
    print("📊 Risco: Qualquer computador na internet pode tentar invadir o servidor sem barreiras.\n")
    infraestrutura_segura = False
else:
    print("🔒 Seguro: Firewall principal ativo e configurado.")

# 2. Teste de Exposição do Banco de Dados
if configuracao_servidor["porta_banco_dados"] == "publica":
    print("🚨 [ALERTA CRÍTICO] Vazamento de Dados Iminente!")
    print(f"💥 O acesso ao Banco de Dados está marcado como PÚBLICO.")
    print("📊 Risco: Hackers podem tentar roubar ou apagar todas as informações dos clientes diretamente.\n")
    infraestrutura_segura = False
else:
    print("🔒 Seguro: Porta do banco de dados protegida contra acessos externos.")

# Resultado Final da Auditoria
if infraestrutura_segura:
    print("✅ APROVADO: A configuração do servidor segue as regras de segurança da empresa. Pode publicar!")
else:
    print("❌ REPROVADO: O servidor possui erros graves que facilitam invasões. Correção obrigatória.")

print("\n--- AUDITORIA DE INFRAESTRUTURA CONCLUÍDA ---")

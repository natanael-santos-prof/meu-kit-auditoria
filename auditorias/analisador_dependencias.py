import time

# Banco de dados simulado de Segurança da Informação (Vulnerabilidades conhecidas no mercado)
# Ele lista quais versões de programas têm vírus conhecidos
banco_de_falhas_cve = {
    "django": {"versao_vulneravel": "3.2.0", "risco": "ALTO", "descricao": "Permite invasão de banco de dados remota."},
    "requests": {"versao_vulneravel": "2.20.0", "risco": "MÉDIO", "descricao": "Vazamento de dados em conexões inseguras."},
    "flask": {"versao_vulneravel": "1.1.0", "risco": "CRÍTICO", "descricao": "Execução de códigos maliciosos no servidor."}
}

# Lista real de programas e bibliotecas que os desenvolvedores da nossa empresa estão usando no projeto atual
componentes_do_projeto = [
    {"nome": "django", "versao": "4.2.0"},   # Versão nova e atualizada (Segura!)
    {"nome": "requests", "versao": "2.31.0"}, # Versão nova e atualizada (Segura!)
    {"nome": "flask", "versao": "1.1.0"}     # 🚨 ALERTA: Versão velha e vulnerável instalada!
]

print("--- INICIANDO ANÁLISE DE COMPOSIÇÃO DE SOFTWARE (DEVSECOPS) ---")
print("Verificando se o projeto utiliza códigos desatualizados ou perigosos...\n")
time.sleep(1.0)

projeto_seguro = True

# O robô auditor compara cada programa do projeto com o banco de dados de falhas conhecidas
for componente in componentes_do_projeto:
    nome_programa = componente["nome"]
    versao_programa = componente["versao"]
    
    # Verifica se esse programa específico possui algum registro de falha na história
    if nome_programa in banco_de_falhas_cve:
        detalhes_falha = banco_de_falhas_cve[nome_programa]
        
        # Se a versão usada for igual à versão marcada como vulnerável, acende o alerta vermelho!
        if versao_programa == detalhes_falha["versao_vulneravel"]:
            print(f"🚨 [ALERTA DE SEGURANÇA] Componente Perigoso Detectado: [{nome_programa}]")
            print(f"📊 Nível de Risco: {detalhes_falha['risco']}")
            print(f"⚠️ Versão em Uso: {versao_programa} (Esta versão está desatualizada!)")
            print(f"📝 Detalhes do Perigo: {detalhes_falha['descricao']}")
            print("🛑 Ação Obrigatória: Atualize este componente para a versão mais recente imediatamente.\n")
            projeto_seguro = False
        else:
            print(f"Pressione OK: Componente [{nome_programa}] está na versão {versao_programa} (Livre de falhas conhecidas).")

if projeto_seguro:
    print("🔒 Perfeito: Todas as dependências do projeto estão atualizadas e seguras para publicação!")
else:
    print("❌ REPROVADO: O código possui falhas de segurança conhecidas e NÃO pode ser publicado na internet.")

print("--- AUDITORIA DE COMPOSIÇÃO CONCLUÍDA ---")

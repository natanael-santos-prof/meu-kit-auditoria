# 📑 Gaveta 3: Meu Kit de Auditoria (Prevenção de Falhas e DevSecOps)

Este repositório é o meu "guarda-roupa" focado em **Prevenção e Auditoria de Códigos (DevSecOps)**. Aqui eu guardo robôs em **Python** que funcionam como fiscais de segurança. O objetivo deles é ler o trabalho dos programadores e achar erros graves **antes** que o site da empresa vá para a internet.

---

## 📂 Como este Guarda-Roupa está Organizado?

Para manter o padrão profissional, o projeto está dividido assim:
* 📁 **`auditorias/`**: A gaveta interna onde ficam os 3 robôs fiscais de código.
* 📑 **`README.md`**: Este manual de instruções explicativo (este arquivo).

---

## 🔍 O que meus Robôs Fiscais fazem? (Explicado de Forma Simples)

Como essas ferramentas rodam dentro do ambiente seguro da própria empresa antes do site nascer, elas **não precisam de nenhuma camuflagem**. O objetivo delas é o oposto: fazer barulho, acender alertas vermelhos e avisar a equipe de tecnologia sobre falhas humanas perigosas.

### 1. O Caçador de Senhas Esquecidas (`cacador_segredos.py`)
* **O que ele faz:** Os programadores às vezes esquecem senhas reais escritas no meio das linhas de código por pressa. Este robô funciona como um corretor ortográfico, mas em vez de caçar erros de português, ele caça palavras como "senha =", "password =" ou "token =". Se achar, ele bloqueia o projeto para a senha não vazar na internet.

### 2. O Fiscal de Componentes Velhos (`analisador_dependencias.py`)
* **O que ele faz:** Para criar um site rápido, os programadores usam "blocos de montar" prontos da internet (bibliotecas). Este robô lê a lista de blocos que a empresa usa e cruza com um banco de dados mundial de vírus. Se ele achar um bloco antigo e perigoso, ele avisa: *"Ei, esse componente está velho e tem um vírus conhecido, atualize agora!"*.

### 3. O Inspetor da Planta do Servidor (`validador_infraestrutura.py`)
* **O que ele faz:** Hoje em dia, a configuração dos servidores é feita por arquivos de texto. Este robô analisa esse arquivo para ver se o engenheiro não cometeu nenhuma bobeira, como esquecer o Firewall desligado ou deixar o banco de dados de clientes aberto para qualquer um acessar na internet. Ele garante que a "muralha" seja ligada corretamente.

---

## 🚀 Como testar essas ferramentas?

Esses robôs fiscais analisam textos de código locais através do terminal:
1. Baixe os arquivos da pasta `auditorias/`.
2. Abra o terminal do seu computador.
3. Execute o comando para rodar o fiscal desejado:
   ```bash
   cd auditorias
   python cacador_segredos.py
   python analisador_dependencias.py
   python validador_infraestrutura.py
   ```

---
*Projeto educativo focado em Segurança de Aplicações (AppSec), DevSecOps e Conformidade de Infraestrutura.*


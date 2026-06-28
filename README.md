# 📑 Gaveta 3: Meu Kit de Auditoria (Prevenção de Falhas e DevSecOps Avançado)

Este repositório é o meu "guarda-roupa" focado em **Prevenção e Auditoria de Códigos (DevSecOps)**. Aqui eu guardo robôs em **Python** que funcionam como fiscais automatizados de segurança para achar erros graves **antes** que os sistemas cheguem à internet.

---

## 📂 Estrutura do Repositório

O projeto está estruturado seguindo os padrões do mercado:

* 📁 **`auditórios/`**: A gaveta interna onde ficam guardados os scripts de auditoria em Python.
* 📁 **`laboratorio/`**: Contém o guia prático de como simular vulnerabilidades e validar as ferramentas.
* 📁 **`.github/workflows/`**: Pasta que armazena as configurações do robô de automação na nuvem (GitHub Actions).
* 📑 **`README.md`**: Este manual de instruções explicativo (este arquivo).

---

## 🔍 O que meus Robôs Fiscais fazem?

Estas ferramentas rodam de forma prévia em ambientes internos, focando na visibilidade total de falhas humanas de configuração.

### 1. O Caçador de Senhas com Varredura Profunda (`cacador_segredos.py`)
* **Mecanismo Cão Farejador:** Utiliza varredura recursiva (`os.walk`) para caminhar por dentro de **todas as subpastas** do projeto automaticamente, caçando senhas ou chaves (`api_key`) expostas por descuido.

### 2. O Fiscal de Componentes Obsoletos (`analisador_dependencias.py`)
Cruza as bibliotecas usadas pelos desenvolvedores com um banco de dados mundial de vírus (CVEs) para garantir que a empresa não use códigos velhos e perigosos.

### 3. O Inspetor de Infraestrutura como Código (`validador_infraestrutura.py`)
Analisa arquivos de configuração de servidores na nuvem, barrando erros graves como Firewalls desativados por engano.

---

## ⚙️ Esteira de Segurança Automatizada (CI/CD)

Graças ao **GitHub Actions**, criamos uma engrenagem que liga um computador virtual na nuvem de forma 100% automatizada toda vez que o projeto recebe uma atualização (`push`), executando o Caçador de Senhas e gerando relatórios em tempo real.

---

## 🚀 Como Testar no Laboratório

Para ver os robôs trabalhando e flagrando falhas ao vivo direto na nuvem do GitHub, siga o manual explicativo em:
📂 `laboratorio/como_testar_auditoria.txt`

---
*Projeto educativo focado em Segurança de Aplicações (AppSec), DevSecOps Avançado e Automação de Pipelines de Código.*

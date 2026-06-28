# 📑 Gaveta 3: Meu Kit de Auditoria (Prevenção de Falhas e DevSecOps Avançado)

Este repositório é o meu "guarda-roupa" focado em **Prevenção e Auditoria de Códigos (DevSecOps)**. Aqui eu guardo robôs em **Python** que funcionam como fiscais automatizados de segurança. O objetivo deles é analisar a estrutura do projeto e apontar erros graves **antes** que os sistemas cheguem à internet.

---

## 📂 Estrutura do Repositório

Para manter o padrão profissional, o projeto está estruturado de forma limpa:
* 📁 **`auditórios/`**: A gaveta interna onde ficam guardados os scripts de auditoria em Python.
* 📁 **`.github/workflows/`**: Pasta oculta que armazena os robôs de automação em nuvem do GitHub Actions.
* 📑 **`README.md`**: Este manual de instruções explicativo (este arquivo).

---

## 🔍 O que meus Robôs Fiscais fazem?

Como essas ferramentas rodam dentro do ambiente de desenvolvimento seguro e de forma prévia, elas não necessitam de camuflagem de rede. Seu foco total é a visibilidade e a precisão na caça de vulnerabilidades.

### 1. O Caçador de Senhas com Varredura Profunda (`cacador_segredos.py`)
* **Mecanismo Avançado (Cão Farejador):** Atualizado com a técnica de **Varredura Recursiva** (`os.walk`). O robô não analisa apenas a pasta atual, mas caminha de forma autônoma por dentro de **todas as subpastas e ramificações** do projeto, garantindo que nenhuma falha fique escondida.
* **O que ele faz:** Examina arquivos de texto e códigos atrás de credenciais expostas como `senha =`, `password =`, `api_key =` ou `token =`, emitindo alertas críticos com o local exato (arquivo e linha) da exposição.

### 2. O Fiscal de Componentes Obsoletos (`analisador_dependencias.py`)
* **O que ele faz:** Inspeciona as bibliotecas de terceiros ("blocos de montar") utilizadas no software e as cruza com uma base de dados de vulnerabilidades conhecidas (CVEs), reprovando a publicação se houver componentes desatualizados ou com vírus catalogados.

### 3. O Inspetor de Infraestrutura como Código (`validador_infraestrutura.py`)
* **O que ele faz:** Analisa arquivos de configuração de servidores em nuvem, garantindo a conformidade e barrando erros humanos graves, como Firewalls desativados ou bancos de dados configurados como públicos por engano.

---

## ⚙️ Esteira de Segurança Automatizada (CI/CD)

A grande engrenagem deste repositório é o arquivo `.github/workflows/inspecao_seguranca.yml`. Ele ativa o **GitHub Actions**, criando um robô invisível na nuvem que:
1. Dispara de forma 100% automatizada a cada atualização (`push`) enviada ao repositório.
2. Inicializa uma máquina virtual isolada, instala o ambiente Python e executa a varredura do nosso **Caçador de Senhas**.
3. Gera relatórios de segurança em tempo real e bloqueia ou aprova o projeto diretamente na nuvem.

---
*Projeto educativo focado em Segurança de Aplicações (AppSec), DevSecOps Avançado e Automação de Pipelines de Código.*


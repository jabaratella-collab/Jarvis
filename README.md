# J.A.R.V.I.S. - Assistente Virtual Local (Linux)

Local AI Virtual Assistant on Linux | Assistente Virtual Local com IA no Linux.

Este projeto é um script em **Python** desenvolvido para atuar como um assistente de monitoramento e automação de sistema rodando 100% localmente no terminal do Ubuntu. Ele utiliza a ferramenta **Ollama** para processamento de linguagem natural offline, garantindo privacidade total dos dados e da infraestrutura.

## Funcionalidades
* **Interação via Terminal:** Chat contínuo com a IA diretamente pela linha de comando do Linux.
* **Monitoramento do Sistema:** Executa comandos nativos do sistema operacional (como `uptime` e `free -h`) de forma automatizada através da biblioteca `subprocess`.
* **Geração de Relatórios Inteligentes:** A IA lê os dados brutos do hardware (Memória RAM, tempo de atividade) e os traduz em um relatório natural e compreensível em português.
* **Memória de Contexto:** Mantém o histórico das últimas interações armazenado em cache temporário para garantir fluidez na conversa.

## Tecnologias Utilizadas
* **Python 3**
* **Ollama** (Modelos LLM locais)
* **Linux (Ubuntu)** / Linha de Comando (CLI)
* Bibliotecas nativas: `subprocess` e `readline`

## Como o código funciona na prática?
O script entra em um loop de interação onde aguarda os comandos do usuário. Caso a palavra "relatório" seja detectada, o Python dispara rotinas no sistema operacional (`subprocess.run`), coleta as saídas de saúde da máquina e as injeta no prompt da IA. O LLM então atua não apenas como um chatbot, mas como um interpretador de dados do sistema, devolvendo um diagnóstico claro ao usuário.

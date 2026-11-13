import ollama
import readline
import subprocess

print("=== Sistemas Online. Conexão com J.A.R.V.I.S. estabelecida ===")
print("(Digite 'sair' a qualquer momento para encerrar os sistemas)\n")

historico_mensagens = []
LIMITE_MENSAGENS = 10

while True:
    texto_usuario = input("Senhor: ")

    if texto_usuario.strip().lower() == 'sair':
        print("J.A.R.V.I.S.: Entrando em modo de espera. Até logo, Senhor.")
        break

    if "relatorio" in texto_usuario.lower():
        print("[Coletando dados da placa-mãe e do sistema operacional...]")
        resultado_uptime = subprocess.run(['uptime', '-p'], capture_output=True, text=True)
        resultado_ram = subprocess.run(['free', '-h'], capture_output=True, text=True)
        texto_usuario = f"""
                O usuário pediu um relatório do sistema. Aqui estão os dados crus do Ubuntu agora:
                - Tempo que a máquina está ligada: {resultado_uptime.stdout.strip()}
                - Tabela de Memória RAM: \n{resultado_ram.stdout.strip()}

                Aja estritamente como J.A.R.V.I.S. e faça um relatório verbal formal para mim (o Senhor) baseado nestes dados. 
                Analise a saúde do sistema, mas ATENÇÃO: É uma ordem absoluta que você traduza tudo e gere a sua resposta ÚNICA E EXCLUSIVAMENTE em Português do Brasil (PT-BR).
                """


    historico_mensagens.append({
        'role': 'user',
        'content': texto_usuario
    })

    while len(historico_mensagens) > LIMITE_MENSAGENS:
        historico_mensagens.pop(0)

    print("J.A.R.V.I.S.: ", end="", flush=True)

    resposta_stream = ollama.chat(
        model='Jarvis',
        messages=historico_mensagens,
        stream=True
    )

    texto_completo_jarvis = ""

    for pedaco in resposta_stream:
        conteudo = pedaco['message']['content']
        print(conteudo, end='', flush=True)
        texto_completo_jarvis += conteudo

    print("\n")

    historico_mensagens.append({
        'role': 'assistant',
        'content': texto_completo_jarvis
    })
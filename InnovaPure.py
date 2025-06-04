import re
from fuzzywuzzy import process

banco_dados = {
    "Bom dia, Boa Tarde, Boa Noite": "Olá! Como posso ajudar você hoje??",
    "oi, olá": "Olá, tudo bem?",
    "Qual o seu nome? como você se chama? é você? você": "InnovaPure! O chatbot de atendimento da Innova-T.O.",
    "Quem é O CEO da Innova?, fundador da innova, fundou a innova": "O Fundador e CEO da Innova é Lucas Jaeger!",
    "seu Criador? quem é seu criador? criador, criado, Quem te criou?": "Meu criador se chama Alexandre França!",
    "atendido, atendimento, atender, Quero marcar um horário": "Para marcar um horário, basta digitar seu número!"
}

def marcar_horario(input_do_usuario):
    padrao_de_telefone = r'\d{2}\d{5}\d{4}'
    if re.search(padrao_de_telefone,input_do_usuario):
        return "Horário marcado na Quarta feira ás 16 horas da tarde!"
    return None

def responder(input_do_usuario):
    marcar = marcar_horario(input_do_usuario)
    if marcar:
        return marcar
    
    melhor_resposta = process.extractOne(input_do_usuario,banco_dados.keys())
    if melhor_resposta[1] > 50:
        return banco_dados[melhor_resposta[0]]
    else:
        return "Desculpe, não entendi sua pergunta. Poderia repetir?"

while True:
    entrada = input('Usuário: ') 
    resposta = responder(entrada)
    
    if entrada == 'SAIR':
        break
    
    print(f'InnovaPure: {resposta}')
    
       
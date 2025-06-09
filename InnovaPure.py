import re
from fuzzywuzzy import process
import json

dados =  {
  "Bom dia, Boa Tarde, Boa Noite": "Olá! Como posso ajudar você hoje??",
  "oi, olá": "Olá, tudo bem?",
  "Qual o seu nome? como você se chama? é você? você, quem é vc? quem é você?": "InnovaPure! O chatbot de atendimento da Innova-T.O.",
  "é você? você, quem é vc? quem é você?": "InnovaPure! O chatbot de atendimento da Innova-T.O.",
  "Quem é O CEO da Innova?, fundador da innova, fundou a innova": "O Fundador e CEO da Innova é Lucas Jaeger!",
  "seu Criador? quem é seu criador? criador, criado, Quem te criou?": "Meu criador se chama Alexandre França!",
  "atendido, atendimento, atender, Quero marcar um horário": "Para marcar um horário, basta digitar seu número!",
  "Quantas pessoas trabalham na innova? pessoas, funcionários, quantos funcionários a innova tem?": "A Innova contém uma equipe de mais de 20 profissionais Altamente Qualificados!",
  "Oque é a Innova? com oque a innova trabalha? oque a empresa faz?, oque a innova faz?": "Transformamos ideias em Realidade Digital! Temos Soluções em software que vão Potencializar o seu negócio!",
  "oque a innova faz? oque é a innova T.O.? Quem é a innova? innova tech one": "Transformamos ideias em Realidade Digital! Temos Soluções em software que vão Potencializar o seu negócio!",
  "Qual é o instagram da innova?insta, Qual é o insta de vcs? ,Vocês possuem alguma rede social? meio de contato, perfil, instagram": "Acesse nosso perfil no Instagram: @innovatech.one e entre em contato Conosco!",
  "Obrigado, agradeço, valeu, tmj": "Que bom que eu pude te ajudar :D"
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
    
    melhor_resposta = process.extractOne(input_do_usuario,dados.keys())
    if melhor_resposta[-1] > 80:
        return dados[melhor_resposta[0]]
    else:
        return "Desculpe, não entendi sua pergunta. Poderia repetir?"

while True:
    entrada = input('Usuário: ') 
    resposta = responder(entrada)
    
    if entrada == 'SAIR':
        break
    
    print(f'InnovaPure: {resposta}')
    
       
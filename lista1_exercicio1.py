## WS PRIME - LISTA DE EXERCÍCIOS ##

# EXERCÍCIO 01 #

nome = input("Digite seu nome: ")
endereço = input("Digite seu endereço: ")
telefone = input("Digite seu telefone, com DDD: ")
e_mail = input("Digite seu e-mail: " )

print (f' Cadastro realizado com sucesso! Seu nome é: {nome} ')
print (f' Cadastro realizado com sucesso! Seu endereço é: {endereço} ')
print (f' Cadastro realizado com sucesso! Seu telefone é: {telefone} ')
print (f' Cadastro realizado com sucesso! Seu e-mail é: {e_mail} ')


#dúvida:
# É possível colocar todas os prints em um único print? A ideia seria o programa imprimir um único texto com o resumo das informações cadastradas pelo usuários
# pensei em algo assim: 
# print (f' Cadastro realizado com sucesso! Os dados cadastrados são: Nome: {nome}, Endereço {endereço}, Telefone{telefone}, e-mail{e-mail}')
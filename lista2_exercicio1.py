## WS PRIME - ESCOLA DE PROGRAMADORES

## LISTA 02 - EXERCÍCIO 01


name = input('Write your name: ')
address = input('Write you anddres: ')
phone = input('Write you phone: ')
e_mail = input('Write your e-mail: ')



cadastro = {"name":"Daniel", "address":"Avenida", "phone": "68_999999", "e_mail": "almeidapapa@embrapa.br"}

print(cadastro)

## dúvida: como criar um vetor que contenha os nomes inputados?

## solução desenvolvida com ajuda de consulta na internet

#criar dicionário vazio
dados = {}
print(type(dados))

# preencher dicionario com as informações "casadas".
dados["name"] = input('Write your name: ')
dados["address"] = input('Write you anddres: ')
dados["phone"] = input('Write you phone: ')
dados["e_mail"] = input('Write your e-mail: ')

#imprimir

print(f'  Thank you for your login:{dados}')

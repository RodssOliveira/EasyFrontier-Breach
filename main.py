#easyfrontier@fiap.com.br

import requests
import github
import search_engine as search

#email = str(input('Insira o email que você deseja verificar: '))
email = 'easyfrontier@fiap.com.br'

print('Iniciando verificacao para o email: ', email)
print('-===========================-')

print('Verificando email no GitHub')
print('-===========================-')
result = github.crawler(email)

if int(result) >= 1:
    print('| Foi encontrado o seu email em um repositório no GitHub {} vezes |\n'.format(result))
else:
    print('| Seu email não foi encontrado no GitHub |\n')


print('-===========================-')
print('Verificando email no Pastebin')
print('-===========================-')
result, site_list = search.pastebin(email)

if int(result) >= 1:
    print('| Foi encontrado o seu email em uma pasta no Pastebin {} vezes |\n'.format(result))
    print('| Sites encontrados')
    for s in site_list:
        print('| ', s)
else:
    print('| Seu email não foi encontrado no Pastebin |\n')



print('-===========================-')
print('Verificando email no Google')
print('-===========================-')
result, site_list = search.google(email)

if int(result) >= 1:
    print('| Foi encontrado o seu email no Google {} vezes |\n'.format(result))
    print('| Sites encontrados')
    for s in site_list:
        print('| ', s)
else:
    print('| Seu email não foi encontrado no Google |\n')

print('            -===========================-')
print('-======================================================-')
print('              | Processo finalizado |')
print('-======================================================-')
print('            -===========================-')









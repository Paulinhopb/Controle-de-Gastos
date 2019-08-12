

dia = int(input('Digite o Dia de Hoje: '))
mes = int(input('Digite o mês de Hoje: '))
ano = int(input('Digite o ano de Hoje: '))
data = ('{}/{}/{}'.format(dia,mes,ano))

print(data)

gasto = float(input('Qual foi o gasto de hoje ? : '))

if gasto == 0:
    r = str(input('Peberci que não houve Gasto algum. \nDeseja Refazer a etapa anterior ? (S) (N)\n'))
    r= r.upper()
    while r ==('S'):

        gasto = float(input('Qual foi o gasto de hoje ? : '))
        r = str(input('Deseja Refazer a etapa anterior ? (S) (N)'))
        r = r.upper()


elif gasto > 0 :
    r2 = str(input('Gasto Computado ! deseja Alterar seu Gasto ? : (S) (N)'))
    r2 = r2.upper()
    while r2 ==('S'):

        gasto = float(input('Insira o seu Gasto : '))
        r2 = str(input('Gasto Computado ! deseja Alterar seu Gasto ? : (S) (N)'))
        r2 = r2.upper()


print('=' * 250)
print('Dados Gravados ... Seu Gasto foi de : R${} ,Obrigado(a)'.format(gasto))
print('=' * 250)

print('Fim ...')
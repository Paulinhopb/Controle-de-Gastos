from tkinter import *





def pay ():

    gasto = float(input('Qual foi o gasto de hoje ? : '))

    if gasto == 0:
        r = str(input('Peberci que não houve Gasto algum. \nDeseja Refazer a etapa anterior ? (S) (N)\n'))
        r = r.upper()
        while r == ('S'):
            gasto = float(input('Qual foi o gasto de hoje ? : '))
            r = str(input('Deseja Refazer a etapa anterior ? (S) (N)'))
            r = r.upper()


    elif gasto > 0:
        r2 = str(input('Gasto Computado ! deseja Alterar seu Gasto ? : (S) (N)'))
        r2 = r2.upper()
        while r2 == ('S'):
            gasto = float(input('Insira o seu Gasto : '))
            r2 = str(input('Gasto Computado ! deseja Alterar seu Gasto ? : (S) (N)'))
            r2 = r2.upper()

    print('=' * 250)
    print('Dados Gravados ... Seu Gasto foi de : R${} ,Obrigado(a)'.format(gasto))
    print('=' * 250)

    print('Fim ...')







window = Tk()
window.title('Controle de Gastos')
window.geometry('750x750')

txt1 = Label(text='Gastos de Hoje !!', fg= 'red')
txt1.place(x= 50, y= 70)
button1 = Button(text='Insirir Gastos', command = lambda: pay(), bg= 'red', fg= 'white')
button1.place(x= 55, y= 100)

txt2 = Label(text='Renda Mensal !!', fg= 'gray')
txt2.place(x= 200, y= 70)
button2 = Button(text='Vizualizar', command = lambda: command(2) , bg= 'gray', fg= 'white')
button2.place(x= 210, y= 100)

txt3 = Label(text='Renda Anual !!', fg= 'black')
txt3.place(x= 370, y= 70)
button3 = Button(text='Vizualizar', command = lambda: command(3) , bg= 'black', fg= 'white')
button3.place(x= 375, y= 100)
window.mainloop()
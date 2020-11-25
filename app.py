from datetime import *
from tkinter import *

def calcular():
    hj = date.today()
    numero = qtde.get()
    futuro = date.fromordinal(hj.toordinal()+int(numero))
    dataf = f'A data futura é: {futuro.strftime("%d/%m/%y")}'
    resultado["text"] = dataf


if __name__ == '__main__':

    janela = Tk()
    janela.title("CALCULAR DIAS")
    janela.geometry("300x300+800+300")

    titulo = Label(janela,
                   text="Contador Dias Futuros", font=("Courier", 12, "bold"))
    bt = Button(janela,
                text="Calcular",
                command=calcular,
                width=15)
    qtde = Spinbox(janela,
                   from_=1,
                   to=100,
                   width=15)
    resultado = Label(janela,
                      text="0",
                      fg="dark green",
                      font=("Courier", 12, "bold"))

    titulo.pack(pady=20)
    qtde.pack(pady=20)
    bt.pack(pady=20)
    resultado.pack(pady=20)

    janela.mainloop()
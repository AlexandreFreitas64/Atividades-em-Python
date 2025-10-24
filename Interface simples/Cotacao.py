import requests
from tkinter import *

def pegar_cotacoes():
    requisicao = requests.get("http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_Dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''

    Dólar: {cotacao_Dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    texto_cotacoes["text"] = texto


janela = Tk()

janela.title("Cotação atual das Moedas")

janela.geometry("400x300")
texto_janela = Label(janela, text = "Clique no Botão para ver as cotações de moeda:")
texto_janela.grid(column= 0, row= 0, padx=60, pady=30)

botao = Button(janela, text="Buscar cotações de Dolar/Euro/BTC", command= pegar_cotacoes)
botao.grid(column=0, row=1)
# texto2 = Label(janela, text= "Clique aqui agora")
# texto2.grid(column=0, row= 1)

texto_cotacoes = Label(janela, text="")
texto_cotacoes.grid(column=0, row=2, pady=30)


janela.mainloop() #vai manter a janela ativa
import pyautogui
import time
import pandas

#Acessar site destino

pyautogui.PAUSE = 1

#abrir o navegador
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

#entrar no site
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'

pyautogui.write(link)
pyautogui.press('enter')

#esperar o carregamento do site
time.sleep(3)

#fazer login
pyautogui.click(x=987, y=364)
pyautogui.write('srsilveirapf@gmail.com')

pyautogui.press('tab')
pyautogui.write('123456')

pyautogui.press('tab')
pyautogui.press('enter')

time.sleep(3)

#importando base de dados

tabela = pandas.read_csv("produtos.csv")

for linha in tabela.index:
    pyautogui.click(x=738, y=251)

    #preenchendo formulario
    codigo = tabela.loc[linha, "codigo"]
    marca = tabela.loc[linha, "marca"]
    tipo = tabela.loc[linha, "tipo"]
    categoria = tabela.loc[linha, "categoria"]
    preco = tabela.loc[linha, "preco_unitario"]
    custo = tabela.loc[linha, "custo"]
    obs = tabela.loc[linha, "obs"]

    pyautogui.write(str(codigo))
    pyautogui.press('tab')


    pyautogui.write(str(marca))
    pyautogui.press('tab')

    pyautogui.write(str(tipo))
    pyautogui.press('tab')

    pyautogui.write(str(categoria))
    pyautogui.press('tab')

    pyautogui.write(str(preco))
    pyautogui.press('tab')

    pyautogui.write(str(custo))
    pyautogui.press('tab')

    if not pandas.isna(obs):
        pyautogui.write(str(obs))

    #salvar registro
    pyautogui.press('tab')
    pyautogui.press('enter')

    pyautogui.scroll(50000)
import pyautogui
import time

# Abrir o Chrome
pyautogui.PAUSE = 0.9
pyautogui.press('win')
pyautogui.write('chrome')

pyautogui.press('enter')

# Entrar no link
link = 'https://hashtagtreinamentos.com/python/intensivao/login'
pyautogui.write(link)
pyautogui.press('enter')

# Esperar o site carregar
time.sleep(10)

# Fazer login
pyautogui.click(x=617, y=366)
pyautogui.write('ltslarissa@hotmail.com')

# Colocar senha
pyautogui.click(x=612, y=472)
pyautogui.write('Larissa')

# Dar enter
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(2)

# importar base de dados
import pandas

tabela = pandas.read_csv(r'C:\Users\338\PycharmProjects\CursoFiap\venv\produtos.csv.py')
print(tabela)

for linha in tabela.index:
    # Preencher informações do produto
    pyautogui.click(x=668, y=252)

    # localizar o produto na tabela
    codigo = tabela.loc(linha, 'codigo')
    marca = tabela.loc(linha, 'marca')
    tipo = tabela.loc(linha, 'tipo')
    categoria = tabela.loc(linha, 'categoria')
    preco_unitario = tabela.loc(linha, ' preco_unitario')
    custo = tabela.loc(linha, 'custo')

    pyautogui.write(str(tabela.loc[linha, 'codigo']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'marca']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'tipo']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')

    obs = tabela.loc[linha, 'obs']
    if not pandas.isna(obs):
        pyautogui.write(str('obs'))

    # apertar para enviar

    pyautogui.press('tab')
    pyautogui.press('enter')

    pyautogui.scroll(10000)
    
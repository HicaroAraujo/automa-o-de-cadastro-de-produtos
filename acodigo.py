import pyautogui
pyautogui.PAUSE = 1
import time 



# entrar no edga
# pesquisar no navegador
# enserir email 
# enserir senha 
# entrar no sistema
pyautogui.press("win") # apertar no windons

pyautogui.press("tab")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
pyautogui.press("tab")
pyautogui.write("hicaro.camisa10@gmail.com")
pyautogui.press("tab")
pyautogui.write("camisa10")
pyautogui.press("tab")
pyautogui.press("enter")

# importar base de dados
import pandas as pd 

tabela = pd.read_csv ("produtos.csv")

# cadastrar produtos  




for linha in tabela.index: # repetirMouse       
    codigo = tabela.loc[linha, "codigo"]

    pyautogui.click(x=756, y=238)
    pyautogui.write(codigo)

    pyautogui.press("tab")
    pyautogui.write(tabela.loc[linha, "marca"])

    pyautogui.press("tab")
    pyautogui.write(tabela.loc[linha, "tipo"])

    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))

    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))

    pyautogui.press("tab")
    
    obs =str(tabela.loc[linha, "obs"])
    if obs != "n19.95 5.0   an":
      pyautogui.write(obs)
    
    pyautogui.press("tab") 
    # para apertar o botão
    pyautogui.press("enter")

    pyautogui.scroll(300)   
        
      







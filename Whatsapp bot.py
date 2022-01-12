# %%
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import pandas as pd
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://web.whatsapp.com/')

# ## Scanear o QR Code do whatsapp a ser automatizado

agenda = pd.read_csv("arquivo_aux.csv", sep = ";")
agenda.head() #verificando se o arquivo esta correto

# ### Testes para ver se localiza a mensagem correta

agenda.loc[agenda["Contato"]=="Hugo","Mensagem 1"]
agenda["Mensagem 2"] #Coluna das segundas mensagens

# ### Selecionando os campos de pesquisa do Whatsapp e armazenando para uso no looping em seguida

for contato in agenda["Contato"].values:
    barra_pesquisa = driver.find_element_by_css_selector("#side > div.uwk68 > div > label > div > div._13NKt.copyable-text.selectable-text")
    barra_pesquisa.send_keys(contato)
    barra_pesquisa.send_keys(Keys.ENTER)
    barra_chat = driver.find_element_by_css_selector("#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
    barra_chat.send_keys(agenda.loc[agenda["Contato"]==contato,"Mensagem 1"])
    barra_chat.send_keys(Keys.ENTER)
    if len(agenda.loc[agenda["Contato"]==contato,"Mensagem 2"]) != 0:
        barra_chat.send_keys(agenda.loc[agenda["Contato"]==contato,"Mensagem 2"])
        barra_chat.send_keys(Keys.ENTER)

print("Mensagens enviadas")



#!/usr/bin/env python
# coding: utf-8

# In[ ]:


### Automação página Blog do Agi

    # Abrir o navegadorn
    # Acessar a página \"https://blogdoagi.com.br/"
    # Clicar a lupa no canto superior esquerdo
    # Digitar no campo de pesquisa o que procura
    # Clicar no botão Pesquisar


# In[2]:


# Abrir o navegador
# Acessar a página \"https://blogdoagi.com.br/"
    
from selenium import webdriver
from selenium.webdriver.common.by import By
    
chrome_options = webdriver.ChromeOptions()
    
navegador = webdriver.Chrome()
navegador.maximize_window()
navegador.get("https://blogdoagi.com.br/")


# In[3]:


# Clicar a lupa no canto superior esquerdo
navegador.find_element('xpath','//*[@id=\"search-open\"]').click()


# In[4]:


# Digitar no campo de pesquisa o que procura
navegador.find_element('xpath','//*[@id=\"masthead\"]/div[1]/div[2]/form/label/input').send_keys("Saldo Agibank")


# In[5]:


# Clicar no botão Pesquisar\n",
navegador.find_element('xpath','//*[@id=\"masthead\"]/div[1]/div[2]/form/input').click()


# In[ ]:





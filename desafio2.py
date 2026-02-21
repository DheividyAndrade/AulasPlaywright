''' 
DESAFIOS 🎖️
Preencha de forma humanizada os campos a seguir no site https://playground-devaprender.netlify.app
- Nome completo
- Email
- Senha

'''
# Configurações recomendadas para usar em suas automações.

from playwright.sync_api import sync_playwright
import random

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,downloads_path=r'C:\Users\deivi\Downloads') # headless -> navegador não é exibido. downloads_path -> pasta onde os arquivos baixados serão armazenados
    context = browser.new_context(
        viewport={"width": 1360, "height": 768},
        accept_downloads=True, #PERMITIR DOWNLOADS AUTOMATICOS
        locale="pt-BR", #locale (ex.: pt-BR, en-US) para definir o idioma do navegador
    )
    page = context.new_page()
    page.set_default_timeout(30000) # 30s para ações/waits
    page.set_default_navigation_timeout(60000) # 60s para navegações
    
    page.goto('https://playground-devaprender.netlify.app',wait_until='domcontentloaded')

    
    # clicar no nome completo
    campo_nome_completo = page.get_by_role("textbox", name="Nome Completo")
    campo_nome_completo.click()
    campo_nome_completo.type("Dheividy Dhanrley", delay=300) # delay -> tempo de espera entre cada caractere para simular uma digitação mais humanizada
    page.wait_for_timeout(2 * 1000) # tempo de espera para simular uma digitação mais humanizada
    # page.wait_for_timeout(random.randint(1, 3) * 1000) # tempo de espera aleatório entre 1 e 3 segundos para simular uma digitação mais humanizada

    # clicar no email
    campo_email = page.get_by_role("textbox", name="Email")
    campo_email.click()
    campo_email.type("deividyandrade@hotmail.com", delay=300) # delay -> tempo de espera entre cada caractere para simular uma digitação mais humanizada
    page.wait_for_timeout(2 * 1000) # tempo de espera para simular uma digitação mais humanizada

    # clicar no campo senha
    campo_senha = page.get_by_role("textbox", name="Senha")
    campo_senha.click()
    campo_senha.type("12345678", delay=300) # delay -> tempo de espera entre cada caractere para simular uma digitação mais humanizada
    
    input('Digite ENTER para encerrar a automação')
    browser.close()
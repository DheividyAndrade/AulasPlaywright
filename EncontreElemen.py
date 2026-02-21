# ENCONTRANDO QUALQUER ELEMENTO EM UM SITE COM PLAYWRIGHT / playwright codegen --target python https://www.nome-do-site.com -> para achar path

from playwright.sync_api import sync_playwright

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
    
    page.goto('https://playground-devaprender.netlify.app/',wait_until='domcontentloaded')
    
    input('Digite ENTER para encerrar a automação')
    # COMO ENCONTRAR ELEMENTOS NA TELA
    # playwright codegen --target python https://playground-devaprender.netlify.app/ -> utilize cmd e cole esse codigo.

    page.get_by_role("textbox", name="Nome Completo") # usado 80% das vezes
    page.get_by_text("Vamos Automatizar TUDO!") # muito usado (para extrair textos)
    page.get_by_placeholder('Digite seu nome completo') # pouco usado 
    page.get_by_label("País").select_option("br") # usado principalmente para selecionar opções em dropdowns
    page.locator() # seletores CSS, XPath, etc... (pouco usado, mas necessário para casos mais complexos)

    browser.close()
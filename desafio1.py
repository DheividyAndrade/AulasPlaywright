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
    
    page.goto('https://xopify.netlify.app/',wait_until='domcontentloaded')
    
    # Entrar no site e clicar no produto "Fones de Ouvido Quantum Noise-Cancelling"
    page.get_by_role("heading", name="Fones de Ouvido Quantum Noise").click()

    input('Digite ENTER para encerrar a automação')
    browser.close()
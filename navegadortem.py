# Abrir um navegador temporario

from playwright.sync_api import sync_playwright

# Abrir um navegador temporario
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False) # headless -> navegador não é exibido.
    context = browser.new_context(
        viewport={"width": 1360, "height": 768},
        accept_downloads=True,
        locale="pt-BR",
    ) # Cria um novo (perfil temporario) para paginas, com configurações independentes, cookies e permissões


    page = context.new_page() # abre uma nova pagina (aba) no navegador
    page.goto('https://playground-devaprender.netlify.app/',wait_until='domcontentloaded')
    input('Digite ENTER para encerrar a automação')
    browser.close()




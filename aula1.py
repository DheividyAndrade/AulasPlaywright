'''from playwright.sync_api import sync_playwright

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
'''

# Abrir um navegador persistente MELHOR OPÇÃO!!
from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch_persistent_context(
        user_data_dir=r'./automacao_whatsapp', # pasta onde os dados do navegador serão armazenados
        headless=False,
        viewport={"width": 1360, "height": 768},
        accept_downloads=True, # permite downloads automaticos
        downloads_path=r'./downloads', # pasta onde os arquivos baixados serão armazenados
        locale="pt-BR", # define o idioma do navegador para português do Brasil
        record_video_dir=r'./videos', # define a pasta onde os videos gravados serão armazenados
        record_video_size={"width": 1360, "height": 768}, # define o tamanho do video gravado
        color_scheme="dark", # define o tema do navegador para escuro/ se quiser claro use "light"

    ) # Cria um novo (perfil persistente) para paginas, com configurações independentes, cookies e permissões    

    page = browser.new_page() # abre uma nova pagina (aba) no navegador
    page.goto("https://web.whatsapp.com/",wait_until='domcontentloaded') # Acessa o site do whatsapp web
    input('Digite ENTER para encerrar a automação')
    browser.close()

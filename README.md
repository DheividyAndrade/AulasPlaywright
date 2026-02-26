# 🎭 Aulas Playwright com Python

Repositório de estudos e exemplos práticos de **automação de navegadores** utilizando a biblioteca [Playwright](https://playwright.dev/python/) com Python.

---

## 📚 Sobre este repositório

Este repositório reúne os exemplos e scripts desenvolvidos durante as aulas de automação com Playwright. O conteúdo abrange desde a abertura básica de um navegador até configurações avançadas de contextos persistentes e temporários, além de automação do WhatsApp Web.

---

## 🛠️ Pré-requisitos

Antes de executar qualquer script, certifique-se de ter instalado:

- [Python 3.8+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/)
- Biblioteca Playwright para Python

### Instalação

```bash
# Instalar o Playwright
pip install playwright

# Instalar os navegadores necessários
playwright install
```

---

## 📁 Estrutura do Projeto

```
AulasPlaywright/
│
├── EncontreElemen.py        # (em breve) Exemplos de como localizar elementos na página
├── navegadorper.py          # Abrindo um navegador com perfil PERSISTENTE
├── navegadorrec.py          # Configurações RECOMENDADAS para automações
├── navegadortem.py          # Abrindo um navegador TEMPORÁRIO
└── automacao_whatsapp/      # Pasta de dados do perfil persistente do WhatsApp Web
```

---

## 📄 Descrição dos Arquivos

### 🔒 `navegadorper.py` — Navegador com Perfil Persistente

Demonstra como abrir um navegador utilizando um **contexto persistente** (`launch_persistent_context`). Nesse modo, cookies, sessões e dados de login são salvos em uma pasta local, permitindo que você reutilize a sessão entre execuções (ideal para automações que exigem login, como o WhatsApp Web).

**Principais configurações utilizadas:**

| Parâmetro | Descrição |
|---|---|
| `user_data_dir` | Pasta onde os dados do navegador são armazenados (`./automacao_whatsapp`) |
| `headless=False` | Exibe o navegador na tela |
| `viewport` | Define a resolução da janela (1360×768) |
| `accept_downloads=True` | Permite downloads automáticos |
| `downloads_path` | Pasta de destino dos arquivos baixados |
| `locale="pt-BR"` | Define o idioma do navegador para Português do Brasil |
| `record_video_dir` | Pasta onde os vídeos das sessões serão gravados |
| `record_video_size` | Tamanho do vídeo gravado (1360×768) |
| `color_scheme="dark"` | Define o tema escuro (use `"light"` para tema claro) |

**Caso de uso:** Automação do WhatsApp Web — o script acessa `https://web.whatsapp.com/` e aguarda o usuário pressionar ENTER para encerrar.

---

### ⚙️ `navegadorrec.py` — Configurações Recomendadas

Apresenta um **template de boas práticas** para iniciar automações com o Playwright. Utiliza contexto não-persistente (`browser.new_context()`), separando claramente as responsabilidades de browser, contexto e página.

**Principais configurações utilizadas:**

| Parâmetro | Descrição |
|---|---|
| `headless=False` | Exibe o navegador na tela |
| `downloads_path` | Pasta de destino dos arquivos baixados |
| `viewport` | Define a resolução da janela (1360×768) |
| `accept_downloads=True` | Permite downloads automáticos |
| `locale="pt-BR"` | Define o idioma do navegador |
| `set_default_timeout(30000)` | Timeout padrão de 30 segundos para ações/waits |
| `set_default_navigation_timeout(60000)` | Timeout de 60 segundos para navegações |

**Site utilizado:** [Playground DevAprender](https://playground-devaprender.netlify.app/) — ambiente de prática para automação.

---

### 🕐 `navegadortem.py` — Navegador Temporário

Demonstra como abrir um navegador com **contexto temporário** (`browser.new_context()`). Nesse modo, todos os dados (cookies, sessões, cache) são descartados ao fechar o navegador, garantindo um ambiente limpo a cada execução.

**Principais configurações utilizadas:**

| Parâmetro | Descrição |
|---|---|
| `headless=False` | Exibe o navegador na tela |
| `viewport` | Define a resolução da janela (1360×768) |
| `accept_downloads=True` | Permite downloads automáticos |
| `locale="pt-BR"` | Define o idioma do navegador |

**Site utilizado:** [Playground DevAprender](https://playground-devaprender.netlify.app/)

---

### 🔍 `EncontreElemen.py` — Encontrando Elementos (em breve)

Arquivo reservado para os exemplos sobre **localização e interação com elementos** da página, como cliques, preenchimento de formulários, seletores CSS, XPath e muito mais.

---

## 🧠 Conceitos Abordados

- **`sync_playwright`**: API síncrona do Playwright para Python
- **Contexto Persistente**: mantém dados de sessão entre execuções
- **Contexto Temporário**: descarta todos os dados ao encerrar
- **Configurações de navegador**: viewport, locale, downloads, gravação de vídeo, color scheme
- **Timeouts**: configuração de timeouts para ações e navegações
- **Automação do WhatsApp Web**: utilizando perfil persistente para manter a sessão ativa

---

## 🔄 Diferença entre Perfil Persistente e Temporário

| Característica | Perfil Persistente (`navegadorper.py`) | Perfil Temporário (`navegadortem.py`) |
|---|---|---|
| Salva cookies/sessões | ✅ Sim | ❌ Não |
| Ideal para login único | ✅ Sim | ❌ Não |
| Ambiente limpo a cada execução | ❌ Não | ✅ Sim |
| Uso de `user_data_dir` | ✅ Necessário | ❌ Não necessário |
| Caso de uso típico | WhatsApp Web, redes sociais | Testes isolados, web scraping |

---

## ▶️ Como Executar

```bash
# Navegador com perfil persistente (WhatsApp Web)
python navegadorper.py

# Configurações recomendadas
python navegadorrec.py

# Navegador temporário
python navegadortem.py
```

> **Dica:** Pressione `ENTER` no terminal para encerrar a automação em qualquer um dos scripts.

---

## 🔗 Links Úteis

- [Documentação oficial do Playwright para Python](https://playwright.dev/python/docs/intro)
- [Playground DevAprender](https://playground-devaprender.netlify.app/)
- [WhatsApp Web](https://web.whatsapp.com/)

---

## 👩‍💻 Autora

Desenvolvido por **Dheividy Andrade** como material de estudo das aulas de automação com Playwright.

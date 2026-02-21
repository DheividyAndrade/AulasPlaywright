# Diretrizes de Boas Práticas do Playwright

## Estratégia de Localizadores

- **Prefira usar métodos `get_by_`**: Sempre que possível, use os métodos `get_by_*` do Playwright (como `get_by_role`, `get_by_label`, `get_by_placeholder`, etc.), pois são mais semânticos e mais resistentes a mudanças na estrutura do DOM.
    ```python
    # Bom: usando get_by_role
    page.get_by_role("button", name="Submit").click()
    
    # Evite: usar seletores CSS diretamente
    page.locator("button.submit-btn").click()
    ```
- **Use Locators**: Sempre use os locators embutidos do Playwright. Eles fornecem auto-waiting e retry-ability, o que torna os testes mais resilientes.
    ```python
    # Bom: usando locators embutidos
    page.get_by_role("button", name="Submit").click()
    ```

- **Prefira atributos visíveis ao usuário**: Use localizadores baseados em atributos visíveis ao usuário (role, text, label, placeholder) em vez de XPath ou seletores de classe CSS. Atributos voltados ao usuário são mais resistentes a mudanças no DOM.
    ```python
    # Bom: atributos visíveis ao usuário
    page.get_by_role("textbox", name="Username").fill("user123")
    page.get_by_label("Email").fill("user@example.com")
    page.get_by_placeholder("Enter password").fill("secret")
    
    # Evite: seletores de classe CSS
    page.locator(".form-input-class").fill("value")
    ```

- **Encadeie e filtre localizadores**: Encadeie localizadores para restringir buscas a partes específicas da página, obtendo maior precisão.
    ```python
    # Bom: encadeando localizadores
    page.locator("nav").get_by_role("link", name="Products").click()
    page.get_by_role("article").filter(has_text="Featured").get_by_role("button").click()
    ```

- **Evite problemas de seleção por posição**: Crie localizadores que identifiquem unicamente os elementos-alvo. Evite usar `.first()`, `.last()` ou `.nth()` quando possível, pois podem causar comportamento inesperado se a estrutura da página mudar.
    ```python
    # Evite: usar .first() quando o elemento não é único
    page.locator("button").first.click()
    
    # Bom: usar atributos específicos para identificar unicamente
    page.get_by_role("button", name="Delete Account").click()
    page.locator("button", has_text="Confirm").click()
    ```

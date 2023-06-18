# Pytest + playwright 


```python
from playwright.sync_api import Page


# При установленнои pytest-playwright - автоматически докинет страницу, даже не надо будет делать фикстуру
def test_some_page(page: Page):
    page.goto(url)
    
```

--- 

```bash 
# Запуск в режиме headless = False: 
pytest --headed 

# Запуск в slowmo: 
pytest --headed --slowmo 1000

# Определенный браузер
pytest --browser webkit

# Определенный девайс: 
pytest --device="iPhone 13 Mini"



```
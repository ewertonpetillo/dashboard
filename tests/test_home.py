import time

def test_home(browser):
    url = "http://0.0.0.0:8081/"
    browser.get(url)
    time.sleep(10)
    assert browser.title == "Dash"
    print("Teste da pagina inicial com sucesso!!")
    
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as OptionsChrome
from selenium.webdriver.firefox.options import Options as OptionsFirefox

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="fi",
                     help="Choose language. Supported languages: ar, cs, ca, da, de, en-gb, el, es, fi, fr, it, ko, "
                          "nl, pl, pt, pt-br, ro, ru, sk, uk, zh-hans")
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def language(request):
    language = request.config.getoption("language")
    yield language


@pytest.fixture(scope="function")
def browser(request, language):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = OptionsChrome()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        print(str(language))
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        options = OptionsFirefox()
        options.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()

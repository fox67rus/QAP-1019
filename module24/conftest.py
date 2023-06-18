import pytest

@pytest.fixture
def firefox_options(firefox_options):
    firefox_options.binary = "C:\Program Files\Mozilla Firefox\firefox.exe"
    firefox_options.add_argument('-foreground') # запуск в реальном режиме, для фонового - '-background'
    firefox_options.set_preference('browser.anchor_color', '#FF0000') # выбор цвета подложки браузера
    return firefox_options
@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.binary = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
    # chrome_options.add_extension('/path/to/extension.crx') # включение дополнений браузера
    chrome_options.add_argument('--kiosk') # защищённый полноэкранный режим без меню, применяемый в публичных местах
    return chrome_options



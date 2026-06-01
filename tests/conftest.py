import pytest
import csv
import os
from selenium import webdriver

@pytest.fixture(scope='function')
def driver():
    """Fixture untuk membuat driver browser baru di setiap test case menggunakan driver bawaan Selenium 4"""
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-notifications')

    # === TAMBAHKAN 2 BARIS INI AGAR BISA JALAN DI SERVER GITHUB LINUX ===
    options.add_argument('--headless')  # Menjalankan Chrome tanpa jendela visual
    options.add_argument('--no-sandbox')  # Syarat keamanan tambahan untuk server Linux
    options.add_argument('--disable-dev-shm-usage') # Mencegah crash memori di server cloud
    
    # KUNCI PERBAIKAN: Kita langsung panggil webdriver.Chrome() polos tanpa Service atau ChromeDriverManager
    d = webdriver.Chrome(options=options)
    
    yield d
    d.quit()

@pytest.fixture(scope='function')
def login_page(driver):
    """Fixture otomatis yang mengembalikan object halaman login"""
    from pages.login_page import LoginPage
    return LoginPage(driver)

def load_csv(filename):
    """Baca file CSV dari folder data/ dan kembalikan sebagai list of dict"""
    filepath = os.path.join('data', filename)
    with open(filepath, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return [row for row in reader]

        # ── FUNGSI MODUL 4.5: SCREENSHOT OTOMATIS SAAT FAIL ─────────────────────
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    
    # Jika pengujian selesai dijalankan ('call') dan hasilnya gagal (failed)
    if report.when == 'call' and report.failed:
        driver = item.funcargs.get('driver')
        if driver:
            # Buat foldernya jika belum ada
            os.makedirs('reports/screenshots', exist_ok=True)
            # Ambil nama file dari nama test case agar rapi
            name = item.nodeid.replace('/', '_').replace('::', '_')
            driver.save_screenshot(f'reports/screenshots/{name}.png')
            print(f'\n[ALERT] Test Gagal! Screenshot disimpan: reports/screenshots/{name}.png')
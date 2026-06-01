# pages/dashboard_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DashboardPage(BasePage):
    # Locators khusus halaman sukses login (Secure Area)
    LOGOUT_BTN = (By.CSS_SELECTOR, 'a.button.secondary.radius')
    SECURE_HEADER = (By.TAG_NAME, 'h2')

    def is_on_dashboard(self):
        """Memeriksa apakah teks 'Secure Area' tampil di halaman"""
        return "Secure Area" in self.get_text(self.SECURE_HEADER)

    def logout(self):
        """Melakukan aksi klik pada tombol Logout"""
        self.click(self.LOGOUT_BTN)
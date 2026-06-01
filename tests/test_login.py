import pytest
from pages.dashboard_page import DashboardPage

class TestLogin:
    def test_login_valid(self, login_page):
        login_page.login('tomsmith', 'SuperSecretPassword!')
        assert login_page.is_login_successful(), 'Login valid harus berhasil'

    def test_login_invalid_password(self, login_page):
        login_page.login('tomsmith', 'wrongpassword')
        assert login_page.is_login_failed(), 'Login dengan password salah harus gagal'

    def test_login_empty_username(self, login_page):
        login_page.login('', 'SuperSecretPassword!')
        assert login_page.is_login_failed(), 'Login tanpa username harus gagal'

    def test_flash_message_content(self, login_page):
        login_page.login('wronguser', 'wrongpass')
        msg = login_page.get_flash_message()
        assert 'invalid' in msg.lower(), f'Pesan error tidak sesuai: {msg}'

        # ── INI TAMBAHAN UNTUK LATIHAN 3.1 ──────────────────────────────────
    def test_complete_login_to_logout_flow(self, driver, login_page):
        """LATIHAN 3.1: Alur penuh sukses login -> masuk dashboard -> logout -> kembali ke login"""
        # 1. Login menggunakan kredensial yang valid
        login_page.login('tomsmith', 'SuperSecretPassword!')
        
        # 2. Validasi dengan method is_on_dashboard()
        dashboard = DashboardPage(driver)
        assert dashboard.is_on_dashboard(), 'User gagal masuk ke halaman Dashboard Utama'
        
        # 3. Jalankan aksi logout()
        dashboard.logout()
        
        # 4. Validasi user terlempar kembali ke halaman login semula
        assert "login" in login_page.get_current_url(), 'Setelah logout, URL tidak mengarah ke login page'
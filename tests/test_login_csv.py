# tests/test_login_csv.py
import pytest
import allure
from pages.login_page import LoginPage
from tests.conftest import load_csv

@allure.feature('Authentication')
@allure.story('Data-Driven Login CSV')
class TestLoginCSV:

    @pytest.mark.parametrize('row', load_csv('login_data.csv'))
    @allure.title('Login Test Skenario: {row[description]}')
    def test_login_from_csv(self, driver, row):
        """Membaca data dari data/login_data.csv secara otomatis dengan Anotasi Allure"""
        page = LoginPage(driver)
        
        # Mengelompokkan langkah pengujian agar rapi di dokumentasi
        with allure.step(f"Jalankan login untuk user: {row['username']}"):
            page.login(row['username'], row['password'])
        
        with allure.step("Validasi hasil asersi sesuai ekspektasi CSV"):
            if row['expected'] == 'PASS':
                assert page.is_login_successful(), f"Skenario [{row['description']}] harusnya BERHASIL"
            else:
                assert page.is_login_failed(), f"Skenario [{row['description']}] harusnya GAGAL"
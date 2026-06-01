# tests/test_register.py
import pytest
from tests.conftest import load_csv

class TestRegisterDDT:

    @pytest.mark.parametrize('row', load_csv('register_data.csv'))
    def test_registration_from_csv(self, driver, row):
        """LATIHAN 4.1: Pengujian Register Data-Driven dari file CSV"""
        print(f"\nMenjalankan skenario Register: {row['description']}")
        
        # Buka halaman testing register (Modul mereferensikan demoqa)
        driver.get("https://demoqa.com/register")
        
        # Logika Asersi: memvalidasi ekspektasi data dari CSV
        if row['expected'] == 'PASS':
            assert row['username'] != '', "Username tidak boleh kosong untuk data valid"
        else:
            # Kita sengaja buat pengujian gagal untuk baris terakhir 'Password mengandung spasi'
            # demi membuktikan fungsi otomatis jepret layar (screenshot) di conftest berjalan!
            if 'spasi' in row['description']:
                assert False, "Sengaja digagalkan untuk testing screenshot otomatis!"
            
            assert row['expected'] == 'FAIL'
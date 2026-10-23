from datetime import date

from app.models.bahan_makanan import BahanMakanan
from app.services.kedaluwarsa_checker import KedaluwarsaChecker

HARI_INI = date(2026, 10, 24)


def buat_bahan(tanggal_exp):
    return BahanMakanan(1, "Susu", 5, "liter", tanggal_exp)


def test_tanggal_kemarin_sudah_kedaluwarsa():
    checker = KedaluwarsaChecker()
    bahan = buat_bahan(date(2026, 10, 23))
    assert checker.sudah_kedaluwarsa(bahan, HARI_INI) is True


def test_tanggal_hari_ini_belum_kedaluwarsa():
    checker = KedaluwarsaChecker()
    bahan = buat_bahan(date(2026, 10, 24))
    assert checker.sudah_kedaluwarsa(bahan, HARI_INI) is False


def test_tanggal_besok_belum_kedaluwarsa():
    checker = KedaluwarsaChecker()
    bahan = buat_bahan(date(2026, 10, 25))
    assert checker.sudah_kedaluwarsa(bahan, HARI_INI) is False
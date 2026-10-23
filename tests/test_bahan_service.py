from datetime import date

import pytest

from app.exceptions import BahanTidakDitemukan, DataTidakValid
from app.repositories.memory_repository import MemoryRepository
from app.services.bahan_service import BahanService
from app.services.kedaluwarsa_checker import KedaluwarsaChecker

HARI_INI = date(2026, 10, 24)


def buat_service():
    return BahanService(MemoryRepository(), KedaluwarsaChecker())


def test_tambah_bahan_berhasil():
    service = buat_service()
    bahan = service.tambah_bahan("Tepung", 10, "kg", date(2027, 1, 1))
    assert bahan.id == 1
    assert service.ambil_bahan(1).nama == "Tepung"


def test_tambah_bahan_jumlah_negatif_ditolak():
    service = buat_service()
    with pytest.raises(DataTidakValid):
        service.tambah_bahan("Tepung", -1, "kg", date(2027, 1, 1))


def test_tambah_bahan_nama_kosong_ditolak():
    service = buat_service()
    with pytest.raises(DataTidakValid):
        service.tambah_bahan("  ", 5, "kg", date(2027, 1, 1))


def test_ambil_bahan_tidak_ada_harus_error():
    service = buat_service()
    with pytest.raises(BahanTidakDitemukan):
        service.ambil_bahan(99)


def test_ubah_bahan_berhasil():
    service = buat_service()
    service.tambah_bahan("Susu", 5, "liter", date(2027, 1, 1))
    hasil = service.ubah_bahan(1, "Susu UHT", 8, "liter", date(2027, 2, 1))
    assert hasil.nama == "Susu UHT"
    assert hasil.jumlah == 8


def test_hapus_bahan_berhasil():
    service = buat_service()
    service.tambah_bahan("Susu", 5, "liter", date(2027, 1, 1))
    service.hapus_bahan(1)
    assert service.daftar_bahan() == []


def test_hapus_bahan_tidak_ada_harus_error():
    service = buat_service()
    with pytest.raises(BahanTidakDitemukan):
        service.hapus_bahan(99)


def test_daftar_kedaluwarsa_hanya_yang_basi():
    service = buat_service()
    service.tambah_bahan("Susu basi", 1, "liter", date(2026, 10, 1))
    service.tambah_bahan("Tepung segar", 5, "kg", date(2027, 5, 1))

    hasil = service.daftar_kedaluwarsa(HARI_INI)

    assert len(hasil) == 1
    assert hasil[0].nama == "Susu basi"
    

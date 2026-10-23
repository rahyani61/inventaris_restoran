from datetime import date

from app.exceptions import BahanTidakDitemukan, DataTidakValid
from app.models.bahan_makanan import BahanMakanan
from app.repositories.base_repository import BaseRepository
from app.services.kedaluwarsa_checker import KedaluwarsaChecker


class BahanService:
    def __init__(self, repository: BaseRepository, checker: KedaluwarsaChecker):
        self.repository = repository
        self.checker = checker

    def tambah_bahan(self, nama: str, jumlah: float, satuan: str,
                     tanggal_kedaluwarsa: date) -> BahanMakanan:
        self._validasi(nama, jumlah)
        bahan = BahanMakanan(0, nama, jumlah, satuan, tanggal_kedaluwarsa)
        return self.repository.tambah(bahan)

    def daftar_bahan(self):
        return self.repository.ambil_semua()

    def ambil_bahan(self, bahan_id: int) -> BahanMakanan:
        bahan = self.repository.ambil_by_id(bahan_id)
        if bahan is None:
            raise BahanTidakDitemukan(bahan_id)
        return bahan

    def ubah_bahan(self, bahan_id: int, nama: str, jumlah: float, satuan: str,
                   tanggal_kedaluwarsa: date) -> BahanMakanan:
        self.ambil_bahan(bahan_id)  # error otomatis kalau tidak ada
        self._validasi(nama, jumlah)
        bahan_baru = BahanMakanan(bahan_id, nama, jumlah, satuan, tanggal_kedaluwarsa)
        return self.repository.ubah(bahan_id, bahan_baru)

    def hapus_bahan(self, bahan_id: int) -> None:
        self.ambil_bahan(bahan_id)  # error otomatis kalau tidak ada
        self.repository.hapus(bahan_id)

    def daftar_kedaluwarsa(self, hari_ini: date = None):
        return [
            bahan for bahan in self.repository.ambil_semua()
            if self.checker.sudah_kedaluwarsa(bahan, hari_ini)
        ]

    def _validasi(self, nama: str, jumlah: float) -> None:
        if not nama or not nama.strip():
            raise DataTidakValid("Nama bahan tidak boleh kosong")
        if jumlah < 0:
            raise DataTidakValid("Jumlah tidak boleh negatif")
from dataclasses import dataclass
from datetime import date


@dataclass
class BahanMakanan:
    id: int
    nama: str
    jumlah: float
    satuan: str
    tanggal_kedaluwarsa: date
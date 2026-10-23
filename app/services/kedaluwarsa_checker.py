from datetime import date


class KedaluwarsaChecker:
    """Hanya bertugas menentukan apakah bahan sudah kedaluwarsa."""

    def sudah_kedaluwarsa(self, bahan, hari_ini: date = None) -> bool:
        hari_ini = hari_ini or date.today()
        return bahan.tanggal_kedaluwarsa < hari_ini
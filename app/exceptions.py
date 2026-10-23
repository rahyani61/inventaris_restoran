class BahanTidakDitemukan(Exception):
    def __init__(self, bahan_id):
        super().__init__(f"Bahan dengan id {bahan_id} tidak ditemukan")
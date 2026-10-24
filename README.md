# Inventaris Bahan Makanan Restoran

Backend sederhana untuk mencatat bahan makanan restoran dan mengecek
bahan yang sudah kedaluwarsa. Dibuat dengan Python dan FastAPI.

## Cara Menjalankan

```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Buka http://127.0.0.1:8000/docs untuk mencoba API.

## Menjalankan Unit Test

```
pytest -v
```

## Daftar Endpoint

| Method | Endpoint | Fungsi |
|---|---|---|
| POST | /bahan | Tambah bahan |
| GET | /bahan | Lihat semua bahan |
| GET | /bahan/{id} | Lihat satu bahan |
| PUT | /bahan/{id} | Ubah bahan |
| DELETE | /bahan/{id} | Hapus bahan |
| GET | /bahan/kedaluwarsa | Lihat bahan yang sudah kedaluwarsa |

## Struktur Projek

- `app/models/` : bentuk data (BahanMakanan)
- `app/repositories/` : penyimpanan data (in-memory)
- `app/services/` : logika bisnis (BahanService, KedaluwarsaChecker)
- `app/routes/` : endpoint API
- `tests/` : unit test

Alur: Request -> routes -> services -> repositories

## Penerapan SOLID

- **SRP**: `KedaluwarsaChecker` hanya bertugas menentukan kedaluwarsa.
- **DIP**: `BahanService` bergantung pada `BaseRepository` (abstraksi),
  bukan pada `MemoryRepository`.
- **OCP**: repository baru (misal SQLite) bisa ditambah tanpa mengubah service.
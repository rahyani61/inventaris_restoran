from fastapi import FastAPI

from app.repositories.memory_repository import MemoryRepository
from app.routes import bahan_routes
from app.services.bahan_service import BahanService
from app.services.kedaluwarsa_checker import KedaluwarsaChecker

app = FastAPI(title="Inventaris Bahan Makanan Restoran")

# Di sini semua bagian "dirakit". Ganti repository cukup di satu tempat ini.
repository = MemoryRepository()
checker = KedaluwarsaChecker()
service = BahanService(repository, checker)

app.dependency_overrides[bahan_routes.get_service] = lambda: service
app.include_router(bahan_routes.router)
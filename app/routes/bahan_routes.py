from datetime import date

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from app.exceptions import BahanTidakDitemukan, DataTidakValid
from app.services.bahan_service import BahanService


class BahanInput(BaseModel):
    nama: str
    jumlah: float
    satuan: str
    tanggal_kedaluwarsa: date


router = APIRouter(prefix="/bahan", tags=["Bahan Makanan"])


def get_service() -> BahanService:
    # Diisi oleh main.py lewat dependency_overrides
    raise NotImplementedError


@router.post("", status_code=201)
def tambah_bahan(data: BahanInput, service: BahanService = Depends(get_service)):
    try:
        return service.tambah_bahan(**data.model_dump())
    except DataTidakValid as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("")
def daftar_bahan(service: BahanService = Depends(get_service)):
    return service.daftar_bahan()


@router.get("/kedaluwarsa")
def daftar_kedaluwarsa(service: BahanService = Depends(get_service)):
    return service.daftar_kedaluwarsa()


@router.get("/{bahan_id}")
def ambil_bahan(bahan_id: int, service: BahanService = Depends(get_service)):
    try:
        return service.ambil_bahan(bahan_id)
    except BahanTidakDitemukan as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.put("/{bahan_id}")
def ubah_bahan(bahan_id: int, data: BahanInput,
               service: BahanService = Depends(get_service)):
    try:
        return service.ubah_bahan(bahan_id, **data.model_dump())
    except BahanTidakDitemukan as e:
        raise HTTPException(status_code=404, detail=str(e))
    except DataTidakValid as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{bahan_id}", status_code=204)
def hapus_bahan(bahan_id: int, service: BahanService = Depends(get_service)):
    try:
        service.hapus_bahan(bahan_id)
    except BahanTidakDitemukan as e:
        raise HTTPException(status_code=404, detail=str(e))
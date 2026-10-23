from abc import ABC, abstractmethod


class BaseRepository(ABC):
    @abstractmethod
    def tambah(self, item): ...

    @abstractmethod
    def ambil_semua(self): ...

    @abstractmethod
    def ambil_by_id(self, id): ...

    @abstractmethod
    def ubah(self, id, item): ...

    @abstractmethod
    def hapus(self, id): ...
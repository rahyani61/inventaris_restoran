from .base_repository import BaseRepository


class MemoryRepository(BaseRepository):
    def __init__(self):
        self._data = {}
        self._next_id = 1

    def tambah(self, item):
        item.id = self._next_id
        self._data[item.id] = item
        self._next_id += 1
        return item

    def ambil_semua(self):
        return list(self._data.values())

    def ambil_by_id(self, id):
        return self._data.get(id)

    def ubah(self, id, item):
        if id not in self._data:
            return None
        item.id = id
        self._data[id] = item
        return item

    def hapus(self, id):
        return self._data.pop(id, None) is not None
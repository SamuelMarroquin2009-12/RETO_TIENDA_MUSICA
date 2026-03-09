from datetime import datetime
# TODO: Add code here my codee
from datetime import datetime
class Transaction:
    SELL = 1
    SUPPLY = 2
    def __init__(self, type: int, copies: int):
        self.type = type
        self.copies = copies
        self.date = datetime.now()
class Disc:
    def __init__(self, sid: str, title: str, artist: str, sale_price: float, purchase_price: float, quantity: int):
        self.sid = sid
        self.title = title
        self.artist = artist
        self.sale_price = sale_price
        self.purchase_price = purchase_price
        self.quantity = quantity
        self.transactions = []
        self.song_list = []
    def add_song(self, song: str):
        self.song_list.append(song)
    def sell(self, copies: int):
        if copies > self.quantity:
            return False
        self.quantity -= copies
        new_transaction = Transaction(Transaction.SELL, copies)
        self.transactions.append(new_transaction)
        return True
    def supply(self, copies: int):
        self.quantity += copies
        new_transaction = Transaction(Transaction.SUPPLY, copies)
        self.transactions.append(new_transaction)
    def copies_sold(self):
        total = 0
        for t in self.transactions:
            if t.type == Transaction.SELL:
                total += t.copies
        return total
    def __str__(self):
        songs = ", ".join(self.song_list)
        return f"SID: {self.sid}\nTitle: {self.title}\nArtist: {self.artist}\nSong List: {songs}"
class MusicStore:
    def __init__(self):
        self.discs = {}
    def add_disc(self, sid: str, title: str, artist: str, sale_price: float, purchase_price: float, quantity: int):
        if sid not in self.discs:
            nuevo_disco = Disc(sid, title, artist, sale_price, purchase_price, quantity)
            self.discs[sid] = nuevo_disco
    def search_by_sid(self, sid: str):
        return self.discs.get(sid, None)
    def search_by_artist(self, artist: str) -> list:
        return [d for d in self.discs.values() if d.artist == artist]
    def sell_disc(self, sid: str, copies: int) -> bool:
        disc = self.search_by_sid(sid)
        if disc is None:
            return False
        return disc.sell(copies)
    def supply_disc(self, sid: str, copies: int) -> bool:
        disc = self.search_by_sid(sid)
        if disc is None:
            return False
        disc.supply(copies)
        return True
    def worst_selling_disc(self):
        if not self.discs:
            return None
        peor_disco = None
        menor_cantidad = float('inf')
        for disc in self.discs.values():
            vendidos = disc.copies_sold()
            if vendidos < menor_cantidad:
                menor_cantidad = vendidos
                peor_disco = disc
        return peor_disco
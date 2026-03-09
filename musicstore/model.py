from datetime import datetime
class Transaction:
    # Constantes requeridas por el ejercicio
    SELL = 1
    SUPPLY = 2
    def __init__(self, type: int, copies: int):
        self.type = type
        self.copies = copies
        # Fecha y hora actual usando la librería datetime
        self.date = datetime.now()
class Disc:
    def __init__(self, sid: str, title: str, artist: str, sale_price: float, purchase_price: float, quantity: int):
        self.sid = sid
        self.title = title
        self.artist = artist
        self.sale_price = sale_price
        self.purchase_price = purchase_price
        self.quantity = quantity
        # Inicialización de listas vacías según el requisito 2
        self.transactions = []
        self.song_list = []
    def add_song(self, song: str):
        self.song_list.append(song)
    def sell(self, copies: int):
        if copies > self.quantity:
            return False
        self.quantity -= copies
        # Se crea la transacción usando la constante de la clase Transaction
        nueva_venta = Transaction(Transaction.SELL, copies)
        self.transactions.append(nueva_venta)
        return True
    def supply(self, copies: int):
        self.quantity += copies
        # Se crea la transacción de abastecimiento
        nuevo_suministro = Transaction(Transaction.SUPPLY, copies)
        self.transactions.append(nuevo_suministro)
    def copies_sold(self) -> int:
        total = 0
        for t in self.transactions:
            if t.type == Transaction.SELL:
                total += t.copies
        return total
    def __str__(self):
        # Formateo de lista de canciones separada por coma y espacio
        canciones_str = ", ".join(self.song_list)
        return f"SID: {self.sid}\nTitle: {self.title}\nArtist: {self.artist}\nSong List: {canciones_str}"
class MusicStore:
    def __init__(self):
        # El requisito pide que sea un diccionario de tipo dict[str, Disc]
        self.discs = {}
    def add_disc(self, sid: str, title: str, artist: str, sale_price: float, purchase_price: float, quantity: int):
        if sid not in self.discs:
            nuevo_disco = Disc(sid, title, artist, sale_price, purchase_price, quantity)
            self.discs[sid] = nuevo_disco
    def search_by_sid(self, sid: str):
        if sid in self.discs:
            return self.discs[sid]
        return None
    def search_by_artist(self, artist: str):
        resultado = []
        for disco in self.discs.values():
            if disco.artist == artist:
                resultado.append(disco)
        return resultado
    def sell_disc(self, sid: str, copies: int):
        disco = self.search_by_sid(sid)
        if disco is None:
            return False
        return disco.sell(copies)
    def supply_disc(self, sid: str, copies: int):
        disco = self.search_by_sid(sid)
        if disco is None:
            return False
        disco.supply(copies)
        return True
    def worst_selling_disc(self):
        if not self.discs:
            return None
        peor_disco = None
        menor_cantidad = float('inf')
        for disco in self.discs.values():
            vendidos = disco.copies_sold()
            if vendidos < menor_cantidad:
                menor_cantidad = vendidos
                peor_disco = disco
        return peor_disco
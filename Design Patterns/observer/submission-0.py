class Observer(ABC):
    @abstractmethod
    def notify(self, itemName: str) -> None:
        pass

class Customer(Observer):
    def __init__(self, name: str) -> None:
        self.name = name
        self.notifications = 0

    def notify(self, itemName: str) -> None:
        self.notifications += 1

    def countNotifications(self) -> int:
        return self.notifications

class OnlineStoreItem:
    def __init__(self, itemName: str, stock: int) -> None:
        self.itemName = itemName
        self.stock = stock
        self.subs = []

    def subscribe(self, observer: Observer) -> None:
        self.subs.append(observer)

    def unsubscribe(self, observer: Observer) -> None:
        self.subs.remove(observer)
        

    def updateStock(self, newStock: int) -> None:
        old_stock = self.stock
        self.stock = newStock
        if old_stock == 0 and newStock > 0:
            for sub in self.subs:
                sub.notify(self.itemName)
        

from app.db.crud import CRUDBase
from app.db.model import CreditCard
from app.db.schema import CreditCardSchema


class CartRepository(CRUDBase[CreditCard, CreditCardSchema]):
    pass


credit_card_repository = CartRepository(CreditCard)

from app.db.crud import CRUDBase
from app.db.model import CreditCard
from app.db.schema import CreditCardSchema, CreditCardSchemaUpdate


class CartRepository(CRUDBase[CreditCard, CreditCardSchema, CreditCardSchemaUpdate]):
    pass


credit_card_repository = CartRepository(CreditCard)

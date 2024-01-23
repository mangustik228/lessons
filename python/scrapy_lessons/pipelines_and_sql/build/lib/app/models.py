from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase


class Base(DeclarativeBase):
    ...


class Product(Base):
    __tablename__ = "product"
    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    title: Mapped[str]
    price: Mapped[float]
    url: Mapped[str]

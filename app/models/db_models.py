# Обычно разношу модели по отдельным файлам, но модели маленькие и так проверить проще

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'

    uid: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)

    properties: Mapped[list['Property']] = relationship('Property', back_populates='product')


class Property(Base):
    __tablename__ = 'properties'

    uid: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    type: Mapped[str] = mapped_column(nullable=False)
    product_uid: Mapped[int] = mapped_column(ForeignKey('products.uid'))

    product: Mapped[Product] = relationship('Product', back_populates='properties')
    values: Mapped[list['PropertyValue']] = relationship('PropertyValue', back_populates='property')


class PropertyValue(Base):
    __tablename__ = 'property_values'

    value_uid: Mapped[int] = mapped_column(primary_key=True)
    value: Mapped[str] = mapped_column(nullable=False)
    property_uid: Mapped[int] = mapped_column(ForeignKey('properties.uid'))

    property: Mapped[Property] = relationship('Property', back_populates='values')

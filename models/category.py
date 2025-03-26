from sqlalchemy.orm import Mapped, mapped_column

from models import db

class Category(db.Model):
    __tablename__ = 'category'

    id: Mapped[int] = mapped_column(
        db.Integer,
        db.Identity(always=True),
        primary_key=True,
        autoincrement=True
    )
    name: Mapped[str] = mapped_column(
        db.String(255), nullable=False
    )

    questions: Mapped[list['Question']] = db.relationship('Question', back_populates='category')

    def __repr__(self):
        return f'Category: {self.name}'
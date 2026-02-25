from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List, Optional

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)

    favorites: Mapped[List["Favorite"]] = relationship(
        "Favorite", back_populates="user")

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
            #
            #
            #

            "is_active": self.is_active,


        }


class Favorite(db.Model):
    __tablename__ = "favorite"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    character_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("character.id"), nullable=True)
    planet_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("planet.id"), nullable=True)

    user: Mapped["User"] = relationship("User", back_populates="favorites")
    character: Mapped[Optional["Character"]] = relationship(
        "Character", back_populates="favorites")
    planet: Mapped[Optional["Planet"]] = relationship(
        "Planet", back_populates="favorites")

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character_id": self.character_id,
            "planet_id": self.planet_id,

        }


class Character(db.Model):
    __tablename__ = "character"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    gender: Mapped[Optional[str]] = mapped_column(String(50))
    height: Mapped[Optional[str]] = mapped_column(String(50))
    eye_color: Mapped[Optional[str]] = mapped_column(String(50))

    favorites: Mapped[List["Favorite"]] = relationship(
        "Favorite", back_populates="character")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "height": self.height,
            "eye_color": self.eye_color
        }


class Planet(db.Model):
    __tablename__ = "planet"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    climate: Mapped[Optional[str]] = mapped_column(String(120))
    population: Mapped[Optional[str]] = mapped_column(String(120))
    terrain: Mapped[Optional[str]] = mapped_column(String(120))

    favorites: Mapped[List["Favorite"]] = relationship(
        "Favorite", back_populates="planet")

    def serialize(self):

        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "population": self.population,
            "terrain": self.terrain


        }

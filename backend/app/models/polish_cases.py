from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..database import Base


class GrammaticalCase(Base):
    __tablename__ = "grammatical_cases"

    case_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    question = Column(String, nullable=False)


class Noun(Base):
    __tablename__ = "nouns"

    noun_id = Column(Integer, primary_key=True)
    base_form = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    is_plural = Column(Boolean, default=False)
    forms = relationship("NounForm", back_populates="noun")


class NounForm(Base):
    __tablename__ = "noun_forms"

    form_id = Column(Integer, primary_key=True)
    case_id = Column(Integer, ForeignKey("grammatical_cases.case_id"))
    noun_id = Column(Integer, ForeignKey("nouns.noun_id"))
    form = Column(String, nullable=False)
    noun = relationship("Noun", back_populates="forms")
    case = relationship("GrammaticalCase")


class Adjective(Base):
    __tablename__ = "adjectives"

    adjective_id = Column(Integer, primary_key=True)
    base_form = Column(String, nullable=False)
    is_plural = Column(Boolean, default=False)
    forms = relationship("AdjectiveForm", back_populates="adjective")


class AdjectiveForm(Base):
    __tablename__ = "adjective_forms"

    form_id = Column(Integer, primary_key=True)
    case_id = Column(Integer, ForeignKey("grammatical_cases.case_id"))
    adjective_id = Column(Integer, ForeignKey("adjectives.adjective_id"))
    gender = Column(String, nullable=False)
    form = Column(String, nullable=False)

    adjective = relationship("Adjective", back_populates="forms")
    case = relationship("GrammaticalCase")

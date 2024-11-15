from typing import List, TypedDict

from sqlalchemy.orm import Session

from ..database import SessionLocal
from ..models.polish_cases import (
    Adjective,
    AdjectiveForm,
    GrammaticalCase,
    Noun,
    NounForm,
)


class NounData(TypedDict):
    base_form: str
    is_plural: bool
    gender: str


class NounFormData(TypedDict):
    noun_id: int
    case_id: int
    form: str


class AdjData(TypedDict):
    base_form: str
    is_plural: bool


class AdjFormData(TypedDict):
    adjective_id: int
    case_id: int
    gender: str
    form: str


def seed_cases(db: Session):
    """Seed the database with Grammatical cases."""
    cases = [
        {"name": "Mianownik", "question": "Kto/Co"},
        {"name": "Dopełniacz", "question": "Kogo/Czego"},
        {"name": "Celownik", "question": "Komu/Czemu"},
        {"name": "Biernik", "question": "Kogo/Co"},
        {"name": "Narzędnik", "question": "Z kim/Z czym"},
        {"name": "Miejscownik", "question": "Na kim/Na czym"},
        {"name": "Wołacz", "question": ""},
    ]

    for case in cases:
        db_case = GrammaticalCase(**case)
        db.add(db_case)
    db.commit()


def seed_nouns(db: Session):
    """Seed the database with Nouns."""
    nouns: List[NounData] = [
        {"base_form": "Polak", "is_plural": False, "gender": "M living"},
        {"base_form": "Polka", "is_plural": False, "gender": "F"},
        {"base_form": "Samochód", "is_plural": False, "gender": "M non-living"},
        {"base_form": "Drzewo", "is_plural": False, "gender": "N"},
        {"base_form": "Miejsce", "is_plural": False, "gender": "N"},
        {"base_form": "Polacy", "is_plural": True, "gender": "M"},
        {"base_form": "Polki", "is_plural": True, "gender": "F"},
        {"base_form": "Drzewa", "is_plural": True, "gender": "N"},
        {"base_form": "Morza", "is_plural": True, "gender": "N"},
    ]

    for noun in nouns:
        db_noun = Noun(**noun)
        db.add(db_noun)
    db.commit()


def seed_noun_forms(db: Session):
    """Seed the database with Noun forms."""
    noun_forms: List[NounFormData] = [
        # Polak (Masc living, singular)
        {"noun_id": 1, "case_id": 1, "form": "Polak"},
        {"noun_id": 1, "case_id": 2, "form": "Bez Polaka"},
        {"noun_id": 1, "case_id": 3, "form": "Daje Polaku"},
        {"noun_id": 1, "case_id": 4, "form": "Polak"},
        {"noun_id": 1, "case_id": 5, "form": "Z Polakiem"},
        {"noun_id": 1, "case_id": 6, "form": "Na Polaku"},
        {"noun_id": 1, "case_id": 7, "form": "Polak!"},
        # Polka (Fem, singular)
        {"noun_id": 2, "case_id": 1, "form": "Polka"},
        {"noun_id": 2, "case_id": 2, "form": "Bez Polki"},
        {"noun_id": 2, "case_id": 3, "form": "Daje Polce"},
        {"noun_id": 2, "case_id": 4, "form": "Polkę"},
        {"noun_id": 2, "case_id": 5, "form": "Z Polką"},
        {"noun_id": 2, "case_id": 6, "form": "Na Polce"},
        {"noun_id": 2, "case_id": 7, "form": "Polka!"},
        # Samochód (Masc non-living, singular)
        {"noun_id": 3, "case_id": 1, "form": "Samochód"},
        {"noun_id": 3, "case_id": 2, "form": "Bez Samochodu"},
        {"noun_id": 3, "case_id": 3, "form": "Samochodu"},
        {"noun_id": 3, "case_id": 4, "form": "Samochód"},
        {"noun_id": 3, "case_id": 5, "form": "Samochodem"},
        {"noun_id": 3, "case_id": 6, "form": "W Samochodzie"},
        {"noun_id": 3, "case_id": 7, "form": "Samochód!"},
        # Drzewo (Neutr, singular)
        {"noun_id": 4, "case_id": 1, "form": "Drzewo"},
        {"noun_id": 4, "case_id": 2, "form": "Bez Drzewa"},
        {"noun_id": 4, "case_id": 3, "form": "Drzewu"},
        {"noun_id": 4, "case_id": 4, "form": "Drzewo"},
        {"noun_id": 4, "case_id": 5, "form": "Z Drzewem"},
        {"noun_id": 4, "case_id": 6, "form": "Na Drzewie"},
        {"noun_id": 4, "case_id": 7, "form": "Drzewo!"},
        # Miejsce (Neutr, singular)
        {"noun_id": 5, "case_id": 1, "form": "Miejsce"},
        {"noun_id": 5, "case_id": 2, "form": "Bez Miejsca"},
        {"noun_id": 5, "case_id": 3, "form": "Miejscu"},
        {"noun_id": 5, "case_id": 4, "form": "Miejsce"},
        {"noun_id": 5, "case_id": 5, "form": "Z Miejscem"},
        {"noun_id": 5, "case_id": 6, "form": "Na Miejscu"},
        {"noun_id": 5, "case_id": 7, "form": "Miejsce!"},
        # Polacy (Masc, plural)
        {"noun_id": 6, "case_id": 1, "form": "Polacy"},
        {"noun_id": 6, "case_id": 2, "form": "Bez Polaków"},
        {"noun_id": 6, "case_id": 3, "form": "Daje Polakom"},
        {"noun_id": 6, "case_id": 4, "form": "Polacy"},
        {"noun_id": 6, "case_id": 5, "form": "Z Polakami"},
        {"noun_id": 6, "case_id": 6, "form": "Na Polakach"},
        {"noun_id": 6, "case_id": 7, "form": "Polacy!"},
        # Polki (Fem, plural)
        {"noun_id": 7, "case_id": 1, "form": "Polki"},
        {"noun_id": 7, "case_id": 2, "form": "Bez Polek"},
        {"noun_id": 7, "case_id": 3, "form": "Daje Polkom"},
        {"noun_id": 7, "case_id": 4, "form": "Polki"},
        {"noun_id": 7, "case_id": 5, "form": "Z Polkami"},
        {"noun_id": 7, "case_id": 6, "form": "Na Polkach"},
        {"noun_id": 7, "case_id": 7, "form": "Polki!"},
        # Drzewa (Neutr, plural)
        {"noun_id": 8, "case_id": 1, "form": "Drzewa"},
        {"noun_id": 8, "case_id": 2, "form": "Bez Drzew"},
        {"noun_id": 8, "case_id": 3, "form": "Drzewam"},
        {"noun_id": 8, "case_id": 4, "form": "Drzewa"},
        {"noun_id": 8, "case_id": 5, "form": "Z Drzewami"},
        {"noun_id": 8, "case_id": 6, "form": "Na Drzewach"},
        {"noun_id": 8, "case_id": 7, "form": "Drzewa!"},
        # Morza (Neutr, plural)
        {"noun_id": 9, "case_id": 1, "form": "Morza"},
        {"noun_id": 9, "case_id": 2, "form": "Bez Morza"},
        {"noun_id": 9, "case_id": 3, "form": "Morzam"},
        {"noun_id": 9, "case_id": 4, "form": "Morza"},
        {"noun_id": 9, "case_id": 5, "form": "Z Morzami"},
        {"noun_id": 9, "case_id": 6, "form": "Na Morzach"},
        {"noun_id": 9, "case_id": 7, "form": "Morza!"},
    ]

    for noun_form in noun_forms:
        db_noun_form = NounForm(**noun_form)
        db.add(db_noun_form)
    db.commit()


def seed_adjectives(db: Session):
    """Seed the database with Adjectives."""
    adjectives: List[AdjData] = [
        {"base_form": "Polski", "is_plural": False},
    ]

    for adjective in adjectives:
        db_adjective = Adjective(**adjective)
        db.add(db_adjective)
    db.commit()


def seed_adjective_forms(db: Session):
    """Seed the database with Adjective forms."""
    adjective_forms: List[AdjFormData] = [
        # Polski (Masc living, singular)
        {"adjective_id": 1, "case_id": 1, "gender": "M living", "form": "Polski"},
        {"adjective_id": 1, "case_id": 2, "gender": "M living", "form": "Do Polskiego"},
        {
            "adjective_id": 1,
            "case_id": 3,
            "gender": "M living",
            "form": "Daje Polskiemu",
        },
        {"adjective_id": 1, "case_id": 4, "gender": "M living", "form": "Polskiego"},
        {"adjective_id": 1, "case_id": 5, "gender": "M living", "form": "Z Polskim"},
        {"adjective_id": 1, "case_id": 6, "gender": "M living", "form": "W Polskim"},
        {"adjective_id": 1, "case_id": 7, "gender": "M living", "form": "Polski!"},
    ]

    for adjective_form in adjective_forms:
        db_adjective_form = AdjectiveForm(**adjective_form)
        db.add(db_adjective_form)
    db.commit()


def seed_all():
    """Run all the seeding functions."""
    db = SessionLocal()
    try:
        # Check if data already exists
        existing_case = db.query(GrammaticalCase).first()
        if not existing_case:
            print("Seeding cases...")
            seed_cases(db)

        existing_noun = db.query(Noun).first()
        if not existing_noun:
            print("Seeding nouns...")
            seed_nouns(db)

        existing_noun_form = db.query(NounForm).first()
        if not existing_noun_form:
            print("Seeding noun forms...")
            seed_noun_forms(db)

        existing_adj = db.query(Adjective).first()
        if not existing_adj:
            print("Seeding adjectives...")
            seed_adjectives(db)

        existing_adj_form = db.query(AdjectiveForm).first()
        if not existing_adj_form:
            print("Seeding adjective forms...")
            seed_adjective_forms(db)

        print("Seeding complete!")
    except Exception as e:
        print(f"Error while seeding: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    seed_all()

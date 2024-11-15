from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqladmin import Admin, ModelView
from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request
from starlette.responses import RedirectResponse

from .database import engine
from .models.polish_cases import (
    Adjective,
    AdjectiveForm,
    GrammaticalCase,
    Noun,
    NounForm,
)


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        username = form.get("username")
        password = form.get("password")

        valid_username = "admin"
        valid_password = "we_LearmGrammar"

        valid = username == valid_username and password == valid_password

        if valid:
            # set the token in the session
            request.session.update({"token": "admin"})

        return valid

    async def logout(self, request: Request) -> bool:
        # remove the token from the session
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        # validate the session
        token = request.session.get("token")
        if not token:
            return False
        return token == "admin"


app = FastAPI(
    title="Polish Cases API",
    description="API for Polish language cases",
    version="1.0.0",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins for development
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


# create admin views
class GrammaticalCaseAdmin(ModelView, model=GrammaticalCase):
    name = "Grammatical Case"
    name_plural = "Grammatical Cases"
    icon = "fa-solid fa-book"
    column_list = ["case_id", "name", "question"]
    column_searchable_list = ["name"]  # Columns that can be searched
    column_sortable_list = [
        "name",
        "question",
    ]  # Columns that can be sorted


class NounAdmin(ModelView, model=Noun):
    name = "Noun"
    name_plural = "Nouns"
    icon = "fa-solid fa-font"
    column_list = ["noun_id", "base_form", "gender", "is_plural"]
    column_sortable_list = [
        "noun_id",
        "base_form",
        "gender",
    ]  # Columns that can be sorted
    column_searchable_list = ["base_form"]  # Columns that can be searched
    column_filters = ["gender", "is_plural"]  # Columns that can be filtered


class NounFormAdmin(ModelView, model=NounForm):
    name = "Noun Form"
    name_plural = "Noun Forms"
    icon = "fa-solid fa-pen"
    column_list = ["form_id", "case_id", "noun_id", "form"]
    column_sortable_list = [
        "form_id",
        "case_id",
        "noun_id",
        "form",
    ]  # Columns that can be sorted


class AdjectiveAdmin(ModelView, model=Adjective):
    name = "Adjective"
    name_plural = "Adjectives"
    icon = "fa-solid fa-font"
    column_list = ["adjective_id", "base_form", "is_plural"]
    column_sortable_list = [
        "adjective_id",
        "base_form",
    ]  # Columns that can be sorted
    column_searchable_list = ["base_form"]  # Columns that can be searched
    column_filters = ["is_plural"]  # Columns that can be filtered


class AdjectiveFormAdmin(ModelView, model=AdjectiveForm):
    name = "Adjective Form"
    name_plural = "Adjective Forms"
    icon = "fa-solid fa-pen"
    column_list = ["form_id", "case_id", "adjective_id", "gender", "form"]
    column_sortable_list = ["form_id", "case_id", "adjective_id", "form"]
    column_filters = ["gender"]  # Columns that can be filtered


# create the authentication backend
authentication_backend = AdminAuth(secret_key="some-secret-key")

# create an admin interface
admin = Admin(
    app,
    engine,
    authentication_backend=authentication_backend,
    title="Polish Cases Admin",
)

# Add views to the admin interface
admin.add_view(GrammaticalCaseAdmin)
admin.add_view(NounAdmin)
admin.add_view(NounFormAdmin)
admin.add_view(AdjectiveAdmin)
admin.add_view(AdjectiveFormAdmin)


@app.get("/")
async def root():
    return {"message": "Hello World"}


# Health check endpoint (useful for deployment)
@app.get("/health")
async def health_check():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

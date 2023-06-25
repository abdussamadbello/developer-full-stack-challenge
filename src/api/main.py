from fastapi import FastAPI
import routes

app = FastAPI()
app.include_router(routes.login_router)
app.include_router(routes.books_router)
app.include_router(routes.authors_router)


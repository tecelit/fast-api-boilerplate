from fastapi import FastAPI
from core.dependencies import setup_db_dependency
from api.v1.users import routes as user_routes

app = FastAPI(
    title="ExcelusAI-API",
    description="API",
    version="1.0.0",
    openapi_url="/openapi.json",
)

# Include user routes
app.include_router(user_routes.router, prefix="/users", tags=["users"])

# Set up database dependency globally
setup_db_dependency(app)

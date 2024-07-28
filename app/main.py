from fastapi import FastAPI

from app import setup
from app.config import settings
from app.containers import container

app_container_modules = [
    "app.api.rest.routes.v1.user_api",
    "app.api.rest.routes.v1.health",
    # TODO: Add here the CLI modules to inject dependencies
]


def create_app() -> FastAPI:
    app = FastAPI(title=settings.APP_TITLE, docs_url="/api/docs/ui", debug=settings.DEBUG)
    container.wire(app_container_modules)

    setup.setup_logging()
    setup.setup_error_handler(app)
    setup.setup_routes(app)
    return app

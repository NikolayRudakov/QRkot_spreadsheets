# app/api/endpoints/__init__.py
from .google_api import router as google_api_router
from .charityproject import router as charity_project_router  # noqa
from .donation import router as donation_router  # noqa
from .user import router as user_router  # noqa
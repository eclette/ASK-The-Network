"""App entrypoint"""


from google.adk.cli.fast_api import get_fast_api_app
from src.core.settings import settings


app = get_fast_api_app(
    agents_dir=settings.AGENT_DIR,
    session_service_uri=settings.SESSION_SERVICE_URI,
    artifact_service_uri=None,
    allow_origins=["*"],
    web=True,
)


# uvicorn src.services:app --host 0.0.0.0 --port 3456 --reload
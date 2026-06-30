"""Settings"""

from pathlib import Path
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings"""

    # dirs
    WORKING_DIR: Path = Path(__file__).resolve().parent.parent.parent
    AGENT_DIR: str = str(WORKING_DIR / "src/network_agent")
    SESSION_SERVICE_URI:str = f"sqlite:///{str(WORKING_DIR / "sessions.db")}"
    DATA_DIR: Path = WORKING_DIR / "src/data"

    #db
    DB_URL:str ="mysql+pymysql://root:Changeme_123@localhost:3306/radio_network_data"

    # model
    MODEL_NAME: str = "gemini-3-flash-preview"
    GOOGLE_API_KEY: str = ""

    MAX_ROWS: int = 20


settings = Settings()
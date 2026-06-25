"""Pydantic models"""

from pydantic import BaseModel, Field
from typing import Literal, List, Any


class SQLCommandResult(BaseModel):
    """Normalized queries returned from SQL tools"""

    status: Literal["success", "failure"]
    rows: List[dict[str, Any]] = Field(default_factory=list)
    error: str | None = None


    @classmethod
    def success(cls, rows: list[dict[str, Any]]) -> "SQLCommandResult":
        return cls(status="success", rows=rows)

    @classmethod
    def failure(cls, error: str):
        return cls(status="failure", error=error)
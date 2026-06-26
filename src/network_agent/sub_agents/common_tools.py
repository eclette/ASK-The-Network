"""Tools for all sub-agents"""

from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError


from src.data_models.models import SQLCommandResult

from src.database.db import engine


def send_sql_command(sql_query: str):
    """Execute a SQL command using the configured database connection.

      Args:
          sql_query: Raw SQL query to execute.

      Returns:
          SQLCommandResult with either returned rows or error details.
    """

    if not sql_query:
        return SQLCommandResult.failure("sql_query parameter should not be empty")

    try:
        with engine.connect() as connection:
            result = connection.execute(text(sql_query))

            if result.returns_rows:
                rows = [dict(row) for row in result.mappings().all()]
                return SQLCommandResult.success(rows=rows)
    except SQLAlchemyError as e:
        return SQLCommandResult.failure(str(e))
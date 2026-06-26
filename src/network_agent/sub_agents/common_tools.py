"""Tools for all sub-agents"""

from logging import getLogger

from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from src.data_models.models import SQLCommandResult
from src.database.db import engine


logger = getLogger(__name__)
sql_command_logger = getLogger("audit.sql.commands")
sql_result_logger = getLogger("audit.sql.results")


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
            sql_command_logger.info(f"Sending SQL command: {sql_query}")
            result = connection.execute(text(sql_query))

            if result.returns_rows:
                rows = [dict(row) for row in result.mappings().all()]
                sql_result_logger.info(f"rows: {rows}")
                return SQLCommandResult.success(rows=rows)
    except SQLAlchemyError as e:
        logger.error(str(e))
        return SQLCommandResult.failure(str(e))

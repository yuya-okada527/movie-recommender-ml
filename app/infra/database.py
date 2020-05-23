from sqlalchemy import create_engine

from ..config import settings

DB_URL = \
    f"{settings.db_engine}://" \
    f"{settings.db_user}:{settings.db_password}" \
    f"@{settings.db_host}:{settings.db_port}/{settings.db_name}"

engine = create_engine(DB_URL)

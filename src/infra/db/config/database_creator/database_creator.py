#pylint:disable=W0611
from sqlalchemy import Engine
from src.infra.db.config.base_entity.base import Base
from src.infra.db.entities.users import Users

def create_tables(engine:Engine) -> None:
    Base.metadata.create_all(engine)
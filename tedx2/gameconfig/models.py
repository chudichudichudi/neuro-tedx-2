# -*- coding: utf-8 -*-

from tedx2.database import (
    Column,
    db,
    Model,
    SurrogatePK,
)


class GameConfig(SurrogatePK, Model):
    __tablename__ = 'game_config'
    name = Column(db.String(250), unique=True, nullable=False)
    config = Column(db.Unicode)

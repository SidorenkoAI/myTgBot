from dataclasses import dataclass
from environs import Env
import sqlite3

@dataclass
class TgBot:
    token: str            # Токен для доступа к телеграм-боту

@dataclass
class DatabaseConfig:
    dbPath: str

    def getConnect(self):
        connection = sqlite3.connect(self.dbPath)
        cursor = connection.cursor()
        # Создаем таблицу Users
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY,
        tgid INTEGER NOT NULL,
        username TEXT,
        allgames INTEGER NOT NULL,
        wingames INTEGER NOT NULL,
        UNIQUE(tgid)
        )
        ''')
        # Сохраняем изменения
        connection.commit()
        return connection

@dataclass
class Config:
    tg_bot: TgBot
    db: DatabaseConfig

def load_config(dbPath: str, path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(
        tg_bot=TgBot(
            token=env('BOT_TOKEN'),
        ),
        db=DatabaseConfig(dbPath=dbPath)
    )
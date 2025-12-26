from sqlalchemy import select
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from db.models import Base, User

from config import DB_PATH


class Database:
    def __init__(self, db_path: str):
        self.engine = create_async_engine(
            f"sqlite+aiosqlite:///{db_path}",
            echo=False,
        )
        self.session_factory = async_sessionmaker(self.engine, expire_on_commit=False)

    async def initialize(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    async def add_user_if_not_exists(self, user_id: int) -> bool:
        async with self.session_factory() as session:
            result = await session.execute(select(User).where(User.user_id == user_id))
            user = result.scalar_one_or_none()

            if user:
                return False

            session.add(User(user_id=user_id))
            await session.commit()
            return True


db = Database(DB_PATH)

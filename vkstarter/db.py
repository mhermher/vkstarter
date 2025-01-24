from functools import wraps
from typing import Callable, Concatenate, Generator, Optional

from sqlalchemy import create_engine
from sqlmodel import Session, SQLModel

sqlite_name = 'data.db'
sqlite_url = f'sqlite:///{sqlite_name}'

engine = create_engine(sqlite_url, echo = True, connect_args = {'check_same_thread': False})

def create_db() -> None:
    '''Create the database.'''
    SQLModel.metadata.create_all(engine)

def get_session() -> Generator[Session, None, None]:
    '''Get session from engine.'''
    with Session(engine) as session:
        yield session


def with_session[R, **P](func: Callable[Concatenate[Session, P], R]) -> Callable[Concatenate[Session, P], R]:
    '''Provide a session to a function where it is optional.'''
    @wraps(func)
    def wrapper(session: Optional[Session], *args: P.args, **kwargs: P.kwargs) -> R:
        if session is None:
            session = Session(engine)
        return func(session, *args, **kwargs)
    return wrapper

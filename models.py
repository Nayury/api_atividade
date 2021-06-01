from sqlalchemy import create_engine, Column, INTEGER,String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///atividades.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

class Pessoas(Base):
    __tablename__='pessoas'
    id = Column(INTEGER, primary_key=True)
    nome = Column(String(40), index=True)
    idade = Column(INTEGER)

    def __repr__(self):
        return '<Pessoa  {}>'.format(self.nome)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

class Atividades(Base):
    __tablename__ ="atividades"
    id = Column(INTEGER, primary_key=True)
    nome = Column(String(80))
    pessoa_id = Column(INTEGER, ForeignKey('pessoas.id'))
    pessoa = relationship('Pessoas')

    def __repr__(self):
        return '<Atividades  {}>'.format(self.nome)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

class Usuarios(Base):
    __tablename__ = 'usuarios'
    id = Column(INTEGER, primary_key=True)
    login = Column(String(20), unique=True)
    senha = Column(String(20))

    def __repr__(self):
        return '<Usuario {}'.format(self.login)
    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()


def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()

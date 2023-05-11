from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.horizontal_shard import ShardedQuery
from sqlalchemy.ext.horizontal_shard import ShardedSession
from base_model import BaseModel
from orms.tables import VerificationOtp

class CustomQuery(ShardedQuery):
    def paginate(self, page: int, page_size: int):
        return self.limit(page_size).offset((page - 1) * page_size)

user = "julian_decoss"
password = "l!JK&7dV!cvPc-Bk" #CONTRASEÑA
host = "main-ro.db.private.konfio.mx" #PROD SI QUIERES HACER QUERIES EN DEV COMENTA LA 14 Y DESCOMENTA LA 15 Y VISCEVERSA
#host = "dev.db.private.konfio.mx"
port = "3306"
ssl_args = {'sslrootcert': '/Users/intern/Downloads/rds-ca-2019-root.pem',} #AQUI VA EL ROOT PEM QUE ES EL ARCHIVO QUE TE DAN PARA CONECTARTE A PROD
engine = create_engine(
    f"mysql+pymysql://{user}:{password}@{host}:{port}",
    pool_pre_ping=True,
    connect_args={
        "ssl": {"ssl_ca": '/Users/intern/Downloads/rds-ca-2019-root.pem'}, #AQUI VA EL ROOT PEM QUE ES EL ARCHIVO QUE TE DAN PARA CONECTARTE A PROD
        "connect_timeout": 25
        },
    pool_size=20,
    pool_recycle=300,
)

aurora_shards = {
    "konfio": engine
}

shards = {**aurora_shards}

def shard_chooser(mapper, instance, clause=None):
    shard = BaseModel.get_shard()

    if shard not in shards:
        raise Exception

    if mapper:
        shard = mapper.class_.get_shard()

    return shard


def id_chooser(query, ident):
    shard = BaseModel.get_shard()

    if shard not in shards:
        raise Exception

    for column in query.column_descriptions:
        if column["entity"]:
            shard = column["entity"].get_shard()
            break

    #if query._select_from_entity:
        #shard = query._select_from_entity.class_.get_shard()

    return [shard]


def query_chooser(query):
    shard = BaseModel.get_shard()

    if shard not in shards:
        raise Exception

    for column in query.column_descriptions:
        if column["entity"]:
            shard = column["entity"].get_shard()
            break

    #if query._select_from_entity:
        #shard = query._select_from_entity.class_.get_shard()

    return [shard]


sharded_session = sessionmaker(query_cls=CustomQuery, class_=ShardedSession)

session = scoped_session(sharded_session)

session.configure(
    shards=shards,
    shard_chooser=shard_chooser,
    id_chooser=id_chooser,
    query_chooser=query_chooser,
)
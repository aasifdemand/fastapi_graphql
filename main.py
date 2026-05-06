from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from db.database import engine,Base
from db.models import UserModel
from schema.index import schema

app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

graphql_app = GraphQLRouter(schema)

app.include_router(
    graphql_app,
    prefix="/graphql"
)
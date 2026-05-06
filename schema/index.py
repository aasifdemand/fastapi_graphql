import strawberry

from schema.resolvers.query import Query
from schema.resolvers.mutation import Mutation

schema = strawberry.Schema(
    query=Query,
    mutation=Mutation
)
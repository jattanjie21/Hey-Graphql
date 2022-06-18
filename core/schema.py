import graphene
from recipe import schema

class Query(schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
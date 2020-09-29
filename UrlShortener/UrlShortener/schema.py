import graphene
import Shortener.schema


class Query(Shortener.schema.Query,graphene.ObjectType):
    pass


class Mutation(Shortener.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query,mutation=Mutation)
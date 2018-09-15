import graphene
import graphql_jwt
import apps.rappi.schema

class Query(apps.rappi.schema.Query, graphene.ObjectType):
    pass

class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
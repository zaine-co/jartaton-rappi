import graphene
from graphene_django import DjangoObjectType
from .models import *
#####QUERY
class StorekeepersType(DjangoObjectType):
    class Meta:
        model = Storekeepers

class OrdersType(DjangoObjectType):
    class Meta:
        model = Orders

class Query(graphene.ObjectType):
    storekeepers = graphene.List(StorekeepersType)
    orders = graphene.List(OrdersType)
    storekeeper = graphene.Field(StorekeepersType, id=graphene.Int())

    def resolve_storekeepers(self, info, **kwargs):
        return Storekeepers.objects.using('jartatonP').all()
    
    def resolve_orders(self, info, **kwargs):
        return Orders.objects.using('jartatonM').all()
    
    def resolver_storekeeper(self, info, id=None, **kwargs):
        if id:
            return Storekeepers.objects.using('jartatonP').get(pk=id)
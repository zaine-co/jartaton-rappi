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
    order = graphene.Field(OrdersType, id=graphene.Int())
    storekeepers_vehicle = graphene.List(StorekeepersType, vehicle=graphene.Int())

    def resolve_storekeepers(self, info, **kwargs):
        return Storekeepers.objects.using('jartatonP').all()
    
    def resolve_orders(self, info, **kwargs):
        return Orders.objects.using('jartatonM').all()
    
    def resolve_storekeeper(self, info, id=None, **kwargs):
        if id:
            return Storekeepers.objects.using('jartatonP').get(pk=id)
    
    def resolve_order(self, info, id=None, **kwargs):
        if id:
            return Orders.objects.using('jartatonM').get(pk=id)
    
    def resolve_storekeepers_vehicle(self, info, vehicle=None, **kwargs):
        if vehicle:
            return Storekeepers.objects.using('jartatonP').filter(toolkit__vehicle=vehicle)

#print(Storekeepers.objects.using('jartatonP').filter(toolkit__vehicle=2))
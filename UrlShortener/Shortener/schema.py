import graphene
from graphene_django import DjangoObjectType
from django.db.models import Q
from .models import URL


class URLType(DjangoObjectType):
    class Meta:
        model = URL


class Query(graphene.ObjectType):
    urls = graphene.List(URLType,url=graphene.String(),items=graphene.Int())

    def resolve_urls(self,info,url=None,items=None,**kwargs):
        queryset = URL.objects.all()

        if url:
            _filter = Q(full_url__icontains=url)
            queryset = queryset.filter(_filter)
        if items:
            queryset = queryset[:items]
        return queryset


class CreateURL(graphene.Mutation):
    url = graphene.Field(URLType)

    class Arguments:
        full_url = graphene.String()

    def mutate(self,info,full_url):
        url = URL(full_url=full_url)
        url.save()

        return CreateURL(url=url)

class DeleteUrl(graphene.Mutation):
    # Return Values
    id = graphene.Int()
    url = graphene.String()

    class Arguments:
        id = graphene.ID()

    def mutate(self,info,id):
        obj = URL.objects.get(id=id)
        obj.delete()
        return DeleteUrl(id=id,url=obj.full_url)

class Mutation(graphene.ObjectType):
    create_url = CreateURL.Field()
    delete_url = DeleteUrl.Field()
import graphene
from graphene import ObjectType
from graphene_django import DjangoObjectType
from .models import Recipe


class RecipeType(DjangoObjectType):

    class Meta:
        model = Recipe
        fields = ('dish','description')

class Query(ObjectType):

    all_recipes = graphene.List(RecipeType)

    def resolve_all_recipes(self, info):
        return Recipe.objects.all()
import graphene
from graphene import ObjectType
from graphene_django import DjangoObjectType
from .models import Recipe


class RecipeType(DjangoObjectType):

    class Meta:
        model = Recipe
        fields = ('__all__')

class Query(ObjectType):

    """
    This query returns all the recipes listed in the
    database.
    """
    all_recipes = graphene.List(RecipeType)

    def resolve_all_recipes(self, info):
        return Recipe.objects.all()
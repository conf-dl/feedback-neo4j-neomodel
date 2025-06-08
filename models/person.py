from neomodel import (
    AsyncRelationshipTo,
    AsyncStructuredNode,
    IntegerProperty,
    StringProperty,
)

from .relationship import ActedInRel


class Person(AsyncStructuredNode):
    # Field of the node
    born = IntegerProperty()
    name = StringProperty(required=True)

    # Relationship of the node
    acted_in = AsyncRelationshipTo(".movie.Movie", "ACTED_IN", model=ActedInRel)
    wrote = AsyncRelationshipTo(".movie.Movie", "WROTE")
    directed = AsyncRelationshipTo(".movie.Movie", "DIRECTED")
    produced = AsyncRelationshipTo(".movie.Movie", "PRODUCED")

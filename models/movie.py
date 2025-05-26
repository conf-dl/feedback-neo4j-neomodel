from neomodel import (
    AsyncRelationshipFrom,
    AsyncStructuredNode,
    IntegerProperty,
    StringProperty,
)

from .relationship import ActedInRel, ReviewedRel


class Movie(AsyncStructuredNode):
    # Field of the node
    released = IntegerProperty(required=True)
    tagline = StringProperty(max_lenght=1024)
    title = StringProperty(max_lenght=128, required=True)

    # Relationship of the node
    actors = AsyncRelationshipFrom(".person.Person", "ACTED_IN", model=ActedInRel)
    writers = AsyncRelationshipFrom(".person.Person", "WROTE")
    directers = AsyncRelationshipFrom(".person.Person", "DIRECTED")
    producers = AsyncRelationshipFrom(".person.Person", "PRODUCED")
    reviewers = AsyncRelationshipFrom(".person.Person", "REVIEWED", model=ReviewedRel)

from neomodel import AsyncStructuredRel, ArrayProperty, IntegerProperty, StringProperty


class ActedInRel(AsyncStructuredRel):
    roles = ArrayProperty()


class ReviewedRel(AsyncStructuredRel):
    rating = IntegerProperty()
    summary = StringProperty(max_length=4096)

from neomodel import AsyncStructuredRel, ArrayProperty


class ActedInRel(AsyncStructuredRel):
    roles = ArrayProperty()

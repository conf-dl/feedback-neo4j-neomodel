from os import getenv

from dotenv import load_dotenv
from neomodel import (
    AsyncStructuredNode,
    ArrayProperty,
    BooleanProperty,
    DateProperty,
    IntegerProperty,
    StringProperty,
    AsyncRelationship,
)

load_dotenv()


class MyNode(AsyncStructuredNode):
    # Name of your node
    __label__ = getenv("GITHUB_USER") or getenv("USER")

    # Field of the node
    fullname = StringProperty(required=True)
    adult = BooleanProperty(default=False)
    height = IntegerProperty()
    hobbies = ArrayProperty()
    birthday = DateProperty()

    neighbors_node = AsyncRelationship("MyNode", "NEAREST")

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
    # Field of the node
    name = StringProperty(required=True)
    adult = BooleanProperty(default=False)
    height = IntegerProperty()
    hobbies = ArrayProperty()
    birthday = DateProperty()

    neighbors_node = AsyncRelationship("MyNode", "NEAREST")

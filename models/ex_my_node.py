from os import getenv
from dotenv import load_dotenv

from neomodel import (
    AsyncStructuredNode,
    ArrayProperty,
    BooleanProperty,
    DateProperty,
    IntegerProperty,
    StringProperty,
)

load_dotenv()


class MyNode(AsyncStructuredNode):
    # Name of your node
    __label__ = getenv("GITHUB_USER")

    # Field of the node
    fullname = StringProperty(required=True)
    adult = BooleanProperty(default=False)
    height = IntegerProperty()
    hobbies = ArrayProperty()
    birthday = DateProperty()

from asyncio import run
from os import getenv

from dotenv import load_dotenv
from neo4j.time import DateTime
from neomodel import config

from models.ex_my_node import MyNode
from models.movie import Movie
from models.person import Person

load_dotenv()

config.DATABASE_URL = getenv("NEO4J_URL")


async def get_all_movie() -> list[Movie]:
    return await Movie.nodes.all()


async def get_all_person() -> list[Person]:
    return await Person.nodes.all()


async def get_all_movies_of_actor(actor_name: str) -> list[Movie]:
    if all_movies_acted_in := await Person.nodes.filter(name=actor_name).first():
        return await all_movies_acted_in.acted_in.all()
    else:
        raise ValueError("Please enter a valid actor name")


async def main():
    try:
        # Get all movies
        print("Movies:\n")

        all_movie = await get_all_movie()
        print(f"Number of Movie nodes: {len(all_movie)}\n")

        for i, movie in enumerate(all_movie, start=1):
            print(f"\t{i:2}. {movie.title} | {movie.released}")

        # Get all persons
        print("\n\nPersons:\n")

        all_person = await get_all_person()
        print(f"Number of Person nodes: {len(all_person)}\n")

        for i, person in enumerate(all_person, start=1):
            print(f"\t{i:3}. {person.name} | {person.born or 'N/A'}")

        # Get all movies of an actor
        actor_name = input("\n\nEnter actor name: ")

        try:
            all_movies_of_actor = await get_all_movies_of_actor(actor_name=actor_name)
            print(f"Number of Movie for '{actor_name}': {len(all_movies_of_actor)}\n")

            for i, movie in enumerate(all_movies_of_actor, start=1):
                print(f"\t{i}. {movie.title} | {movie.released}")
        except ValueError:
            print("\n /!\\ Invalid actor name /!\\")

        # Your tests
        my_name = getenv("NAME")
        print(f"\n\nMy node: {my_name}\n")

        adult = True
        height = 170
        hobbies = ["Python", "Neo4j"]
        birthdate = DateTime(year=1970, month=1, day=1)

        if (my_node := await MyNode.nodes.get_or_none(name=my_name)) is None:
            my_node = await MyNode(
                name=my_name,
                adult=adult,
                height=height,
                hobbies=hobbies,
                birthdate=birthdate,
            ).save()

        # my_node = await MyNode.nodes.filter(name=my_name).first()
        birth = birthdate.year_month_day
        print(
            f"My name: {my_node.name}, height: {my_node.height}, hobbies: {', '.join(my_node.hobbies)}, birthdate: {birth[2]}/{birth[1]}/{birth[0]}"
        )

        neighbor_name = input("\n\nEnter neighbor name: ")
        if (neighbor := await MyNode.nodes.get_or_none(name=neighbor_name)) is None:
            neighbor = await MyNode(
                name=neighbor_name,
                adult=True,
                height=180,
                hobbies=[
                    "Python",
                    "Movie",
                ],
                birthdate=DateTime(year=1970, month=1, day=2),
            ).save()

        await my_node.neighbors_node.connect(neighbor)

    except Exception as e:
        print(f"Error during Neo4j operations: {e}")


if __name__ == "__main__":
    try:
        run(main())
    except Exception as e:
        print(f"Unexpected error: {e}")

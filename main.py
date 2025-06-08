from asyncio import run
from os import getenv

from dotenv import load_dotenv
from neomodel import config

from models.movie import Movie
from models.person import Person

load_dotenv()

config.DATABASE_URL = getenv("NEO4J_URL")


async def get_all_person():
    return await Person.nodes.all()


async def get_all_movie():
    return await Movie.nodes.all()


async def get_all_movies_of_actor(actor_name: str):
    if all_movies_acted_in := await Person.nodes.filter(name=actor_name).first():
        return await all_movies_acted_in.acted_in.all()
    else:
        raise ValueError("Please enter a valid actor name")


async def main():
    try:
        # Get all persons
        print("Persons:\n")

        all_person = await get_all_person()
        print(f"Number of Person nodes: {len(all_person)}\n")

        for i, person in enumerate(all_person, start=1):
            print(f"\t{i:3}. {person.name} | {person.born or 'N/A'}")

        # Get all movies
        print("\n\nMovies:\n")

        all_movie = await get_all_movie()
        print(f"Number of Movie nodes: {len(all_movie)}\n")

        for i, movie in enumerate(all_movie, start=1):
            print(f"\t{i:2}. {movie.title} | {movie.released}")

        # Get all movies of an actor
        actor_name = input("\n\nEnter actor name: ")

        try:
            all_movies_of_actor = await get_all_movies_of_actor(actor_name=actor_name)
            print(f"Number of Movie for '{actor_name}': {len(all_movies_of_actor)}\n")

            for i, movie in enumerate(all_movies_of_actor, start=1):
                print(f"\t{i}. {movie.title} | {movie.released}")
        except ValueError:
            print("\n /!\\ Invalid actor name /!\\")

    except Exception as e:
        print(f"Error during Neo4j operations: {e}")


if __name__ == "__main__":
    try:
        run(main())
    except Exception as e:
        print(f"Unexpected error: {e}")

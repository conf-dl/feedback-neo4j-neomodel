from asyncio import get_event_loop, run
from os import getenv

from dotenv import load_dotenv
from neomodel import config

from models.movie import Movie
from models.person import Person

load_dotenv()

config.DATABASE_URL = getenv("NEO4J_URL")


async def get_all_person():
    print(f"Number of Person nodes: {await Person.nodes.get_len()}")
    return await Person.nodes.filter().all()


async def get_all_movie():
    print(f"Number of Movie nodes: {await Movie.nodes.get_len()}")
    return await Movie.nodes.filter().all()


async def main():
    try:
        # Get all persons
        print("Person:\n")
        all_person = await get_all_person()
        for i, person in enumerate(all_person, start=1):
            print(f"\t{i}. {person.name} | {person.born}")

        # Get all movies
        print("\n\nMovie:\n")
        all_movie = await get_all_movie()
        for i, movie in enumerate(all_movie, start=1):
            print(f"\t{i}. {movie.title} | {movie.released}")

        return all_person, all_movie
    except Exception as e:
        print(f"Error during Neo4j operations: {e}")

        return [], []


if __name__ == "__main__":
    try:
        persons, movies = run(main())
    except RuntimeError as e:
        print(f"Asyncio runtime error: {e}")
        loop = get_event_loop()
        persons, movies = loop.run_until_complete(main())
    except Exception as e:
        print(f"Unexpected error: {e}")

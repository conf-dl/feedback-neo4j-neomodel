from asyncio import run
from os import getenv

from dotenv import load_dotenv
from neomodel import adb, config

from models import Movie, Person

load_dotenv()

config.DATABASE_URL = getenv("NEO4J_URL")


async def create_relationships():
    query = """
    MATCH (p:Person)-[r:ACTED_IN|WROTE|DIRECTED|PRODUCED]->(m:Movie)
    RETURN id(p), type(r), id(m)
    """
    results, meta = await adb.cypher_query(query)

    for result in results:
        person_id, rel_type, movie_id = result

        person_query = f"MATCH (p:Person) WHERE id(p) = {person_id} RETURN p"
        movie_query = f"MATCH (m:Movie) WHERE id(m) = {movie_id} RETURN m"

        person_results, _ = await adb.cypher_query(person_query)
        movie_results, _ = await adb.cypher_query(movie_query)

        person_node = person_results[0][0]
        movie_node = movie_results[0][0]

        person = Person.inflate(person_node)
        movie = Movie.inflate(movie_node)

        if person and movie:
            if rel_type == "ACTED_IN":
                await person.acted_in.connect(movie)
            elif rel_type == "WROTE":
                await person.wrote.connect(movie)
            elif rel_type == "DIRECTED":
                await person.directed.connect(movie)
            elif rel_type == "PRODUCED":
                await person.produced.connect(movie)


if __name__ == "__main__":
    run(create_relationships())

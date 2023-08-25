import strawberry
import typing # 코드에 type annotation(주석)을 추가하게 해줍니다.


@strawberry.type
class Movie:
    pk: int
    title: str
    year: int
    rating: int


movies_db = [
    Movie(pk=1, title="Godfather", year=1990, rating=10),
]


@strawberry.type
class Query:
    @strawberry.field
    def movies(self) -> typing.List[Movie]: # Movie 리스트 타입
        return movies_db

    @strawberry.field
    def movie(self, movie_pk: int) -> Movie:
        return movies_db[movie_pk - 1]


schema = strawberry.Schema(query=Query)
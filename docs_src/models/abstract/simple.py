import mongoz

database_uri = "mongodb://localhost:27017"
registry = mongoz.Registry(database_uri)


class BaseModel(mongoz.Document):
    class Meta:
        abstract = True
        registry = registry

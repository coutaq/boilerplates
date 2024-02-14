from attr import field
from peewee import *
import datetime
from marshmallow import Schema, fields
from playhouse.shortcuts import ReconnectMixin


class ReconnectMySQLDatabase(ReconnectMixin, MySQLDatabase):
    pass


db = ReconnectMySQLDatabase("database", host="localhost", user="root", password="")


class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    id = AutoField()
    email = TextField()
    name = TextField()
    password = TextField()
    token = TextField(null=True)
    created_at = DateTimeField(default=datetime.datetime.now)


class UserSchema(Schema):
    email = fields.String()
    name = fields.String()
    created_at = fields.DateTime()


if __name__ == "__main__":
    tables = [User]
    db.drop_tables(tables)
    db.create_tables(tables)

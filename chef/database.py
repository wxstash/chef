import os

from mongoengine import *

# Model/Schema definitions

class Users(Document):
    email = StringField(required=True)
    username = StringField(required=True, max_length=24)
    password = StringField(required=True)
    user_type = StringField()
    user_id = StringField()
    auth_token = StringField()

# Management
def start():
    try:
        MONGODB_URI = os.getenv('MONGODB_URI')
    except:
        print('\nMongoDB Config not set\n')
        raise

    connect('chef', alias='default', host=MONGODB_URI)

if __name__ == "__main__":
    start()    

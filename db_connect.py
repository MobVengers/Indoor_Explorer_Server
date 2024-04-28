import mongoengine as me
# import certifi
import os


def initialize_db(db_user, db_pass):
    
    connection_string = f"mongodb+srv://{db_user}:{db_pass}@localization.wyqcqe0.mongodb.net/localization-data?retryWrites=true&w=majority"

    try:
        # me.connect(host=connection_string, tlsCAFile=certifi.where())
        me.connect(host=connection_string)
        print("## Connected to database")
    except Exception as e:
        print(f"Error connecting to database: {e}")
    



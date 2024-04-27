# db.py
import mongoengine as me

# TODO: env file
connection_string = "mongodb+srv://admin:admin@localization.wyqcqe0.mongodb.net/localization-data?retryWrites=true&w=majority"

def initialize_db():
    try:
        me.connect(host=connection_string)
        print("## Connected to database")
    except Exception as e:
        print(f"Error connecting to database: {e}")
    


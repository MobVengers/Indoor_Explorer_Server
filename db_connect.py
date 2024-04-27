import mongoengine as me
# import certifi
import os

# Now you can access environment variables
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASSWORD")

connection_string = f"mongodb+srv://{db_user}:{db_pass}@localization.wyqcqe0.mongodb.net/localization-data?retryWrites=true&w=majority"

def initialize_db():
    try:
        # me.connect(host=connection_string, tlsCAFile=certifi.where())
        me.connect(host=connection_string)
        print("## Connected to database")
    except Exception as e:
        print(f"Error connecting to database: {e}")
    



# db.py
import mongoengine as me

# TODO: env file
connection_string = "mongodb+srv://admin:admin@localization.wyqcqe0.mongodb.net/localization-data?retryWrites=true&w=majority"
me.connect(host=connection_string)

print("Connected to database")


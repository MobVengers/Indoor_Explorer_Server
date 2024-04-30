import mongoengine as me

class AdminKey(me.Document):
    hashkey = me.StringField(required=True)
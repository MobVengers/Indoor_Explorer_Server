import mongoengine as me

class Position(me.EmbeddedDocument):
    x = me.FloatField(required=True)
    y = me.FloatField(required=True)
    floor = me.FloatField(required=True)

class CalibrationPoint(me.Document):
    projectid = me.StringField(required=True)
    name = me.StringField(required=True)
    radiomap = me.MapField(field=me.FloatField())  # Map of float values
    position = me.EmbeddedDocumentField(Position, required=True)
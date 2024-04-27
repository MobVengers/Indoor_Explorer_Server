import mongoengine as me
import datetime

class CalibrationFingerprint(me.Document):
    id = me.StringField(required=True)
    projectId = me.StringField(required=True)
    calibrationPointId = me.StringField(required=True)
    radioMap = me.MapField(field=me.FloatField())
    created_at = me.DateTimeField(default=datetime.datetime.now)
    updated_at = me.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return f"CalibrationFingerprint(id={self.id}, projectId={self.projectId})"
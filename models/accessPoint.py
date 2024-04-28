import mongoengine as me
import datetime

class AccessPoint(me.Document):
    projectid = me.StringField(required=True)
    ssid = me.StringField(required=True)
    bssid = me.StringField(required=True)
    created_at = me.DateTimeField(default=datetime.datetime.now)
    updated_at = me.DateTimeField(default=datetime.datetime.now)
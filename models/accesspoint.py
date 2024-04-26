import mongoengine as me

class AccessPoint(me.Document):
    projectId = me.StringField(required=True)
    ssid = me.StringField(required=True)
    bssid = me.StringField(required=True)
    created_at = me.DateTimeField(default=me.datetime.utcnow)
    updated_at = me.DateTimeField(default=me.datetime.utcnow)

    def __str__(self):
        return f"{self.ssid} ({self.bssid})"
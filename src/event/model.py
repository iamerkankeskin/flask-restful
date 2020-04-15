from backend.src.common.main import db, ma


class Event(db.Model):
    __table_args__ = {"schema": "content"}
    event_id = db.Column(db.BigInteger, autoincrement=True, primary_key=True)
    event_name = db.Column(db.String(200), nullable=False)
    event_slug = db.Column(db.String(255), nullable=False)
    event_summary = db.Column(db.Text)
    event_content = db.Column(db.Text)
    event_meta_title = db.Column(db.String(170))
    event_meta_keyword = db.Column(db.String(170))
    event_meta_description = db.Column(db.String(170))
    event_created = db.Column(db.DateTime)
    event_modified = db.Column(db.DateTime)
    event_status = db.Column(db.Integer)


class EventSchema(ma.ModelSchema):
    class Meta:
        model = Event

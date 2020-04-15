from backend.src.common.main import *
from backend.src.event.model import Event, EventSchema


class EventDao():

    @staticmethod
    def all():
        events = Event.query.all()
        schema = EventSchema(many=True)
        result = schema.dump(events)
        return jsonify({"result": result})

    @staticmethod
    def get(event_id):
        event_row = Event.query.get(event_id)
        schema = EventSchema()
        result = schema.dump(event_row)
        return jsonify({"result": result})

    @staticmethod
    def delete(event_id):
        event = Event.query.filter_by(event_id=event_id).first()
        db.session.delete(event)
        db.session.commit()
        return jsonify({"result": True})

    @staticmethod
    def update(event_id, data):
        event = Event.query.get(event_id)
        event.event_name = data[0]
        event.event_slug = data[1]
        event.event_summary = data[2]
        event.event_content = data[3]
        event.event_meta_title = data[4]
        event.event_meta_keyword = data[5]
        event.event_meta_description = data[6]
        event.event_created = data[7]
        event.event_modified = data[8]
        event.event_status = data[9]
        db.session.commit()

        return jsonify({"result": True})

    @staticmethod
    def add(data):
        new_event = Event(event_name=data[0], event_slug=data[1], event_summary=data[2],
                          event_content=data[3], event_meta_title=data[4],
                          event_meta_keyword=data[5], event_meta_description=data[6],
                          event_created=data[7], event_modified=data[8], event_status=data[9])

        db.session.add(new_event)
        db.session.commit()
        return jsonify({"result": True})

    @staticmethod
    def check_if_slug(event_slug):
        result = Event.query.filter_by(event_slug=event_slug).first()
        return result


event_dao = EventDao()

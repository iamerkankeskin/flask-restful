from backend.src.common.main import *
from backend.src.event.dao import event_dao
import datetime


class EventService:

    @staticmethod
    def all():
        return event_dao.all()

    @staticmethod
    def get(event_id):
        if not event_id.isnumeric():
            return jsonify({"result": "error", "message": "ID hatalı"})

        return event_dao.get(event_id)

    @staticmethod
    def delete(event_id):
        if not event_id.isnumeric():
            return jsonify({"result": "error", "message": "ID hatalı"})

        return event_dao.delete(event_id)

    @staticmethod
    def update(event_id):
        event_name = request.form.get("event_name")
        event_slug = request.form.get("event_slug")
        event_summary = request.form.get("event_summary")
        event_content = request.form.get("event_content")
        event_meta_title = request.form.get("event_meta_title")
        event_meta_keyword = request.form.get("event_meta_keyword")
        event_meta_description = request.form.get("event_meta_description")
        event_created = datetime.datetime.utcnow()
        event_modified = datetime.datetime.utcnow()
        event_status = 1

        if event_name == "" or event_name is None:
            return jsonify({"result": "error", "message": "Etkinlik adı yazmalısınız"})

        data = [event_name, event_slug, event_summary, event_content, event_meta_title,
                event_meta_keyword,
                event_meta_description, event_created, event_modified, event_status]

        return event_dao.update(event_id, data)

    @staticmethod
    def add():

        event_name = request.form.get("event_name")
        event_slug = request.form.get("event_slug")
        event_summary = request.form.get("event_summary")
        event_content = request.form.get("event_content")
        event_meta_title = request.form.get("event_meta_title")
        event_meta_keyword = request.form.get("event_meta_keyword")
        event_meta_description = request.form.get("event_meta_description")
        event_created = datetime.datetime.utcnow()
        event_modified = datetime.datetime.utcnow()
        event_status = 1

        if event_name is None:
            return jsonify({"result": "error", "message": "Etkinlik adı yazmalısınız"})

        if EventService.check_if_slug(event_slug) is not None:
            return jsonify({"result": "error", "message": "Bu etkinlik daha önce eklenmiştir!"})

        data = [event_name, event_slug, event_summary, event_content, event_meta_title,
                event_meta_keyword,
                event_meta_description, event_created, event_modified, event_status]

        return event_dao.add(data)

    @staticmethod
    def check_if_slug(slug):
        return event_dao.check_if_slug(slug)


event_service = EventService()

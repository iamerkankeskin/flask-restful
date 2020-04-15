from backend.src.common.main import *
from backend.src.event.service import event_service


@app.route(api_path + "/events", methods=['GET'])
def index():
    return event_service.all()


@app.route(api_path + "/event/<event_id>", methods=['GET'])
def get(event_id):
    return event_service.get(event_id)


@app.route(api_path + "/event/<event_id>", methods=['DELETE'])
def delete(event_id):
    return event_service.delete(event_id)


@app.route(api_path + "/event/<event_id>", methods=['PUT'])
def update(event_id):
    return event_service.update(event_id)


@app.route(api_path + "/event", methods=['POST'])
def add():
    return event_service.add()


if __name__ == '__main__':
    app.run(debug=True)

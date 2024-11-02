from flask import request, jsonify
from models import Content, Booking

def setup_routes(app, db):
    
    @app.route('/content', methods=['POST'])
    def add_content():
        data = request.json
        content = Content(title=data['title'], body=data['body'], media_url=data.get('media_url'))
        db.session.add(content)
        db.session.commit()
        return jsonify({"message": "Content added!"})

    @app.route('/content', methods=['GET'])
    def get_content():
        contents = Content.query.all()
        return jsonify([{
            "id": content.id,
            "title": content.title,
            "body": content.body,
            "media_url": content.media_url
        } for content in contents])

    @app.route('/book', methods=['POST'])
    def book():
        data = request.json
        booking = Booking(name=data['name'], email=data['email'], booking_time=data['booking_time'])
        db.session.add(booking)
        db.session.commit()
        return jsonify({"message": "Booking successful!"})

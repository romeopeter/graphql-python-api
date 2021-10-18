from app import db
from datetime import datetime


class Post(db.Model):
    """Post database model"""

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.Date(), default=datetime.now)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "created_at": str(self.created_at.strftime("%d-%m-%Y")),
        }

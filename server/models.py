from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('name')
    def validate_name(self, key, name):
        if not name:
            raise ValueError("Author must have name attribute")
        return name

    @validates('phone_number')
    def validate_number(self, key, number):
       if len(number) != 10:
           raise ValueError("Phone number must be 10 digists")
       return number


    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('content')
    def validates_content_length(self, key, content):
        if len(content) <= 250:
            raise ValueError("Post Content must be at least 250 characters long.")
        return content
    
    @validates('summary')
    def validates_summary_length(self, key, summary):
        if len(summary) >= 250:
            raise ValueError("Post summary cannot exceed 250 characters.")
        return summary

    @validates('category')
    def validates_category(self, key, category):
        categories = ["Fiction", "Non-Fiction"]
        if category not in categories:
            raise ValueError("Category must be either Fiction or Non-Fiction")
        return category
    
    @validates('title')
    def clickbait(self, key, title):
        clickbait = ["Won't Believe", "Secret", "Top", "Guess"]
        if not any(substring in title for substring in clickbait):
            raise ValueError("No clickbait found")
        return title

    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'

from datetime import date
from app import db
from app.models import Post
from ariadne import convert_kwargs_to_snake_case


def listPosts_resolver(obj, info):
    """
    Resolver method to fetch all posts
    """

    try:
        posts = [post.to_dict() for post in Post.query.all()]
        payload = {"success": True, "post": posts}
    except Exception as error:
        payload = {"success": False, "errors": [str(error)]}

    return payload


@convert_kwargs_to_snake_case
def getPost_resolver(obj, info, id):
    """
    Resolver method to fetch single post
    """

    try:
        post = Post.query.get(id)
        payload = {"success": True, "post": post}
    except AttributeError as error:
        payload = {"success": False, "errors": [f"Post item matching {id} not found"]}

    return payload


@convert_kwargs_to_snake_case
def createPost_resolver(obj, info, title, description):
    """
    Resolver method to create new post
    """

    try:

        todays_date = date.today()
        post = Post(
            title=title,
            description=description,
            created_at=todays_date.strftime("%b-%d-%y"),
        )

        db.session.add(post)
        db.session.commit()

        payload = {"success": True, "post": post.to_dict()}
    except ValueError as error:
        payload = {"success": False, "errors": [str(error)]}

    return payload


@convert_kwargs_to_snake_case
def updatePost_resolver(obj, info, id, title, description):
    """
    Resolver method to update new post
    """

    try:
        post = Post.query.get(id)

        if post:
            post.title = title
            post.description = description

        db.session.add(post)
        db.session.commit()

        payload = {"success": True, "post": post.to_dict()}
    except AttributeError as error:
        payload = {"success": False, "errors": [str(error)]}

    return payload


@convert_kwargs_to_snake_case
def deletePost_resolver(obj, info, id):
    """
    Resolver method to update new post
    """

    try:
        post = Post.query.get(id)

        db.session.delete(post)
        db.session.commit()

        payload = {"success": True, "post": post.to_dict()}
    except AttributeError as error:
        payload = {"success": False, "errors": [str(error)]}

    return payload

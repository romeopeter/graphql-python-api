from app.models import Post
from ariadne import convert_kwargs_to_snake_case


def listPosts_resolver(obj, info):
    """
	Resolver method to fetch all posts from DB
	"""

    try:
        posts = [post.to_dict() for post in Post.query.all()]
        payload = {"success": True, "post": posts}
    except Exception as error:
        payload = {"success": False, "errors": [str(error)]}

    return payload


@convert_kwargs_to_snake_case
def getPost_resolver(obj, info, id):
    try:
        post = Post.query.get(id)
        payload = {"success": True, "post": post}
    except Exception as error:
        payload = {"success": False, "errors": [f"Post item matching {id} not found"]}

    return payload

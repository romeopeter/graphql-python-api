from app import server
from flask import request, jsonify
from ariadne import (
    load_schema_from_path,
    make_executable_schema,
    graphql_sync,
    snake_case_fallback_resolvers,
    ObjectType,
)
from ariadne.constants import PLAYGROUND_HTML
from app.api_resolvers import (
    listPosts_resolver,
    getPost_resolver,
    createPost_resolver,
    updatePost_resolver,
    deletePost_resolver,
)

# Query types
query = ObjectType("Query")
query.set_field("listPosts", listPosts_resolver)
query.set_field("getPost", getPost_resolver)

# Mutation types
query = ObjectType("Mutation")
query.set_field("createPost", createPost_resolver)
query.set_field("updatePost", updatePost_resolver)
query.set_field("deletePost", deletePost_resolver)


graphql_type_defs = load_schema_from_path("app/schema.graphql")
schema = make_executable_schema(graphql_type_defs, query, snake_case_fallback_resolvers)


@server.route("/")
def hello():
    return "<h1>Hello there!</h1>"


@server.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200


@server.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema, data, context_value=request, debug=server.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code

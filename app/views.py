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


graphql_type_defs = load_schema_from_path("app/schema.graphql")
schema = make_executable_schema(graphql_type_defs, snake_case_fallback_resolvers)


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
        schema, data, context_valu=request, debug=server.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code

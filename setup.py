from setuptools import setup


set(
    name="graphql-python-api",
    packages=["app"],
    include_package_data=True,
    install_requires=[
        "flask",
        "flask-sqlalchemy",
        "ariadne",
        "flask-cors",
        "python-dotenv",
    ],
)

from flask import Flask, redirect, flash

from .api.routes import api
from .site.routes import site

app = Flask(
    "myapp",
)

# register blueprints
app.register_blueprint(api)
app.register_blueprint(site)


# show url_map
print(app.url_map)



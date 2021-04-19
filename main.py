from conf.wsgi import application

# App Engine by default looks for a main.py file at the root of the tracker
# directory with a WSGI-compatible object called tracker.
# This file imports the WSGI-compatible object of your Django tracker,
# application from mysite/wsgi.py and renames it tracker so it is discoverable by
# App Engine without additional configuration.
# Alternatively, you can add a custom entrypoint field in your tracker.yaml:
# entrypoint: gunicorn -b :$PORT mysite.wsgi

app = application
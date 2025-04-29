import gunicorn

gunicorn.SERVER_SOFTWARE = 'simple'

# Debug
debug = False
spew = False

# Process
bind = '0.0.0.0:3000'
backlog = 2048

# Workers
workers = 1
worker_class = 'gevent'
worker_connections = 100
timeout = 120
keepalive = 2

# Logging
loglevel = 'INFO'

preload_app = False

# Server hooks
def post_fork(server, worker):
    server.log.info("Worker spawned (pid: %s)", worker.pid)

def pre_fork(server, worker):
    pass

def pre_exec(server):
    server.log.info("Forked child, re-executing.")

def when_ready(server):
    server.log.info("Server is ready. Spwawning workers")

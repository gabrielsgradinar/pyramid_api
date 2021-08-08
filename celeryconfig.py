
broker_url = "redis://localhost:6379/0"
result_backend = 'db+sqlite:///results.db'

imports = [
    "pyramid_api.tasks"
]
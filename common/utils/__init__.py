from os import environ

def get_env_var(key):
    try:
        return environ[key]
    except KeyError:
        raise NameError(f"Missing {key} environment variable.")

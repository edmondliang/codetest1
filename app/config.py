import os


class DefaultConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    URL_REGISTER_USERS = os.environ.get('URL_REGISTER_USERS')
    URL_UNREGISTER_USERS = os.environ.get('URL_UNREGISTER_USERS')
    URL_PROJECT_MEMBERSHIPS = os.environ.get('URL_PROJECT_MEMBERSHIPS')


def get_config(name="default"):

    mapping = dict(
        default=DefaultConfig
    )

    return mapping.get(name)

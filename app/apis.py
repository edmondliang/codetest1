
from functools import lru_cache
import requests
from .config import get_config
from .schemas import (RegisterUserSchema, UnregisterUserSchema,
                      ProjectMembershipSchema)


class APIS:

    def __init__(self):
        self.cfg = get_config()

    @lru_cache(maxsize=32)
    def get_register_users(self):
        r = requests.get(self.cfg.URL_REGISTER_USERS)
        r.raise_for_status()
        result = r.json()
        return RegisterUserSchema(many=True).load(result)

    @lru_cache(maxsize=32)
    def get_unregister_users(self):
        r = requests.get(self.cfg.URL_UNREGISTER_USERS)
        r.raise_for_status()
        result = r.json()
        return UnregisterUserSchema(many=True).load(result)

    @lru_cache(maxsize=32)
    def get_project_memberships(self):
        r = requests.get(self.cfg.URL_PROJECT_MEMBERSHIPS)
        r.raise_for_status()
        result = r.json()
        return ProjectMembershipSchema(many=True).load(result)

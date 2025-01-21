from enum import Enum


class RoleUser(str, Enum):
    normal = "normal"
    admin = "admin"
    superuser = "superuser"

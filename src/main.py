from apps.auth.models import base
from apps.main_settings.models import base as m_base
from fastapi import FastAPI

from .postgres_alchemy import engine

# create fast api instance
app = FastAPI()

base.metadata.create_all(engine)
m_base.metadata.create_all(engine)

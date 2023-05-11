from victory.settings import settings

from .postgresql import Postgresql

postgresql = Postgresql(uri=str(settings.db_url))

from typing import ClassVar
from django.core.exceptions import ImproperlyConfigured
from pydantic import BaseModel

class DjaggerConfig(BaseModel):
    """Djagger configuration schema"""
    global_prefix: ClassVar[str] = ""

try:
    from django.conf import settings
    djagger_config = DjaggerConfig.parse_obj(settings.DJAGGER_CONFIG)

except (ImproperlyConfigured, AttributeError):
    djagger_config = DjaggerConfig()

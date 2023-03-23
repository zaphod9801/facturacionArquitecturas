import datetime
from tortoise import fields

class AuditMixin():
    created_at = fields.DatetimeField(null=False, auto_now_add=True, generated=True, default=datetime.datetime.now())

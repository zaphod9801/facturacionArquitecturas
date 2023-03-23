from typing import Any
from uuid import uuid4
from facturacion_back.models.TransaccionType import TransaccionType
from facturacion_back.models.mixins.AuditMixin import AuditMixin

from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator
from pydantic import BaseModel


class Transaccion(AuditMixin, models.Model):

    id = fields.UUIDField(pk=True, default=uuid4, index=True)
    type = fields.CharEnumField(TransaccionType, null=False)
    value = fields.FloatField(null=False)
    detalles = fields.TextField(null=False)
    cliente = fields.CharField(null=False, max_length=30)


class Transaccion_Pydantic(BaseModel):
    id: Any
    type: TransaccionType
    value: float
    detalles: str
    cliente: str
    created_at: Any


class TransaccionIn_Pydantic(BaseModel):
    type: TransaccionType
    value: float
    detalles: str
    cliente: str

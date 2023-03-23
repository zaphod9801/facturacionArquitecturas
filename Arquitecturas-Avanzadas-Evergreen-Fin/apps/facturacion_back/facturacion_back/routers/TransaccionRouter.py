from fastapi_crudrouter import TortoiseCRUDRouter
from facturacion_back.models.Transaccion import Transaccion, Transaccion_Pydantic, TransaccionIn_Pydantic


print(Transaccion_Pydantic.schema_json(indent=2))

TransaccionRouter = TortoiseCRUDRouter(
    schema=Transaccion_Pydantic,
    create_schema=TransaccionIn_Pydantic,
    db_model=Transaccion,
    prefix='transacciones'
)

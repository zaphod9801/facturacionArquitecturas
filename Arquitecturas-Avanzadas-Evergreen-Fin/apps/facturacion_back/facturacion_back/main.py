from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
# Import all models so Tortoise registers them
import facturacion_back.models as models

from facturacion_back.routers.TransaccionRouter import TransaccionRouter

app = FastAPI()

register_tortoise(
    app,
    db_url="sqlite://memory:",
    modules={
        "models": [models]
    },
    generate_schemas=True,
    add_exception_handlers=True
)

# Add routers
app.include_router(TransaccionRouter)

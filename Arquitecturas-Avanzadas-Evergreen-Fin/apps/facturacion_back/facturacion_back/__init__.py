import uvicorn

def start():
    uvicorn.run('facturacion_back.main:app', port=3000)
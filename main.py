import uvicorn

from src.di import container_general

if __name__ == '__main__':
    uvicorn.run(
        container_general.app,
        host=container_general.config.service.host,
        port=container_general.config.service.port,
    )

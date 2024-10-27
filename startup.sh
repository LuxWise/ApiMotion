#!/usr/bin/env bash
# Ejecutar build.sh
./build.sh

# Iniciar la aplicación con Gunicorn
python -m gunicorn motionapi.asgi:application -k uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000

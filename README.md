# Proyecto  de Práctica API REST en Django - CRUD 

Este proyecto es una API REST desarrollada en Django, diseñada para proporcionar información mediante operaciones CRUD (Crear, Leer, Actualizar, Borrar). Este backend es parte de un ejercicio académico para aprender a crear y desplegar una API en un entorno de producción en Azure.

## Objetivo

La API tiene el objetivo de manejar datos de forma estructurada a través de endpoints seguros y eficientes. El proyecto busca profundizar en las tecnologías de backend, desde la estructura de la base de datos hasta la optimización en el despliegue.

## Requisitos

Las principales librerías que utiliza el proyecto se listan a continuación. Estas deben instalarse usando el archivo `requirements.txt`:

- **asgiref==3.8.1** - Para soporte de ASGI en Django.
- **Brotli==1.1.0** - Para compresión Brotli, útil para reducir el tamaño de los archivos.
- **dj-database-url==2.3.0** - Facilita la configuración de la base de datos mediante URL.
- **Django==5.0.1** - Framework principal de desarrollo.
- **django-cors-headers==4.5.0** - Gestiona los permisos CORS en Django.
- **djangorestframework==3.15.2** - Framework REST para el manejo de la API.
- **gunicorn==23.0.0** - Servidor WSGI para la producción.
- **psycopg2-binary==2.9.10** - Adaptador de PostgreSQL.
- **uvicorn==0.32.0** - Servidor ASGI.
- **whitenoise==6.7.0** - Ayuda a servir archivos estáticos en producción.

El archivo `requirements.txt` contiene todas las dependencias necesarias para la ejecución del proyecto.

## Archivos del Proyecto

- **startup.sh**: Script de inicio para el despliegue en Azure.
- **build.sh**: Script de construcción que instala dependencias, maneja archivos estáticos y aplica migraciones de la base de datos.
- **requirements.txt**: Lista de dependencias del proyecto.

## Configuración y Despliegue en Azure

### Archivo `build.sh`

Este archivo contiene comandos esenciales para preparar el entorno de producción. Realiza las siguientes acciones:

```bash
#!/usr/bin/env bash
# Termina si hay algún error
set -o errexit

# Instala las dependencias
pip install -r requirements.txt

# Colecta archivos estáticos para producción
python manage.py collectstatic --no-input

# Aplica las migraciones pendientes a la base de datos
python manage.py migrate
```

### Archivo `startup.sh`

Este archivo realiza las siguientes acciones:

```bash
#!/usr/bin/env bash
# Ejecutar build.sh
./build.sh

# Iniciar la aplicación con Gunicorn
python -m gunicorn motionapi.asgi:application -k uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000
```

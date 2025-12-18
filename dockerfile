# Usamos una imagen oficial de Python 3.11
FROM python:3.11-slim

# Evita que Python genere archivos .pyc y asegura que los logs se vean al instante
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# --- Instalación de dependencias del sistema ---
# Se instalan las librerías necesarias para compilar el cliente de MySQL (mysqlclient)
RUN apt-get update && apt-get install -y \
    pkg-config \
    default-libmysqlclient-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Instalación de dependencias de Python aprovechando la caché de capas
COPY requirements.txt /app/
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copiamos el código fuente al contenedor
COPY . /app/

# Exponemos el puerto 8000 (puerto interno del contenedor)
EXPOSE 8000

# Comando de inicio: lanzamos el servidor de Django escuchando en todas las interfaces
CMD ["python", "mymicroservice/manage.py", "runserver", "0.0.0.0:8000"]
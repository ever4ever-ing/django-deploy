# Usa una imagen base de Python
FROM python:3.11-slim

# Establece variables de entorno
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Establece el directorio de trabajo
WORKDIR /app

# Instala dependencias del sistema
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copia los archivos de dependencias
COPY requeriments.txt .

# Instala las dependencias de Python
RUN pip install --upgrade pip && \
    pip install -r requeriments.txt && \
    pip install gunicorn

# Copia el proyecto
COPY . .

# Crea directorios necesarios
RUN mkdir -p staticfiles

# Recolecta archivos estáticos
RUN python manage.py collectstatic --noinput || true

# Expone el puerto 8000
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "project.wsgi:application"]

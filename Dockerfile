# Usa una imagen base de Python
FROM python:3.12-slim

# Evita que Python genere archivos .pyc y bufferice la salida
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Directorio de trabajo
WORKDIR /app

# Copia e instala dependencias
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copia el código completo
COPY . /app/

# Ejecuta collectstatic
RUN python manage.py collectstatic --noinput

# Expone el puerto (Cloud Run define la variable $PORT, habitualmente 8080)
EXPOSE ${PORT}

# Ejecuta la aplicación
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "backend.wsgi:application"]

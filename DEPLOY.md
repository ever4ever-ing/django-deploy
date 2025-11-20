# Guía de Despliegue en DigitalOcean

## Preparación Local

### 1. Construir y probar el Docker localmente (opcional)
```bash
docker build -t django-app .
docker run -p 8000:8000 django-app
```

## Despliegue en DigitalOcean

### Opción 1: App Platform (Recomendado - Más fácil)

1. **Sube tu código a GitHub** (ya lo tienes hecho ✓)

2. **Crea una App en DigitalOcean:**
   - Ve a https://cloud.digitalocean.com/apps
   - Click en "Create App"
   - Conecta tu repositorio GitHub: `ever4ever-ing/django-deploy`
   - DigitalOcean detectará automáticamente el Dockerfile

3. **Configura las variables de entorno:**
   - En la sección "Environment Variables" agrega:
     ```
     SECRET_KEY=genera-una-clave-secreta-segura-aqui
     DEBUG=False
     ALLOWED_HOSTS=tu-app.ondigitalocean.app
     ```

4. **Configura el plan:**
   - Selecciona el plan Basic (desde $5/mes)
   - Click en "Launch App"

5. **Espera el despliegue:**
   - DigitalOcean construirá y desplegará automáticamente
   - Te dará una URL como: `https://tu-app.ondigitalocean.app`

### Opción 2: Droplet con Docker

1. **Crea un Droplet:**
   - Tamaño: Basic ($6/mes mínimo)
   - Imagen: Ubuntu 22.04 LTS con Docker preinstalado

2. **Conéctate por SSH:**
   ```bash
   ssh root@tu-droplet-ip
   ```

3. **Clona tu repositorio:**
   ```bash
   git clone https://github.com/ever4ever-ing/django-deploy.git
   cd django-deploy
   ```

4. **Crea el archivo .env:**
   ```bash
   nano .env
   ```
   
   Agrega:
   ```
   SECRET_KEY=tu-clave-secreta-super-segura
   DEBUG=False
   ALLOWED_HOSTS=tu-ip-del-droplet
   ```

5. **Construye y ejecuta:**
   ```bash
   docker build -t django-app .
   docker run -d -p 80:8000 --env-file .env django-app
   ```

6. **Accede a tu app:**
   - `http://tu-droplet-ip`

## Configuración de Producción Adicional

### Base de Datos en Producción
Si quieres usar PostgreSQL en lugar de SQLite:

1. En DigitalOcean, crea un "Managed Database" (PostgreSQL)

2. Actualiza `requeriments.txt`:
   ```
   psycopg2-binary==2.9.9
   ```

3. Agrega a las variables de entorno:
   ```
   DATABASE_URL=postgresql://user:password@host:port/dbname
   ```

4. Actualiza `settings.py` para usar DATABASE_URL

### HTTPS y Dominio Personalizado
- En App Platform, puedes agregar un dominio personalizado gratis con SSL automático
- En Droplet, usa nginx + certbot para SSL

## Comandos Útiles

### Ver logs en DigitalOcean App Platform:
```bash
doctl apps logs <app-id>
```

### Actualizar la aplicación:
1. Haz push a GitHub
2. DigitalOcean detectará cambios y redesplegará automáticamente

### Ver logs en Docker (Droplet):
```bash
docker ps  # Ver contenedores en ejecución
docker logs <container-id>
```

## Notas Importantes

- ⚠️ **Cambia SECRET_KEY** en producción (genera una nueva)
- ⚠️ **Establece DEBUG=False** en producción
- ⚠️ **Agrega tu dominio** a ALLOWED_HOSTS
- 💾 SQLite funciona para apps pequeñas, pero considera PostgreSQL para producción
- 🔐 No subas el archivo `.env` a GitHub (ya está en .gitignore)

## Soporte
- Docs DigitalOcean: https://docs.digitalocean.com/products/app-platform/
- Django Deployment: https://docs.djangoproject.com/en/5.2/howto/deployment/

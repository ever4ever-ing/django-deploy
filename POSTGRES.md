# 🐘 Guía de PostgreSQL para Django - Rama Dev

## 📋 Resumen de Funcionalidades

Esta rama `dev` incluye:
- ✅ Modelo `Producto` con campos: nombre, precio, categoría, descripción
- ✅ Vista de tabla de productos con diseño Bootstrap
- ✅ Formulario para crear nuevos productos
- ✅ Registro en Django Admin
- ✅ Soporte para PostgreSQL en producción
- ✅ SQLite para desarrollo local

---

## 🗂️ Modelo de Datos

### Producto (`app/models.py`)

```python
class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=50, choices=CATEGORIAS)
    descripcion = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
```

**Categorías disponibles:**
- Electrónica
- Ropa
- Alimentos
- Hogar
- Deportes
- Otros

---

## 🚀 Configuración Local (Desarrollo con SQLite)

### 1. Cambiar a la rama dev
```bash
git checkout dev
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3. Crear migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Crear superusuario (opcional, para acceder al admin)
```bash
python manage.py createsuperuser
```

### 5. Ejecutar servidor
```bash
python manage.py runserver
```

### 6. Acceder a la aplicación
- **Vista principal:** http://localhost:8000/
- **Admin:** http://localhost:8000/admin/

---

## 🗄️ Configuración PostgreSQL en Render

### Paso 1: Crear Base de Datos PostgreSQL en Render

1. Ve a https://dashboard.render.com
2. Click en "New +" → "PostgreSQL"
3. Configura:
   - **Name:** `django-productos-db` (o el nombre que prefieras)
   - **Database:** `productos_db`
   - **User:** Se genera automáticamente
   - **Region:** Elige la más cercana
   - **Plan:** Free (o el que prefieras)
4. Click en "Create Database"
5. **Guarda la URL de conexión** que aparece como "Internal Database URL"

### Paso 2: Configurar Web Service en Render

1. Ve a tu Web Service existente o crea uno nuevo
2. En la sección "Environment", agrega la variable:
   ```
   DATABASE_URL=postgresql://usuario:password@host:port/database
   ```
   (Copia la "Internal Database URL" de tu PostgreSQL)

3. **Build Command:**
   ```bash
   pip install -r requirements.txt && python manage.py migrate
   ```

4. **Start Command:**
   ```bash
   gunicorn project.wsgi:application
   ```

### Paso 3: Desplegar

```bash
git add .
git commit -m "Add productos feature with PostgreSQL support"
git push origin dev
```

Render detectará los cambios y redesplegará automáticamente.

### Paso 4: Crear superusuario en producción (opcional)

Desde el Shell de Render:
```bash
python manage.py createsuperuser
```

---

## 📦 Archivos Actualizados en esta Rama

### Nuevos Archivos:
- `app/forms.py` - Formulario para crear productos
- `app/templates/crear_producto.html` - Template del formulario
- `POSTGRES.md` - Esta documentación

### Archivos Modificados:
- `app/models.py` - Modelo Producto agregado
- `app/admin.py` - Registro del modelo en admin
- `app/views.py` - Vistas index y crear_producto
- `app/urls.py` - URLs para las nuevas vistas
- `app/templates/index.html` - Tabla de productos con Bootstrap
- `requirements.txt` - Agregado psycopg2-binary y dj-database-url
- `project/settings.py` - Configuración dual SQLite/PostgreSQL

---

## 🔄 Configuración de Base de Datos Dual

La aplicación está configurada para usar automáticamente:
- **SQLite** en desarrollo local (cuando no existe `DATABASE_URL`)
- **PostgreSQL** en producción (cuando existe `DATABASE_URL` en variables de entorno)

```python
# settings.py
DATABASE_URL = os.environ.get('DATABASE_URL')

if DATABASE_URL:
    # PostgreSQL en producción
    DATABASES = {
        'default': dj_database_url.config(default=DATABASE_URL)
    }
else:
    # SQLite en desarrollo
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
```

---

## 🎨 Características de la UI

### Vista Principal (index.html)
- ✨ Diseño moderno con Bootstrap 5
- 📊 Tabla responsive con todos los productos
- 🎨 Gradiente de fondo atractivo
- 🔍 Muestra: nombre, precio, categoría, descripción y fecha
- ➕ Botón para agregar nuevo producto

### Formulario de Creación (crear_producto.html)
- 📝 Campos: nombre, precio, categoría, descripción
- ✅ Validación de formularios
- 🎯 Diseño centrado y responsivo
- 💾 Botones de guardar y cancelar

### Admin de Django
- 📋 Lista con filtros por categoría y fecha
- 🔍 Búsqueda por nombre y descripción
- 📊 Ordenamiento por fecha de creación

---

## 🧪 Pruebas

### Probar localmente (SQLite):
```bash
# Ejecutar servidor
python manage.py runserver

# Acceder a http://localhost:8000/
# 1. Crear algunos productos
# 2. Verificar que aparezcan en la tabla
# 3. Probar el formulario
```

### Verificar PostgreSQL en Render:
```bash
# Desde el Shell de Render, ejecuta:
python manage.py shell

# Luego:
from app.models import Producto
print(Producto.objects.count())
```

---

## 📊 Dependencias Agregadas

```txt
psycopg2-binary==2.9.9    # Adaptador PostgreSQL
dj-database-url==2.1.0     # Parser de DATABASE_URL
```

---

## 🔒 Variables de Entorno Requeridas en Render

```bash
# Obligatoria para PostgreSQL:
DATABASE_URL=postgresql://user:pass@host:port/dbname

# Opcionales (recomendadas para producción):
SECRET_KEY=tu-clave-secreta-segura
DEBUG=False
```

---

## 🐛 Solución de Problemas

### Error: "no such table: app_producto"
**Causa:** Migraciones no ejecutadas
**Solución:**
```bash
python manage.py makemigrations
python manage.py migrate
```

### Error: "relation 'app_producto' does not exist" (PostgreSQL)
**Causa:** Migraciones no ejecutadas en PostgreSQL
**Solución:** Asegúrate que el Build Command incluya `migrate`:
```bash
pip install -r requirements.txt && python manage.py migrate
```

### Error: "could not connect to server"
**Causa:** DATABASE_URL incorrecta o base de datos no disponible
**Solución:** Verifica que:
1. La base de datos PostgreSQL esté activa en Render
2. La variable DATABASE_URL esté correcta
3. Uses la "Internal Database URL" (no la externa)

### Error: "psycopg2 not found"
**Causa:** Dependencia no instalada
**Solución:**
```bash
pip install psycopg2-binary
```

---

## 📈 Próximas Mejoras

- [ ] Agregar edición de productos
- [ ] Agregar eliminación de productos
- [ ] Paginación para muchos productos
- [ ] Búsqueda y filtros
- [ ] Imágenes de productos
- [ ] API REST con Django REST Framework

---

## 🔗 URLs Disponibles

| URL | Vista | Descripción |
|-----|-------|-------------|
| `/` | `index` | Lista de productos |
| `/producto/nuevo/` | `crear_producto` | Formulario para crear producto |
| `/admin/` | Admin Django | Panel administrativo |

---

## 📝 Comandos Útiles

```bash
# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Shell de Django
python manage.py shell

# Ver todos los productos
python manage.py shell -c "from app.models import Producto; print(Producto.objects.all())"

# Limpiar base de datos (desarrollo)
python manage.py flush
```

---

## 🌐 Despliegue Completo

### Resumen de Pasos:

1. **Crear PostgreSQL en Render**
2. **Copiar DATABASE_URL**
3. **Agregar DATABASE_URL a Environment del Web Service**
4. **Actualizar Build Command:**
   ```bash
   pip install -r requirements.txt && python manage.py migrate
   ```
5. **Push a GitHub:**
   ```bash
   git add .
   git commit -m "Add productos with PostgreSQL"
   git push origin dev
   ```
6. **Verificar logs en Render** para confirmar que las migraciones se ejecutaron

---

## ✅ Checklist de Despliegue

- [ ] Rama `dev` creada y actualizada
- [ ] PostgreSQL creado en Render
- [ ] DATABASE_URL configurada en Web Service
- [ ] Build Command actualizado con migrate
- [ ] Migraciones ejecutadas exitosamente
- [ ] Superusuario creado (opcional)
- [ ] App funcionando en URL de Render
- [ ] Productos visibles en la tabla
- [ ] Formulario de creación funcional

---

**Última actualización:** 20 de noviembre de 2025  
**Rama:** dev  
**Base de Datos:** PostgreSQL (producción) / SQLite (desarrollo)  
**Estado:** ✅ Lista para desplegar

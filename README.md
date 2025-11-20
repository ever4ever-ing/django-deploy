# 🚀 Django Deploy - Gestión de Productos

Aplicación Django para gestión de productos con soporte para PostgreSQL.

## 📌 Ramas

### `main` - Producción Simple
- Hello World básico
- Configurado para Render
- SQLite
- ✅ Actualmente en producción

### `dev` - Desarrollo con Productos
- ✨ **CRUD de Productos**
- 📊 Vista de tabla con Bootstrap 5
- ➕ Formulario de creación
- 🐘 Soporte PostgreSQL + SQLite
- 🎨 UI moderna y responsive

## 🎯 Funcionalidades (rama dev)

### Modelo Producto
```python
- nombre (CharField)
- precio (DecimalField)
- categoria (CharField con choices)
- descripcion (TextField opcional)
- fecha_creacion (DateTimeField)
- fecha_actualizacion (DateTimeField)
```

### URLs Disponibles
- `/` - Lista de productos (tabla)
- `/producto/nuevo/` - Formulario para crear producto
- `/admin/` - Panel administrativo de Django

## 🚀 Inicio Rápido

### Desarrollo Local
```bash
# Clonar y entrar al proyecto
git clone https://github.com/ever4ever-ing/django-deploy.git
cd django-deploy

# Cambiar a rama dev
git checkout dev

# Crear entorno virtual
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# Instalar dependencias
pip install -r requirements.txt

# Migraciones
python manage.py migrate

# Crear superusuario (opcional)
python manage.py createsuperuser

# Ejecutar servidor
python manage.py runserver
```

Acceder a: http://localhost:8000

## 📦 Despliegue en Render

Ver documentación detallada en:
- **[DEPLOYMENT.md](DEPLOYMENT.md)** - Guía general de despliegue
- **[POSTGRES.md](POSTGRES.md)** - Configuración PostgreSQL y funcionalidades

### Resumen rápido:

1. **Crear PostgreSQL en Render**
2. **Configurar Web Service:**
   - Build Command: `pip install -r requirements.txt && python manage.py migrate`
   - Start Command: `gunicorn project.wsgi:application`
   - Environment: `DATABASE_URL=postgresql://...`
3. **Push a GitHub** y Render despliega automáticamente

## 🛠️ Tecnologías

- Django 5.2.8
- Python 3.12
- PostgreSQL (producción)
- SQLite (desarrollo)
- Bootstrap 5
- Gunicorn
- Render (hosting)

## 📁 Estructura del Proyecto

```
django-deploy/
├── app/
│   ├── models.py          # Modelo Producto
│   ├── views.py           # Vistas index y crear_producto
│   ├── forms.py           # Formulario ProductoForm
│   ├── urls.py            # URLs de la app
│   ├── admin.py           # Registro en admin
│   └── templates/
│       ├── index.html     # Tabla de productos
│       └── crear_producto.html  # Formulario
├── project/
│   ├── settings.py        # Configuración dual DB
│   └── wsgi.py
├── requirements.txt       # Dependencias
├── DEPLOYMENT.md         # Guía de despliegue
└── POSTGRES.md          # Guía PostgreSQL
```

## 🔧 Variables de Entorno (Render)

```bash
DATABASE_URL=postgresql://user:pass@host:port/dbname
SECRET_KEY=tu-clave-secreta
DEBUG=False
```

## 🌐 URLs del Proyecto

- **Repositorio:** https://github.com/ever4ever-ing/django-deploy
- **Producción (main):** https://django-deploy-iaxg.onrender.com

## 📝 Comandos Útiles

```bash
# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Ejecutar tests
python manage.py test

# Recolectar estáticos
python manage.py collectstatic
```

## 🎨 Capturas

### Vista Principal (Tabla de Productos)
- Diseño moderno con gradiente
- Tabla responsive
- Badges de categorías
- Botón para agregar productos

### Formulario de Creación
- Validación automática
- Campos: nombre, precio, categoría, descripción
- Diseño centrado y limpio

## 📚 Documentación Adicional

- [Django Documentation](https://docs.djangoproject.com/)
- [Render Docs](https://render.com/docs)
- [PostgreSQL](https://www.postgresql.org/docs/)

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama (`git checkout -b feature/nueva-funcionalidad`)
3. Commit cambios (`git commit -m 'Add nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

---

**Desarrollado con ❤️ usando Django**  
**Última actualización:** 20 de noviembre de 2025

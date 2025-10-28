# Sistema de Gestión de Voluntarios

Sistema web desarrollado con Django para gestionar voluntarios y eventos comunitarios de una organización sin fines de lucro.

## 🚀 Características

- ✅ Registro y gestión de voluntarios
- ✅ Creación y administración de eventos
- ✅ Asignación de voluntarios a eventos
- ✅ CRUD completo (Crear, Leer, Actualizar, Eliminar)
- ✅ Interfaz responsive con Bootstrap
- ✅ Panel de administración

## 🔧 Instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/tu-usuario/gestion-voluntarios.git
cd gestion-voluntarios
```
2. **Crear entorno virtual**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```
3. **Instalar dependencias**
```bash
pip install django
```
4. **Realizar migraciones**
```bash
cd gestion_voluntarios
python manage.py migrate
```
5. **Crear superusuario**
```bash
python manage.py createsuperuser
```
6. **Ejecutar servidor**
```bash
python manage.py runserver
```
7. **Acceder a la aplicación**

- Aplicación: http://localhost:8000
- Panel admin: http://localhost:8000/admin

## 📁 Estructura del Proyecto
```bash
gestion_voluntarios/
├── gestion_voluntarios/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── voluntarios/
│   ├── migrations/
│   ├── templates/
│   │   └── voluntarios/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── lista_voluntarios.html
│   │       ├── lista_eventos.html
│   │       └── ...
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
└── manage.py
```

## 💻 Funcionalidades Principales
### Gestión de Voluntarios
- Registrar nuevos voluntarios
- Ver listado de voluntarios
- Editar información de voluntarios
- Eliminar voluntarios

### Gestión de Eventos
- Crear nuevos eventos
- Ver listado de eventos
- Asignar voluntarios a eventos
- Editar y eliminar eventos

## 🛠️ Tecnologías Utilizadas
- Backend: Django 4.2
- Frontend: HTML, Bootstrap 5
- Base de datos: SQLite (por defecto)
- Lenguaje: Python 3.8+

## 👤 Autor
Moisés Ortega - https://github.com/moisesdatasci

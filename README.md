# GC02-GPS25_Comunidad
Creación de la base de datos para la API de Comunidad de la aplicación UnderSounds. - GPS 25/26, Ing. Software

**Microservicio de Comunidades (UnderSounds)**

Este proyecto contiene la API REST para la gestión de comunidades de la plataforma UnderSounds, construido con Django y Django REST Framework, conectado con una base de datos SQLite.

## Características Principales
* ⚡️ API REST construida con Django y Django REST Framework
* 🗃️ Base de datos ligera con SQLite 3 (configuración por defecto de Django)
* 🧩 Arquitectura limpia desacoplada con patrón DAO, DTO y Controller (APIView)
* 📑 Documentación y contrato de API definidos con OpenAPI (YAML)
* 🤝 Patrón de Composición de Microservicios (consulta datos de servicios externos como Usuarios)
* 🔒 Preparado para autenticación (el YAML define endpoints con Bearer Auth)

## 🚀 Puesta en marcha (Desarrollo Local)

Sigue estos pasos para clonar, instalar y ejecutar el servidor en tu máquina local.

### 🔙 1. Prerrequisitos

* [Python](https://www.python.org/downloads/) 3.10+
* [Git](https://git-scm.com/install/)

### 🛠️ 2. Instalación

1.  Clona el repositorio (si no lo has hecho):
    ```bash
    git clone https://github.com/jnogalesg/GC02-GPS25_Comunidad
    cd GC02-GPS25_ComunidadBETA
    ```

2.  Crea un entorno virtual. Esto aísla las dependencias del proyecto.
    ```bash
    python -m venv venv
    ```

3.  Activa el entorno virtual:
    ```bash
    # En Windows (CMD o PowerShell)
    .\venv\Scripts\activate
    
    # En macOS/Linux
    source venv/bin/activate
    ```
    Verás un `(venv)` al inicio de tu línea de comandos si se activó correctamente.

4.  Instala todas las dependencias del proyecto:
    ```bash
    pip install -r requirements.txt
    ```
    *`requirements.txt` incluye la instalación de Django, Django REST Framework, request y otras dependecias necesarias*

### 🧑🏻‍💻 3. Configuración de la Base de Datos

Este proyecto utiliza **SQLite** por defecto, por lo que no requiere un servidor de base de datos externo.

1.  Aplica las migraciones para crear las tablas en el archivo `db.sqlite3`:
    ```bash
    # Crea las migraciones a partir de los modelos (solo si has modificado modelos o no hay migraciones)
    python mymicroservice/manage.py makemigrations

    # Aplica las migraciones a la base de datos
    python mymicroservice/manage.py migrate
    ```

### 🚀 4. Ejecutar el Servidor

Una vez instalado y con la base de datos migrada, puedes iniciar el servidor de desarrollo:

```bash
python mymicroservice/manage.py runserver
```

El servidor estará corriendo y escuchando en http://127.0.0.1:8000/

##### 🔍 Inspección y modificación directa de la base de datos:

Puede realizarse desde el panel de superusuario de Django, a través de la dirección: http://127.0.0.1:8000/admin

```
usuario: admin
contraseña: admin
```

## 📁 Arquitectura del microservicio
```
mymicroservice/
├── mymicroservice/       # ⚙️ Configuración global del proyecto Django
│   ├── settings.py       # Variables de entorno, apps instaladas, BD
│   ├── urls.py           # Enrutador principal
│   └── wsgi.py           # Punto de entrada para servidores web
│
├── comunidades/          # 📦 App principal (Lógica del dominio Comunidad)
│   ├── controller/       # 🤵 Controladores (APIViews - Gestionan peticiones HTTP)
│   │   ├── comunidad_controller.py
│   │   ├── miembro_controller.py
│   │   └── ...
│   ├── dao/              # 👨‍🍳 Data Access Objects (Acceso a BD y APIs externas)
│   │   ├── comunidad_dao.py
│   │   ├── miembro_dao.py
│   │   └── ...
│   ├── dto/              # 🍛 Data Transfer Objects (Estructuras de datos puras)
│   │   ├── comunidad_dto.py
│   │   ├── artista_dto.py
│   │   └── ...
│   ├── migrations/       # 🗃️ Historial de cambios en la base de datos
│   ├── models.py         # 🧱 Definición de tablas (La "Despensa")
│   ├── urls.py           # 🔗 Rutas específicas de la API de comunidades
│   └── admin.py          # 🛠️ Panel de administración
│
├── manage.py             # 🚀 Script de ejecución y gestión del servidor
└── requirements.txt      # 📦 Dependencias del proyecto
```
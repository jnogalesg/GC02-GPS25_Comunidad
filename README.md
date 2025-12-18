# GC02-GPS25_Comunidad
Creación de la base de datos para la API de Comunidad de la aplicación UnderSounds. - GPS 25/26, Ing. Software

**Microservicio de Comunidades (UnderSounds)**

Este proyecto contiene la API REST para la gestión de comunidades de la plataforma UnderSounds, construido con **Django**, **Django REST Framework** y **MySQL**, totalmente contenerizado con **Docker**.

## Características Principales
* ⚡️ API REST construida con **Django y Django REST Framework**.
* 🐳 **Despliegue contenerizado** con Docker y Docker Compose.
* 🗄️ **Base de datos MySQL 8.0** persistente y robusta.
* 🧩 Arquitectura limpia desacoplada con **patrón DAO, DTO y Controller**(APIView).
* 🤝 Patrón de **Composición de Microservicios** (consulta datos de servicios externos como Usuarios).
* 📑 Documentación y contrato de API definidos con **OpenAPI** (YAML).

---

## 🚀 Puesta en marcha (Docker)

Esta es la forma recomendada de iniciar el proyecto, ya que levanta tanto la API como la base de datos MySQL configurada automáticamente.

### 1. Prerrequisitos
* [Docker Desktop](https://www.docker.com/products/docker-desktop/) instalado y corriendo.
* [Git](https://git-scm.com/install/).

### 2. Instalación y Despliegue

1.  **Clona el repositorio:**
    ```bash
    git clone https://github.com/jnogalesg/GC02-GPS25_Comunidad
    cd GC02-GPS25_Comunidad
    ```

2.  **Levanta los contenedores:**
    En la raíz del proyecto (donde está `docker-compose.yml`), ejecuta:
    ```bash
    docker-compose up -d --build
    ```
    *Esto descargará las imágenes, instalará dependencias y levantará la API en el puerto **8084** y MySQL en el **3307**.*

3.  **Inicializa la Base de Datos:**
    Una vez levantados los contenedores, ejecuta las migraciones para crear las tablas en MySQL:
    ```bash
    docker exec -it microservicio_comunidades python mymicroservice/manage.py migrate
    ```

4.  **(Opcional) Crea un Superusuario:**
    Para acceder al panel de administración:
    ```bash
    docker exec -it microservicio_comunidades python mymicroservice/manage.py createsuperuser
    ```

### 3. Acceso al Microservicio

* **API Root:** `http://127.0.0.1:8084/comunidad/`
* **Panel de Administración:** `http://127.0.0.1:8084/admin/`

---

## 🗄️ Conexión Externa a la Base de Datos

El proyecto expone el puerto **3307** para permitir conexiones desde herramientas de gestión como **DBeaver**, **MySQL Workbench** o **DataGrip**.

Usa las siguientes credenciales para conectarte:

| Parámetro | Valor |
| :--- | :--- |
| **Motor** | MySQL 8.0 |
| **Host** | `localhost` |
| **Puerto** | `3307` |
| **Base de Datos** | `db_comunidades` |
| **Usuario** | `user_comunidades` |
| **Contraseña** | `password_comunidades` |

> **⚠️ Nota para usuarios de DBeaver:**
> Si recibes un error de "Public Key Retrieval", ve a **Driver Properties** y establece `allowPublicKeyRetrieval` en **TRUE**.

---

## ⚙️ Configuración del Entorno

El proyecto utiliza variables de entorno definidas en `docker-compose.yml` para configurar la conexión.

| Variable | Descripción | Valor en Docker |
| :--- | :--- | :--- |
| `USER_MICROSERVICE_URL` | URL del microservicio de Usuarios para hidratar datos. | `http://host.docker.internal:3000/api/usuarios/` |
| `MYSQL_HOST` | Host de la base de datos interna. | `db` |
| `DEBUG` | Modo depuración. | `True` |

---

## 📁 Arquitectura del Proyecto

```text
mymicroservice/
├── mymicroservice/       # ⚙️ Configuración global del proyecto Django
├── comunidades/          # 📦 App principal
│   ├── controller/       # 🤵 Controladores (Lógica HTTP)
│   ├── dao/              # 👨‍🍳 Data Access Objects (Acceso a BD/APIs)
│   ├── dto/              # 🍛 Data Transfer Objects
│   ├── models.py         # 🧱 Modelos (ORM)
│   └── exceptions.py     # ⚠️ Excepciones personalizadas
├── Dockerfile            # 🐳 Definición de la imagen de la API
├── docker-compose.yml    # 🐙 Orquestación de servicios (API + MySQL)
├── manage.py             # 🚀 Script de gestión
└── requirements.txt      # 📦 Dependencias (incluye mysqlclient)
```
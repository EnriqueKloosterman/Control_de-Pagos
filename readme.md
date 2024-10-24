# Control de Pagos

La Aplicación de Pagos es una plataforma intuitiva para la gestión eficiente de pagos asociados a diferentes boletas. Pensada para usuarios que necesitan llevar un control detallado de sus transacciones, la aplicación permite registrar, visualizar y administrar pagos de manera sencilla.

Con una interfaz moderna y responsiva basada en Django y Tailwind CSS, los usuarios pueden filtrar sus pagos por boleta, fechas y otros criterios. Además, la posibilidad de editar y eliminar pagos facilita mantener la información actualizada.

## Tabla de Contenidos

- [Características](#características)
- [Tecnologías Usadas](#tecnologías-usadas)
- [Instalación](#instalación)
- [Uso](#uso)
- [Contribución](#contribución)
- [Licencia](#licencia)

## Características

- Gestión de boletas.
- Registro y seguimiento de pagos.
- Filtros para buscar boletas por nombre, mes y estado de pago.
- Interfaz amigable y fácil de usar.
- Autenticación de usuarios para un acceso seguro.

## Tecnologías Usadas

- [Django](https://www.djangoproject.com/) - Framework web para Python.
- [SQLite](https://www.sqlite.org/index.html) - Base de datos por defecto.
- [Tailwind CSS](https://tailwindcss.com/) - Framework CSS para estilos.
- [Python](https://www.python.org/) - Lenguaje de programación.
- [HTML/CSS](https://www.w3.org/standards/webdesign/) - Estructura y estilo de la aplicación.

## Instalación

Sigue estos pasos para configurar y ejecutar la aplicación:

1. Clona el repositorio:
    ```bash
    git clone https://github.com/EnriqueKloosterman/Control_de-Pagos.git
    cd nombre_del_repositorio
    ```

2. Crea un entorno virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Linux/Mac
    .\venv\Scripts\activate     # En Windows
    ```

3. Instala las dependencias:
    ```bash
    pip install django-tailwind
    ```

4. Realiza las migraciones:
    ```bash
    python manage.py migrate
    ```

5. Crea un superusuario (opcional):
    ```bash
    python manage.py createsuperuser
    ```

6. **Iniciar Tailwind CSS:**  
   Tailwind necesita correr en segundo plano para compilar los estilos.
   ```bash
   python manage.py tailwind start
   ```

7. Ejecuta el servidor:
    ```bash
    python manage.py runserver
    ```

8. Accede a la aplicación en tu navegador: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Uso

- Regístrate o inicia sesión para acceder a la aplicación.
- Agrega boletas y realiza pagos.
- Utiliza los filtros para buscar boletas específicas.
- Administra tus pagos desde la interfaz.


## Licencia

Este proyecto está bajo la Licencia MIT. Para más detalles, consulta el archivo [LICENSE](LICENSE).

# Proyecto Django - Biblioteca

Este proyecto es una aplicación web básica desarrollada en Django. Permite a los usuarios registrar autores, libros y editoriales, así como buscar estos registros a través de formularios.

## Estructura del Proyecto

- **mi_aplicacion**: Contiene la lógica de la aplicación, modelos, vistas y URLs.
- **templates**: Contiene las plantillas HTML para la aplicación.
- **static**: Contiene archivos estáticos como CSS y JavaScript (si se usan).
- **manage.py**: Herramienta para gestionar el proyecto Django.

## Instalación

1. **Clona el repositorio:**

    ```sh
    git clone https://github.com/tu_usuario/tu_repositorio.git
    cd tu_repositorio
    ```

2. **Crea un entorno virtual y actívalo:**

    ```sh
    python -m venv env
    source env/bin/activate  # En Windows: env\Scripts\activate
    ```

3. **Instala las dependencias:**

    git
    Django
    python
    ```

4. **Aplica las migraciones:**

    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Inicia el servidor de desarrollo:**

    python manage.py runserver
    ```

6. **Accede a la aplicación en tu navegador:**

    Abre `http://127.0.0.1:8000/` en tu navegador.

## Funcionalidades:

### Registro

- **Agregar Autor**: Formulario para registrar información sobre autores, y/o para buscar Autores.

- **Agregar Libro**: Formulario para registrar libros con título, nombre del autor y editorial tambien 
    para buscar libros.

- **Agregar Editorial**: Formulario para registrar Editoriales, como las anteriores, tambien 
    sirve para buscar editoriales ya registradas.

### Búsqueda

- **Buscar_Libros**: Permite buscar libros por título, nombre del autor o editorial.
- **Buscar_Autores**: Permite buscar autores por nombre.
- **Buscar_Editoriales**: Permite buscar editoriales por nombre.

*Todos estas Funcionalidades estan dentro de la pagina de registro, por eso , especifique que la pagina
 Agregar Autor , etc , tambien pueden usarse para buscar.

## Modelos

- **Autor**: Contiene Nombre, Apellido y Nacionalidad.
- **Libro**: Contiene Título, Autor y Editorial
- **Editorial**: Contiene Nombre, Direccion e Email.

## Vistas

- **buscar_libro**: Vista para buscar libros.
- **buscar_autor**: Vista para buscar autores.
- **buscar_editorial**: Vista para buscar editoriales.

** apruebenme plis jajaj


# Recordatorio de Estudio

Este proyecto es una aplicación simple desarrollada en Python utilizando la biblioteca Tkinter. La aplicación presenta un recordatorio con un mensaje personalizado y permite al usuario confirmar una acción específica, la cual se ejecuta mediante un comando de sistema predefinido.

## Requisitos

- Python 3.x
- Tkinter (normalmente incluido con Python)
- Un archivo `settings.json` con las configuraciones necesarias

## Instalación

1. Clona este repositorio:
    ```bash
    git clone https://github.com/tu_usuario/recordatorio_estudio.git
    cd recordatorio_estudio
    ```

2. Asegúrate de tener Python 3.x instalado en tu sistema.

3. Verifica que el archivo `settings.json` esté presente en el directorio raíz del proyecto. Este archivo debe tener el siguiente formato:

    ```json
    {
        "message": ["Tu mensaje de recordatorio aquí", "La frase de confirmación aquí"],
        "exe_path": "ruta/al/archivo/ejecutable",
        "launch_product": "nombre_del_producto"
    }
    ```

## Uso

1. Ejecuta el script de Python:

    ```bash
    python recordatorio_estudio.py
    ```

2. Aparecerá una ventana con el mensaje de recordatorio especificado en `settings.json`.

3. Selecciona "Sí" para confirmar la acción. Se te pedirá que ingreses una frase de confirmación. Si la frase es correcta, se ejecutará el comando especificado en `settings.json`.

4. Selecciona "No" para cerrar la aplicación sin realizar ninguna acción.

## Estructura del Código

- **center_window(window, width_percentage, height_percentage)**: Función para centrar una ventana en la pantalla.
- **on_yes()**: Función llamada cuando el usuario selecciona "Sí". Abre una ventana de confirmación y ejecuta el comando si la frase es correcta.
- **on_no()**: Función llamada cuando el usuario selecciona "No". Cierra la aplicación.
- **root**: Ventana principal de la aplicación.

## Personalización

Puedes personalizar el mensaje de recordatorio y la frase de confirmación editando el archivo `settings.json`. Además, puedes cambiar la ruta del archivo ejecutable y otros parámetros necesarios para la ejecución del comando.

## Contribuciones

¡Las contribuciones son bienvenidas! Siéntete libre de abrir un issue o enviar un pull request.

## Licencia

Este proyecto está bajo la licencia MIT. Puedes ver más detalles en el archivo [LICENSE](LICENSE).

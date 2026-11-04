# Cómo publicar el prototipo navegable (enlace de solo lectura)

Toma unos 5 minutos y no requiere usar la terminal.

1. Entrá a GitHub con tu cuenta y creá un repositorio nuevo: **New repository**.
   - Nombre: `sigeda-prototipo`
   - Visibilidad: **Public** (GitHub Pages es gratis en repositorios públicos). Solo lleva datos ficticios.
   - Marcá «Add a README file» y presioná **Create repository**.
2. En el repositorio: **Add file › Upload files** y arrastrá el archivo `prototipo/index.html` de esta carpeta. Presioná **Commit changes**.
3. Andá a **Settings › Pages**. En «Build and deployment» elegí:
   - Source: **Deploy from a branch**
   - Branch: **main**, carpeta **/ (root)**
   - Presioná **Save**.
4. Esperá 1 o 2 minutos y recargá la página. Arriba aparece el enlace:
   `https://TU-USUARIO.github.io/sigeda-prototipo/`
5. Abrilo en una ventana privada para comprobar que se ve sin iniciar sesión.
6. Para agregar al equipo: **Settings › Collaborators › Add people**. Los colaboradores pueden subir cambios; el docente y cualquier otra persona solo pueden ver.

Pasame el enlace y lo pongo en la portada, en la sección 7 y en el Anexo A del documento.

## Cómo usar el prototipo

- Empieza en **PAN-01 Inicio de sesión**: entra con cualquier usuario y contraseña.
- El botón **«Panel del prototipo»** (abajo a la derecha) permite saltar a cualquier pantalla, ver sus estados (error, cargando, éxito…), abrir los diálogos D-01 a D-08 y cambiar a la **maqueta de alta fidelidad**.
- Para la evaluación con la administradora, dejá el panel cerrado y seguí el guion del Anexo C.

## Si hay que cambiar algo después de la evaluación

Todo sale de un solo archivo (`prototipo/index.html`). Las capturas y el mapa se regeneran con los scripts de `herramientas/`:

```
node herramientas/capturar.js capturas
python3 herramientas/mapa.py pantallas.json mapa_navegacion/Mapa_Navegacion_SIGEDA
python3 herramientas/mapa_doc.py pantallas.json mapa_navegacion/Mapa_Navegacion_SIGEDA_documento
```

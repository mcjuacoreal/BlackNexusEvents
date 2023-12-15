### Desiciones de diseño ###

Durante el proyecto se decidió que la busqueda sería unicamente mediante el lugar del evento, puesto a que 
de lo contrario, si se hubiese querido buscar mediante datos personales o descripciones, se estaría 
poniendo en peligro la privacidad del usuario que reservó confiandonos sus datos personales.

Es por esto mismo que además, al tener una busqueda exitosa, solo se revela el titulo del evento, la
fecha de realización y si este fue realizado o no (usando el campo booleano "realizado" para esto).

Para poder desplegar todos los eventos registrados en un lugar especifico se uso un ciclo de listas, además
de que el buscador funciona como el comando "LIKE" de SQL, ya que revisa si es que la palabra buscada se
ecnuentra dentro de alguna de las ubicaciones y no si es que es exactamente igual.

Para poder repetir el encabezado y el pie de página en todas las plantillas se usó una plantilla base, de 
la cual extendieron todas las demás, modificando solo el cuerpo de la pagina y su título.


### Proceso de desarrollo ###

Primero se construyo la base de datos y su conexion con el proyecto django a base de migrates, enlazandola
con el modelo Eventos recien creado.

Luego se diseño la plantilla base con su respectivo encabezado y pie de pagina.

Posteriormente se crearon las otras plantillas, junto con sus respectivos formularios de ingreso y busqueda
de datos.

Finalmente se implementaron las vistas de cada una de las plantillas del template y se configuraron las url
a mostrar.


### Instrucciones de instalacion y ejecución ###

1.- Descargar Django y postgreSQL desde sus páginas oficiales de no tenerlos instalados.

2.- Crear una carpeta para el proyecto y clonar el repositorio de github: 
    https://github.com/mcjuacoreal/BlackNexusEvents

3.- Desde una consola entrar a la carpeta del proyecto y ejecutar el comando:
    "python manage.py createsuperuser"
    Luego rellenar los datos para crear un superusuario y poder ingresar al panel de control.

4.- Desde el mismo directorio ejecutar el comando:
    "python manage.py runserver"
    Luego dirigirse a la url proporcionada seguida de /index/

4.- Si se desea ingresar al panel de control, usar la url proporcionada seguida de /admin/ e ingresar
    el usuario y contraseña configurados durante el paso 3.



MUCHAS GRACIAS POR LEER, TENGA UN BUEN DÍA, SALUDOS!!!
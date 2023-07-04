#Proyecto de Django
Este es el repositorio del proyecto de Django. A continuación, se proporcionan instrucciones y comandos útiles para trabajar en este proyecto.

Clonar el repositorio
Utiliza el siguiente comando para clonar el repositorio en tu máquina local:

git clone https://github.com/luiseliasdavid/django_fazt01.git

Instalar los requisitos del proyecto
Si estás configurando el proyecto en un entorno nuevo, instala todas las dependencias utilizando el siguiente comando:

pip install -r requirements.txt

Levantar el servidor
Para iniciar el servidor de desarrollo de Django, ejecuta el siguiente comando:

python manage.py runserver

Activar el entorno virtual
Si estás utilizando Git Bash como tu terminal, puedes activar el entorno virtual con el siguiente comando:
source venv/Scripts/activate


Actualizar cambios en la base de datos
Si realizas cambios en los modelos de la base de datos, deberás aplicar las migraciones correspondientes. Ejecuta los siguientes comandos:

python manage.py makemigrations
python manage.py migrate

Jinja commands
Para utilizar Jinja en tus plantillas HTML, puedes consultar la documentación oficial de Jinja para obtener información sobre la sintaxis y las funcionalidades disponibles. Puedes encontrar la documentación en el siguiente enlace:

https://jinja.palletsprojects.com/en/3.1.x/









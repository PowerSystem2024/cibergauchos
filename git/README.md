# Git-Github - Segundo semestre - Grupo Cibergauchos

# CLASE 01 MIÉRCOLES 14 DE AGOSTO DEL 2024 - Portafolio 1

> USO DE GITHUB Parte 1

<sub>GitHub es una plataforma que nos permite guardar repositorios de Git que podemos usar como servidores remotos y ejecutar algunos comandos de forma visual e interactiva (sin necesidad de la consola de comandos).</sub>

<sub>Luego de crear nuestra cuenta, podemos crear o importar repositorios, crear organizaciones y proyectos de trabajo, descubrir repositorios de otras personas, contribuir a esos proyectos, dar estrellas y muchas otras cosas.</sub>

> COMANDOS

**_#Import repository, New repository, New organization: significa que es como tu empresa, New project: significa es como un grupo de repositorios que puedes tener dentro de una empresa, New gist: es un pedasito de código que puedes compartir_**

**_New repository #Ponemos el nombre: class-git, descripción: Haremos un blog increible, hay muchas licencias para publicar el código: NO lo hacemos ahora._**

**_Create repository #Lo ponemos en privado o en Publico._**

<sub>El README.md es el archivo que veremos por defecto al entrar a un repositorio. Es una muy buena práctica configurarlo para describir el proyecto, los requerimientos y las instrucciones que debemos seguir para contribuir correctamente.</sub>

> Para clonar un repositorio desde GitHub (o cualquier otro servidor remoto) debemos copiar la URL (por ahora, usando HTTPS) y ejecutar el comando git clone + la URL que acabamos de copiar. Esto descargará la versión de nuestro proyecto que se encuentra en GitHub.

### ATENCIÓN: ¿Por qué? Porque a través de https nos pedirá usuario(nombre perfil) y contraseña.

<sub>Sin embargo, esto solo funciona para las personas que quieren empezar a contribuir en el proyecto.</sub>

> Cómo conectar un repositorio de GitHub a nuestro documento local Si queremos conectar el repositorio de GitHub con nuestro repositorio local, que creamos aconsejo que al trabajar desde GitHub no utilizemos localmente el comando git init, si debemos ejecutar las siguientes instrucciones:

```sh
Guardar la URL del repositorio de GitHub con el nombre de origin
git remote add origin URL
Verificar que la URL se haya guardado correctamente:
git remote
git remote -v
Traer la versión del repositorio remoto y hacer merge para crear un commit con los archivos de ambas partes. Podemos usar git fetch y git merge o solo git pull con el flag --allow-unrelated-histories:
git pull origin master --allow-unrelated-histories
Por último, ahora sí podemos hacer git push para guardar los cambios de nuestro repositorio local en GitHub:
git push origin master
```

> Cómo autenticarte en GitHub 2022

<sub>Antes de empezar debemos renombrar la rama ‘máster’ a ‘main’, este es el nuevo estándar en GitHub, para esto:</sub>

> Primero nos posicionamos en la rama a la que queremos cambiarle el nombre.

> Ejecutamos el siguiente comando: git branch -M main

<sub>Pasos para crear un token de acceso personal.</sub>

<sub>Desde el 2022 GitHub ya no deja hacer el push con la contraseña del propio GitHub, para esto tenemos que crear un token, y este token es la contraseña que vamos a colocar cuando nos pida clave. </sub>

**_Descubre el uso de tags en Github_**

> Seguir la secuencia: Ingresamos a nuestra cuenta de GitHub.

<sub>Buscamos Settings</sub>

<sub>Click en Developer settings</sub>

<sub>Click en Personal access tokens</sub>

<sub>Click en Generate new token aquí se puede colocar un nombre, la fecha de expiración.</sub>

<sub>Tildar en repo y luego click en el botón verde Generate token</sub>

## PORTAFOLIO

> Inicialización proyecto Vue Js



# CLASE 02 MIÉRCOLES 21 DE AGOSTO DEL 2024 - Portafolio 2

> Vamos a cargar la llave SSH publica en GitHub

<sub>Para copiar la llave publica debes ir al archivo .ssh y allí encontrarás el archivo .pub lo podes abrir con el txt, luego copiar el contenido que esta dentro.</sub>

<sub>copiar la llave publica #Ir a GitHub, vamos a setting, vamos a SSH and GPG keys</sub>

<sub>crear una nueva #New SSH key poner nombre y pegar la ssh publica, con esto esta listo.</sub>

> Aconsejo que la ssh tenga el nombre del ordenador en el que estas trabajando. Esto se debe hacer con cada pc nueva o dispositivo nuevo que tengamos para acceder a nuestra cuenta de GitHub.

```sh
git branch #Vemos en que rama estamos

git checkout master #Ponernos en la rama master

git branch -M main #Cambiamos el nombre a la rama master

git remote add origin git@github.com:nombreUsuario/class-git.git #Agregamos el repositorio remoto, este es un ejemplo

git remote -v #Vemos si ya esta conectado

git merge segunda #Mergeamos lo que tenemos en la rama segunda en main

git commit -am "Uso de GitHub parte 20" #Hacemos el commit de hoy

git push origin main #Pasamos todo lo hecho a GitHub, revisar en el repositorio en GitHub.
``` 

>Frente al cambio de nombre de rama master a main, suele suceder que en el repo de GitHub se hayan creado dos ramas, la rama master y la rama main, se debe ir al repo, settings y ahí se puede cambiar la rama principal, en vez de que siga siendo master, que sea la rama main, luego de eso ya podemos borrar la rama master.

## PORTAFOLIO

> Instalacion de Extensiones y Creación del Proyecto en Vue JS.


# CLASE 03 MIÉRCOLES 28 DE AGOSTO DEL 2024 - Portafolio 3

> Cambios en GitHub: de master a main

<sub>El escritor Argentino Julio Cortázar afirma que las palabras tienen color y peso. Por otro lado, los sinónimos existen por definición, pero no expresan lo mismo. Feo no es lo mismo que desagradable, ni aromático es lo mismo que oloroso.</sub>

<sub>Por lo anterior, podemos afirmar que los sinónimos no expresan lo mismo, no tienen el mismo “color” ni el mismo “peso”.</sub>

<sub>Sí, esta lectura es parte de la enseñanza profesional de Git & GitHub.</sub>

**_Desde el 1 de octubre de 2020 GitHub cambió el nombre de la rama principal: ya no es “master” -como aprenderás aquí- sino main._**

<sub>Este derivado de una profunda reflexión ocasionada por el movimiento #BlackLivesMatter.</sub>

<sub>La industria de la tecnología lleva muchos años usando términos como master, slave, blacklist o whitelist y esperamos pronto puedan ir desapareciendo.</sub>

<sub>Y sí, las palabras importan.</sub>

**_Por lo que de aquí en adelante cada vez que me escuches mencionar “master” debes saber que hago referencia a “main”._**

### ¿Cuando es que sigue siendo master y cuando sigue siendo main?

**_Cuando se crea un repositorio desde git bash en nuestro ordenador a través de git init, sigue siendo el estandar como master. ¿Qué hacer con esto? Debes cambiar el nombre de la rama master a main con el comando git branch -M main._**
_Ahora cuando creamos un repositorio desde la nube, osea desde GitHub, ya verás que la rama principal tiene por default el nombre de main y al clonar a nuestro ordenador seguira teniendo este nombre y no será necesario ningun cambio._

## PORTAFOLIO

> Inicialización de proyecto en Vue JS




# CLASE 04 MIÉRCOLES 4 DE SEPTIEMBRE DEL 2024 - Portafolio 4



> Tu primer push

<sub>La creación de las SSH es necesario solo una vez por cada computadora. Aquí conocerás cómo conectar a GitHub usando SSH.</sub>


<sub>Luego de crear nuestras llaves SSH podemos entregarle la llave pública a GitHub para comunicarnos de forma segura y sin necesidad de escribir nuestro usuario y contraseña todo el tiempo.</sub>

<sub>Para esto debes entrar a la Configuración de Llaves SSH en GitHub, crear una nueva llave con el nombre que le quieras dar y el contenido de la llave pública de tu computadora.</sub>

> Ahora podemos actualizar la URL que guardamos en nuestro repositorio remoto, solo que, en vez de guardar la URL con HTTPS, vamos a usar la URL con SSH:

```ssh

git remote set-url origin url-ssh-del-repositorio-en-github

Comandos para copiar la llave SSH:

ESTAS SON LAS RUTAS DEL SSH PUBLICO
-Mac:
pbcopy < ~/.ssh/id_rsa.pub

Windows (Git Bash):

clip < ~/.ssh/id_rsa.pub

Linux (Ubuntu):

cat ~/.ssh/id_rsa.pub

```

> Importante


<sub>Las buenas costumbres nos enseñan que antes de hacer un push, siempre debemos hacer un pull, un fetch, esto para que si alguien ya hizo algún cambio, no se genere un conflicto.</sub>

> Invitar a un colaborador

<sub>Para invitar a un colaborador debemos ir a GitHub y seleccionar:</sub>
<sub>setting -> colaborators -> ingresar contraseña o un F2A de verificación y enviar la invitación escribiendo el nombre de usuario.</sub>


<sub>Del otro lado el usuario invitado solo debe aceptar y listo, ya puede participar del proyecto haciendo commit.</sub>

## PORTAFOLIO

> Inicialización proyecto Vue Js

# CLASE 05 MIÉRCOLES 11 DE SEPTIEMBRE DEL 2024 - Portafolio 5

> *Git tag y versiones en GitHub*

<sub>En Git, las etiquetas o Git tags tienen un papel importante al asignar versiones a los commits más significativos de un proyecto. Aprender a utilizar el comando git tag, entender los diferentes tipos de etiquetas, cómo crearlas, eliminarlas y compartirlas, es esencial para un flujo de trabajo eficiente.</sub>


> Creación de etiquetas en Git

```sh
git tag

```


> Sustituye con un identificador semántico que refleje el estado del repositorio en el momento de la creación. Git admite etiquetas anotadas y ligeras.


> Listado de etiquetas
> Para obtener una lista de etiquetas en el repositorio, ejecuta el siguiente comando:
<div align="center">
<img src="https://static.platzi.com/media/user_upload/tagging%20%281%29-12fce53a-7a10-4eab-9b45-c37111d925f8.jpg" align="center" style="width: 350" />
</br>
</div> 

> Para crear una etiqueta, ejecuta el siguiente comando:



<sub>Las etiquetas anotadas almacenan información adicional como la fecha, etiquetador y correo electrónico, y son ideales para publicaciones públicas. Las etiquetas ligeras son más simples y se emplean como “marcadores” de una confirmación específica.</sub>

```ssh
git tag

Esto mostrará una lista de las etiquetas existentes, como:

v1.0

v1.1

v1.2

Para perfeccionar la lista, puedes utilizar opciones adicionales, como -l con una expresión comodín.


Uso compartido de etiquetas

Compartir etiquetas requiere un enfoque explícito al usar el comando git push. Por defecto, las etiquetas no se envían automáticamente. Para enviar etiquetas específicas, utiliza:

git push origin

Para enviar varias etiquetas a la vez, usa:

git push origin --tags


Eliminación de etiquetas
Para eliminar una etiqueta, usa el siguiente comando:

git tag -d

Esto eliminará la etiqueta identificada por en el repositorio local.

```

En resumen, las etiquetas en Git son esenciales para asignar versiones y capturar instantáneas importantes en el historial de un proyecto. Aprender a crear, listar, compartir y eliminar etiquetas mejorará tu flujo de trabajo con Git.



## PORTAFOLIO
#Creando el componente datos personales 

# CLASE 06 MIÉRCOLES 18 DE SEPTIEMBRE DEL 2024 - Portafolio 6

## Error con los tags
- Investigación: ¿Qué pasa si por error cargamos un tag dos veces?
Si cargamos un tags dos veces a un mismo commit (bajo nombres distintos), simplemente se agregan ambos.
- ¿Cómo solucionarías este problema o error?
Para solucionarlo y eliminar uno de ellos simplemente lo eliminamos con el comando:

```sh
git tag -d "nombre_del_tag_a_eliminar"
```

## Portafolio
Creando una línea de tiempo para la section Educación - Cursos
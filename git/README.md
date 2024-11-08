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

> Frente al cambio de nombre de rama master a main, suele suceder que en el repo de GitHub se hayan creado dos ramas, la rama master y la rama main, se debe ir al repo, settings y ahí se puede cambiar la rama principal, en vez de que siga siendo master, que sea la rama main, luego de eso ya podemos borrar la rama master.

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

> _Git tag y versiones en GitHub_

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

# CLASE 07 MIÉRCOLES 25 DE SEPTIEMBRE DEL 2024 - Portafolio 7

## Error con los tags

<sub>Investigación: Si un tag es imposible generarlo dos veces ¿Cómo es que existe el error de dos tags con el mismo nombre?¿Cómo se origina este problema o error?</sub>

<sub>Las situaciones que pueden dar lugar a errores que parecen indicar que hay dos tags con el mismo nombre pueden ser:</sub>
**_ 1.Tags locales y remotos: Puedes tener un tag con un nombre en tu repositorio local y, si alguien más crea un tag con el mismo nombre en el repositorio remoto, al intentar hacer un “git fetch” o “git pull”, podrías encontrarte con un conflicto o error, especialmente si no estás al tanto de la creación de ese tag en el remoto._**

**_ 2. Reescritura de la historia: Si has reescrito la historia de tu repositorio (por ejemplo, utilizando “git rebase” o “git commit –amend”), puedes terminar en situaciones en las que, al crear un nuevo tag, parezca que hay dos tags con el mismo nombre, aunque realmente estén apuntando a diferentes commits._**

**_ 3. Eliminación y recreación: Si se elimina un tag y luego se vuelve a crear con el mismo nombre, y si no se realiza un “git push –tags” después de la eliminación, puede haber confusiones, especialmente en repositorios colaborativos._**

**_ 4. Error de sincronización: En entornos donde varios desarrolladores están trabajando, puede haber problemas de sincronización que causen la aparición de tags duplicados._**

<sub>-Para resolver el conflicto relacionado con la creación de tags duplicados hay que seguir estos pasos y comandos:</sub>

**1. Verificar los tags existentes**
Primero, verifica los tags que ya existen en tu repositorio para confirmar si efectivamente hay duplicados.

```sh
git tag –l
```

**2. Eliminar el tag duplicado**
Si encuentras un tag que deseas eliminar, puedes hacerlo utilizando el siguiente comando. Asegúrate de saber qué tag deseas mantener.

```sh
git tag -d nombre_del_tag
```

Si el tag ya ha sido enviado a un repositorio remoto, también deberías eliminarlo del remoto:

```sh
git push origin --delete nombre_del_tag
```

**3. Crear un nuevo tag (si es necesario)**
Si necesitas crear un nuevo tag después de eliminar el duplicado, puedes hacerlo con:

```sh
git tag -a nombre_del_tag -m "Mensaje del tag"
```

Esto crea un tag anotado. Si solo deseas un tag ligero, puedes omitir la opción `-a` y el mensaje:

```sh
git tag nombre_del_tag
```

**4. Enviar el tag al remoto**
Después de crear el tag, asegúrate de enviarlo al repositorio remoto:

```sh
git push origin nombre_del_tag
```

**5. Verificar la eliminación y creación**
Verifica nuevamente los tags en tu repositorio local y remoto para asegurarte de que todo esté correcto.
Para listar los tags locales:

```sh
git tag -l
```

Para listar los tags remotos:

```sh
git ls-remote --tags origin
```

## Portafolio

Creando la seccion experiencia

# CLASE 08 MIÉRCOLES 2 DE OCTUBRE DEL 2024 - Portafolio 8

## Manejo de ramas en GitHub

Si no te funciona el comando gitk es posible no lo tengas instalado por defecto.
Para instalar gitk debemos ejecutar los siguientes comandos:

```sh

  sudo apt-get update

  sudo apt-get install gitk
```

Repasa: ¿Qué es Git?

Las ramas nos permiten hacer cambios a nuestros archivos sin modificar la versión principal (main). Puedes trabajar con ramas que nunca envías a GitHub, así como pueden haber ramas importantes en GitHub que nunca usas en el repositorio local. Lo crucial es que aprendas a manejarlas para trabajar profesionalmente.

Si, estando en otra rama, modificamos los archivos y hacemos commit, tanto el historial(git log) como los archivos serán afectados. La ventaja que tiene usar ramas es que las modificaciones solo afectarán a esa rama en particular. Si luego de “guardar” los archivos(usando commit) nos movemos a otra rama (git checkout otraRama) veremos como las modificaciones de la rama pasada no aparecen en la otraRama.

Comandos para manejo de ramas en GitHub
Crear una rama:

```sh
git branch branchName #Crear una rama
git checkout branchName #Movernos a otra rama
git checkout -b nombre-de-la-rama #Crear una rama en el repositorio local
git push origin nombre-de-la-rama #Publicar una rama local al repositorio remoto
```

Recuerda que podemos ver gráficamente nuestro entorno y flujo de trabajo local con Git utilizando el comando gitk. Gitk fue el primer visor gráfico que se desarrolló para ver de manera gráfica el historial de un repositorio de Git.

## Portafolio

Creando la galeria de Proyectos

# CLASE 09 MIÉRCOLES 9 DE OCTUBRE DEL 2024 - Portafolio 9

## Configurar múltiples colaboradores en un repositorio de GitHub

Por defecto, cualquier persona puede clonar o descargar tu proyecto desde GitHub, pero no pueden crear commits, ni ramas. Esto quiere decir que pueden copiar tu proyecto pero no colaborar con él, si este es publico, de otra manera, osea, si es privado es necesario que realmente estes haciendo una invitación, sino no lo van a poder ver. Existen varias formas de solucionar esto para poder aceptar contribuciones. Una de ellas es añadir a cada persona de nuestro equipo como colaborador de nuestro repositorio.

> Cómo agregar colaboradores en Github
> Solo debemos entrar a la configuración de colaboradores de nuestro proyecto. Se encuentra en:
> Repositorio > Settings > Collaborators
> Ahí, debemos añadir el email o username de los nuevos colaboradores.

> Si, como colaborador, agregaste erróneamente el mensaje del commit, lo puedes cambiar de la siguiente manera:

> Hacer un commit con el nuevo mensaje que queremos, esto nos abre el editor de texto de la terminal:

```sh

git commit —amend #Corregimos el mensaje
git pull origin main #Traer el repositorio remoto
git push --set-upstream origin main #Ejecutar el cambio, el error arreglado
```

> Comienzo del colaborador

```sh
cd Documentos #Abre git bash
mkdir class-git #Crea la carpeta o directorio de trabajo
ls -al #Revisa lo que va haciendo, los archivos o directorios que tiene
# 1. No debe hacer un git init, debe buscar el repositorio en el cual esta invitado a participar, por supuesto en GitHub.
# 2. Pasa a clonar desde HTTPS, copiar la url, esto es porque no se arranca el proyecto desde cero, se esta uniendo otro colaborador.
# 3. En git bash ponemos el siguiente comando.
git clone url-copiada-github #Esto hace que clonemos el repositorio
# 4. No pide ni usuario ni contraseña si el repositorio es publico.
code . #Abre VSC y comienza con cambios, o abre el siguiente comando para hacer modificaciones
vim historia.txt #Vamos a escribir: Aquí esta un nuevo colaborador
vim escribimos el mensaje del commit #Esto en Ubuntu
ctrl + x
s #Para un si
enter #Terminado el mensaje del commit
vim escribimos el mensaje del commit #Esto en git bash window
esc #Presionamos escaner luego de terminar de escribir
:wq! #Para salir del editor vim en window
git status
git commit -am "Mi primer commit, estoy muy emocionado!!!"
git pull origin main
git fetch
gti branch #Para ver las ramas que se trajo, no se trae sino solo main, si hay mas debes crearlas local
git log #Para ver toda las historia
git log --graph #Vemos el grafico de las diferentes ramas y del commit que acabamos de hacer que esta en el main, Git es una base de datos de toda las historia de todo lo que se ha hecho
git push origin main #Va a pedir un email que será el del colaborador, su contraseña.
# 5. Nos trae un denegado, ¿Por qué? Porque en el proceso de abordaje el jefe no le dio acceso: el dueño del repositorio no le agregó dandole acceso.
# 6. Ir a settings del repositorio, veremos la opsión Collaborators, agregamos el correo o nombre de usuario: el colaborador debe tener un email publico y visible o de otra manera debera ser con el nombre de usuario publico: ingresar el username y debe ir como colaborador.
# 7. Se puede enviar un email con la url, pero ya GitHub envia una notificación al usuario de invitado, es una cosa que debemos empezar a consultar y revisar.
# 8. El colaborador debe aceptar la invitación, una vez hecho eso ya tendrá total acceso para hacer push al repositorio.
git pull origin main
git push origin main #Colocar nombre de usuario y contraseña, listo
# 9. El dueño del repositorio no ve los cambios, ¿Qué hacer?
git pull origin main
git fetch
git log --stat #Se verá claro que el colaborador ingreso su primer commit
# 10. A partir de ahora el dueño del repositorio y el colaborador deberán repartir el trabajo, esto se hace con distintas ramas de trabajo: el dueño trabajará desde la rama header y el colaborador desde la rama footer, al final cuando se termine, se hara un merge para terminar el proyecto.
```

## Portafolio

Capitulo 8: Creacion de Componente Habilidades.

# CLASE 10 MIÉRCOLES 16 DE OCTUBRE DEL 2024 - Portafolio 10

**Flujo de trabajo profesional**

**Haciendo merge de ramas de desarrollo a main**

> Para poder desarrollar software de manera óptima y ordenada, necesitamos tener un flujo de trabajo profesional, que nos permita trabajar en conjunto sin interrumpir el trabajo de otros desarrolladores.

> Una buena práctica de flujo de trabajo sería la siguiente:

### Crear ramas

<sub>Asignar una rama a cada programador</sub>
<sub>El programador baja el repositorio con git pull origin master</sub>
<sub>El programador cambia de rama</sub>
<sub>El programador trabaja en esa rama y hace commits</sub>
<sub>El programador sube su trabajo con git push origin #nombre_rama</sub>
<sub>El encargado de organizar el proyecto baja, revisa y unifica todos los cambios</sub>

## PORTAFOLIO

<sub>Capitulo 9: Creacion de componente Intereses y Footer.</sub>

# CLASE 11 MIÉRCOLES 23 DE OCTUBRE DEL 2024 - Portafolio 11

<sub>Flujo de trabajo profesional -> Archivos binarios</sub>

> Las imagenes cargandolas en el repositorio, representan un problema: porque las imagenes son pesadas, y si la subimos al repositorio, siempre que hagamos cambios, vamos a estar trayendo la imagen siempre, estas imagenes son binarios para GitHub, mientras mas binarios carguemos, más pesado va a ser el repositorio, algo que no es parte de las buenas practicas.


> Otra cosa muy importante a tener en cuenta, es que en cada commit que hagamos hay un tamaño predefinido para la carga, este no lo podemos superar o no podremos subir los commits, el tamaño es 100 mb, si acoplamos un archivo binario en un commit que pese mas de esto, será un problema, no nos dejará seguir commiteando, porque siempre seguirá arrastrando el archivo binario.

## Portafolio

<sub>Capítulo 10: Build del Portafolio Vuejs y manejo de activos estáticos</sub>
<sub>Despliegue de portafolio en Netlify - Github</sub>
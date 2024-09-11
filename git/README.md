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


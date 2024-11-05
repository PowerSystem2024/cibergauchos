<!--CLASE 6-->
<script setup>
import { ref } from 'vue';
const arreglo = ref([
    { id: 1, fecha: '2024', titulo: 'Proyectos y Colaboraciones', descripcion: 'Hemos participado en proyectos colaborativos, utilizando Git y Github y hemos desarrollado aplicaciones web completas.Nuestro enfoque ha sido optimizar el codigo y seguir las mejores practicas.', enlace: "http:www.proyectos.com" },
    { id: 2, fecha: '2023', titulo: 'Frameworks y Librerias', descripcion: 'Empezamos a trabajar con frameworks como React y Vue.js para construir aplicaciones web dinamicas y eficientes.Tambien exploramos Node.js para el desarrollo del lado del servidor.', enlace: "http:www.aplicaciones.com" },
    { id: 3, fecha: '2022', titulo: 'JavaScript y Desarrollo Web', descripcion: 'Profundizamos en el desarrollo web al aprender JavaScript. Desarrollamos sitios web interactivos y aprendimos sobre la manipulacion del DOM y AJAX.', enlace: "http:www.JavaScript.com" },
    { id: 4, fecha: '2021', titulo: 'HTMLY CSS', descripcion: 'Aprendimos a crear paginas web estaticas usando HTML y darles estilos con CSS.Dominar las etiquetas HTML basicas y las propiedades CSS nos permitio diseñar paginas atractivas.', enlace: "http:www.HTMLyCSS.com" },
    { id: 5, fecha: '2020', titulo: 'Introduccion a la Programacion', descripcion: 'Comenzamos nuestro viaje aprendiendo los fundamentos de la programacion con Python y C. Desarrollamos una solida base en la logica de programacion y algoritmos.', enlace: "http:www.programacion.com" }
]);
</script>

<template>
    <ul>
        <li v-for="item in arreglo" :key="item.id">
            <div class="fecha"> {{ item.fecha }}</div>
            <div class="titulo">{{ item.titulo }}</div>
            <div class="descripcion">{{ item.descripcion }}</div>
            <a class="enlace">{{ item.enlace }}</a>
        </li>
    </ul>
</template>

<style scoped>
ul {
    border-left: 3px solid;
    margin-left: 2rem;
    color: var(--vt-c-indigo);
}

li {
    list-style: decimal;
    padding-left: 1rem;
    color: var(--vt-c-indigo);
    font-weight: bold;
}

.fecha {
    padding-left: 1rem;
    background-color: var(--vt-c-indigo);
    color: white;
    font-weight: bold;
}

.titulo {
    display: flex;
    justify-content: center;
    color: white;
    ;
}

.descripcion {
    padding: 1 rem;
    color: var(--vt-c-indigo);
    font-weight: 500;
}

.enlace {
    display: flex;
    justify-content: center;
    color: rgb(16, 57, 172);
}
</style>

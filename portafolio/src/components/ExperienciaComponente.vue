<script setup>
import icono1 from '/src/assets/node-js.svg';
import icono2 from '/src/assets/collaboration.svg';
import icono3 from '/src/assets/github-svgrepo-com.svg';
import icono4 from '/src/assets/postgresql.svg';
import icono5 from '/src/assets/programming.svg';
import {ref} from 'vue';
const titulo='Desarrolladores Full Stack';
const fecha='Desde Marzo 2022 / Octubre 2023';
const experiencias = ref([
    {id:1, src:icono1, parrafo: 'Desarrollo y mantenimiento de sitios web corporativos utilizando React y Node.'},
    {id:2, src:icono2, parrafo: 'Colaboraciones con el equipo de diseño para implementar interfaces accesibles.'},
    {id:3, src:icono3, parrafo: 'Realizacion de pruebas de codigo y mantenimiento del repositorio Git.'},
    {id:4, src:icono4, parrafo: 'Implementaciones de base de datos PostgreSQL y consultas SQL para optimizacion de datos.'},
    {id:5, src:icono5, parrafo: 'Implementacion de componentes de React para aplicaciones web interactivas.'},
]);
</script>

<template>
    <div class="card">
        <h3 class="titulo">{{ titulo.toLocaleUpperCase() }}</h3>
        <p class="fecha">{{ fecha }}</p>
        <ul class="listado">
            <li class="item" v-for="experencia in experiencias" :key="experencia.id">
                <img class="imagen-svg" :src="experencia.src" width="45rem" :alt="experencia.parrafo">
                <p>{{ experencia.parrafo }}</p>
            </li>
        </ul>
    </div>
</template>

<style scoped>
.card{
    display: flex;
    flex-direction: column;
    padding: 2rem;
    background-color: var(--vt-c-indigo);
    border-radius: 15px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
}
.titulo{
    font-size: 1.5rem;
    color: white;
    font-weight: bold;
}
.fecha{
    font-size: 1rem;
    font-weight: bold;
    color: #ceb793;
    margin-bottom: 1rem;
}
.listado{
    display: flex;
    flex-direction: column;
    color: white;
}
.item{
    align-items: center;
    display: flex;
    padding: 1rem;
    gap: 1.5rem;
}

</style>

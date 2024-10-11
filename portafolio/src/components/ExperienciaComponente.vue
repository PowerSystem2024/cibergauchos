<script setup>
import {ref} from 'vue';
const titulo='Desarrolladores Full Stack';
const fecha='Desde Marzo 2022 / Octubre 2023';
const experiencias = ref([
    {id:1, src:'/src/assets/node-js.svg', parrafo: 'Desarrollo y mantenimiento de sitios web corporativos utilizando React y Node.'},
    {id:2, src:'/src/assets/collaboration.svg', parrafo: 'Colaboraciones con el equipo de diseño para implementar interfaces accesibles.'},
    {id:3, src:'/src/assets/github-svgrepo-com.svg', parrafo: 'Realizacion de pruebas de codigo y mantenimiento del repositorio Git.'},
    {id:4, src:'/src/assets/postgresql.svg', parrafo: 'Implementaciones de base de datos PostgreSQL y consultas SQL para optimizacion de datos.'},
    {id:5, src:'/src/assets/programming.svg', parrafo: 'Implementacion de componentes de React para aplicaciones web interactivas.'},
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
    background-color: rgb(85, 63, 126);
    border-radius: 15px;
}
.titulo{
    font-size: 1.5rem;
    color: rgb(247, 58, 10);
}
.fecha{
    font-size: 1rem;
    color: rgb(20, 20, 20);
    margin-bottom: 1rem;
}
.listado{
    display: flex;
    flex-direction: column;
}
.item{
    align-items: center;
    display: flex;
    padding: 1rem;
    gap: 1.5rem;
}

</style>

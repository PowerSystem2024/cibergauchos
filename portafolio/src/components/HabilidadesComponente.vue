<script setup>
import {ref} from "vue"
import habilidad1 from "../assets/javascript.svg"
import habilidad2 from "../assets/python.svg"
import habilidad3 from "../assets/java.svg"
import habilidad5 from "../assets/vue.svg"
import habilidad6 from "../assets/sql.svg"
import habilidad7 from "../assets/html.svg"
import habilidad8 from "../assets/css.svg"
import habilidad9 from "../assets/git.svg"
import habilidad10 from "../assets/github-svgrepo-com.svg"



const languajes = ref([
    {id:1, src: habilidad1, title: "JavaScript", alt:"Languaje"},
    {id:2, src: habilidad2, title: "Python", alt:"Languaje"},
    {id:3, src: habilidad3, title: "Java", alt:"Languaje"},
    {id:5, src: habilidad5, title: "VueJS", alt:"Languaje"},
    {id:6, src: habilidad6, title: "MySQL", alt:"Languaje"},
    {id:7, src: habilidad7, title: "HTML", alt:"Languaje"},
    {id:8, src: habilidad8, title: "CSS",  alt:"Languaje"},
    {id:9, src: habilidad9, title: "Git", alt:"Languaje"},
    {id:10, src: habilidad10, title: "GitHub", alt:"Languaje"},

])
</script>

<template>
    <div class="card-container">
        <div class="card" v-for="lenguaje in languajes" :key="lenguaje.id">
            <div class="img-container">
                <img :src="lenguaje.src" class="img-lenguaje">
            </div>
            <div class="title-container">
                <h3 class="title-lenguaje">{{ lenguaje.title }}</h3>
            </div>
        </div>
    </div>
</template>

<style scoped>
.card-container{
    width: 100%;
    background-color:  var(--vt-c-indigo);;
    height: auto;
    margin-top: 0.7rem;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 2rem;
    flex-wrap: wrap;
    padding: 2rem;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
    border-radius: 1.2rem;
}

.card{
    width: 250px;
    height: auto;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 0.3rem 1rem;
    border-radius: 1.2rem;
    background-color: rgba(255, 255, 255, 0.15);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
    transition: all 300ms ease-in-out;
}

.card:hover{
    transform: scale(1.1);
    background-color: rgba(240, 255, 255, 0.13);
}

.img-lenguaje{
    width: 70px;
    height: 100px;
}

.title-lenguaje{
    color: #fff;
    font-weight: 600;
    font-size: 1.2rem;
}

</style>
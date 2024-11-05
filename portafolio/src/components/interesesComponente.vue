<script setup>
import { ref } from 'vue';

import Fondolava from './FondoLava.vue';

//Este es un arreglo con ref para que se pueda reactivar el cambio de los intereses.
const intereses = ref([
    'Desarrollo de software de Código Abierto: contribuimos a proyectos en Github, colaborando con equipos de desarrolladores para mejorar herramientas y librerías populares.',
    'Deportes: Jugamos Pádel ya que es un deporte donde no hay contacto y todos nos podemos divertir pasando hermosos momentos juntos.',
    'Tecnología de Innovación: Nos apasionan las nuevas tendencias tecnológicas como la inteligencia artificial y el desarrollo de aplicaciones móviles, entre otras.',
    'Diseño: nos apasiona la idea de un entorno innovador que sea agradable al usaurio en varios dispositivos para que tenga una experiencia agradable al utilizar las aplicaciones que desarrollamos.'
]);
</script>

<template>
    <div class="intereses-contenedor">
        <fondolava />
        <ul class = "contenedor-lista">
            <li class="items" v-for = "intereses in intereses" :key = "interes">
                •	  {{ intereses }}
            </li>

        </ul>
    </div>
  <!---  <div class="intereses-contenedor">
            <ul class="contenedor-lista">
                <li class="item">
                    Desarrollo de software de Código Abierto: contribuyo a proyectos en Github, colaborando con otros desarrolladores para mejorar herramientas y libreriías populares.
                </li>
                
                <li class="item">
                    Deportes al Aire Libre: Disfruto del senderismo y el cliclismo de montaña, actividades que practico regularmente para mantener un equilibrio entre el trabajo y la vida personal.
                </li>
                
                <li class="item">
                    Tecnología de Innovación: Me apasiona explorar nuevas tendencias tecnológicas como la inteligencia artificial y el desarrollo de aplicaciones móviles.
                </li>
                
                <li class="item">
                    Fotografía: Practico la fotografía como un hobby, lo que me ayuda a mantener una perspectiva creativa tanto en mi vida profesional como personal.
                </li>
            </ul>
    </div>-->
</template>

<style scoped>
.intereses-contenedor {
    display: flex;
    position: relative;
    margin: 0 auto;
    max-width: 85%;
    padding: 1rem;
}
.contenedor-lista{
    list-style-type: none;
    padding: 1rem;
    margin-bottom: .5rem;
    color: var(--vt-c-white-soft);
    font-size: 1.4rem;
    text-shadow:3px 3px 6px rgba(0, 0, 0, 1)
}
.item {
    margin-bottom: 1rem;   
}

</style>
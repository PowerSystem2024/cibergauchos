<script setup>
import DatosPersonales from './components/DatosPersonales.vue'
import NavBar from './components/NavBar.vue'
import Educacion from './components/EducacionComponente.vue';
import ExperienciaComponente from './components/ExperienciaComponente.vue';
import ProyectosComponente from './components/ProyectosComponente.vue';
import HabilidadesComponente from './components/HabilidadesComponente.vue';
</script>

<template>
  <header>
    <!-- Navbar -->
    <NavBar />
    <!-- Componente Datos Personales -->
    <DatosPersonales />
  </header>
  <main>
    <!--Componente Educacion-->
    <section id="educacion">Educacion - Cursos</section>
    <Educacion />
    <section id="experiencia">Experiencia</section>
    <ExperienciaComponente />
    <section id="proyectos">Proyectos</section>
    <ProyectosComponente />
    <section id="habilidades">Habilidades</section>
    <HabilidadesComponente />
    <section id="intereses">Intereses</section>
  </main>
</template>

<style scoped></style>

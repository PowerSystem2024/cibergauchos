<script setup>
import DatosPersonales from './components/DatosPersonales.vue'
import NavBar from './components/NavBar.vue'
</script>

<template>
  <header>
    <!-- Navbar -->
    <NavBar />
    <!-- Componente Datos Personales -->
    <DatosPersonales />
  </header>
  <main>
    <section id="educacion">Educacion - Cursos</section>
    <section id="experiencia">Experiencia</section>
    <section id="proyectos">Proyectos</section>
    <section id="habilidades">Habilidades</section>
    <section id="intereses">Intereses</section>
  </main>
</template>

<style scoped></style>

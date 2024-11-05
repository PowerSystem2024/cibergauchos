<script setup>
import DatosPersonales from './components/DatosPersonales.vue'
import NavBar from './components/NavBar.vue'
import Educacion from './components/EducacionComponente.vue';
import ExperienciaComponente from './components/ExperienciaComponente.vue';
import ProyectosComponente from './components/ProyectosComponente.vue';
import HabilidadesComponente from './components/HabilidadesComponente.vue';
import interesesComponente from './components/interesesComponente.vue';
</script>

<template>
  <header id="top">
    <!-- Navbar -->
    <NavBar />
    <!-- Componente Datos Personales -->
    <DatosPersonales />
  </header>
  <main>
    <!--el estilo css de section se encuenttra en base.css-->

    <section id="educacion">
      <h2>Educacion - Cursos</h2>
      <!--Componente Educación-->
      <Educacion />
    </section>

    <section id="experiencia">
      <h2>Experiencia</h2>
      <!--Componente Experiencia-->
      <ExperienciaComponente />
    </section>

    <section id="proyectos">
      <h2>Proyectos</h2>
      <!--Componente Proyectos-->
      <ProyectosComponente />
    </section>

    <section id="habilidades">
      <!--Componente Habilidades-->
      <h2>Habilidades</h2>
      <HabilidadesComponente />
    </section>

    <section id="intereses">
      <!--Componente Habilidades-->
      <h2>Intereses</h2>
      <interesesComponente />
    </section>
  </main>
  <footer>
    <a href="#top">Inicio</a>
    <p>@ 2024 Equipo de desarrollo CiberGauchos</p>
  </footer>
</template>

<style scoped>
main h2 {
  color: var(--vt-c-indigo);
  font-weight: bold;
  margin-bottom: 1rem;
}

footer {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 2rem;
  font-size: 1.3rem;
}
</style>

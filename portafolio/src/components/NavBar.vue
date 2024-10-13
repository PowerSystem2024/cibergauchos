<script setup>
import { ref } from 'vue'
const navegacion = ref([
  { id: 1, nombre: 'Educación', enlace: '#educacion' },
  { id: 2, nombre: 'Experiencia', enlace: '#experiencia' },
  { id: 3, nombre: 'Proyectos', enlace: '#proyectos' },
  { id: 4, nombre: 'Habilidades', enlace: '#habilidades' },
  { id: 5, nombre: 'Intereses', enlace: '#intereses' }
])
</script>

<template>
  <nav class="navbar">
    <div class="navbar-menu">
      <ul class="nav-list">
        <li v-for="nav in navegacion" :key="nav.id" class="nav-item">
          <a :href="nav.enlace">{{ nav.nombre }}</a> <!--Se coloco el operador v-bind al atributo href utilizando su minima exprecion el operador : / y se soluciono el enlace a las distintas secciones-->
        </li>
      </ul>
    </div>
  </nav>
</template>

<style scoped>
.navbar {
  background-color: var(--vt-c-indigo);
  color: #fff;
  padding: 0.5rem 1rem;
  align-items: center;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
}
.navbar-menu {
  display: flex;
  justify-content: flex-end;
}

.nav-list {
  display: flex;
  justify-content: flex-end;
  gap: 1rem;
}
.nav-item {
  font-size: 1.05rem;
  list-style: none;
}
a {
  color: #dadada;
  text-decoration: none;
  transition: 0.2s;
  padding: 5px;
}
a:hover {
  color: white;
}
@media (max-width: 768px) {
  .navbar-menu {
    display: flex;
    justify-content: flex-end;
    width: 100%;
  }
}
</style>

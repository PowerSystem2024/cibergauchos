<script setup>
import linkedin from '/src/assets/linkedin-icon.svg';
import instagram from '/src/assets/instagram-icon.svg';
import github from '/src/assets/github-icon.svg';
import portafolio from '/src/assets/file-icon.svg';
const nombre = 'Grupo Cibergauchos'
const ocupacion = 'Técnicos Universitarios en Programación - UTN'
const residencia = 'Mendoza, Argentina'
const presentacion =
  'Bienvenido al portafolio de proyectos del grupo Cibergauchos. Somos desarrolladores con experiencia en aplicaciones web y móviles.'
const telefono = '+54 9 2634-563212'
const redesSociales = [
  {
    id: 1,
    name: 'instagram',
    src: instagram,
    url: 'https://www.instagram.com/'
  },
  {
    id: 2,
    name: 'linkedin',
    src: linkedin,
    url: 'https://www.linkedin.com/'
  },
  {
    id: 3,
    name: 'github',
    src: github,
    url: 'https://github.com/PowerSystem2024/cibergauchos'
  },
  {
    id: 4,
    name: 'portafolio',
    src: portafolio,
    url: 'https://github.com/PowerSystem2024/cibergauchos'
  }
]
</script>
<template>
  <section class="datos-personales">
    <div class="card">
      <h1>{{ nombre }}</h1>
      <h2>{{ ocupacion }}</h2>
      <p>{{ presentacion }}</p>
      <ul class="contacto-lista">
        <li v-for="redSocial in redesSociales" :key="redSocial.id">
          <a :href="redSocial.url"><img class="icon-redSocial" :src="redSocial.src" width="35rem"
              :alt="redSocial.name" /></a>
        </li>
      </ul>
      <h3>Nuestro teléfono de contacto: {{ telefono }}</h3>
      <h4>{{ residencia }}</h4>
    </div>
  </section>
</template>
<style scoped>
.datos-personales {
  margin: 1.5rem 0;
}

.card {
  padding: 1rem;
  border-radius: 1.2rem;
  background-color: var(--vt-c-indigo);
  color: var(--vt-c-white-mute);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

h1 {
  font-size: 2rem;
  margin-bottom: 0.8rem;
  font-weight: 700;
}

h2 {
  margin-bottom: 0.5rem;
  font-weight: 600;
}

p {
  font-size: 1.1rem;
  width: 70%;
  text-align: center;
}

h3,
h4 {
  font-weight: 600;
}

.contacto-lista {
  margin-top: 2rem;
  display: flex;
  list-style: none;
  gap: 1rem;
}

.icon-redSocial {
  filter: invert(75%);
  transition: 0.2s;
}

.icon-redSocial:hover {
  filter: invert(100%);
  transition: 0.2s;
}
</style>

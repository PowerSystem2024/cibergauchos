<script setup>
const intereses = [{
    titulo: "Desarrollo de software de Código Abierto",
    descripcion: "contribuimos a proyectos en Github, colaborando con equipos de desarrolladores para mejorar herramientas y librerías populares.",
},
{
    titulo: "Tecnología de Innovación",
    descripcion: "Nos apasionan las nuevas tendencias tecnológicas como la inteligencia artificial y el desarrollo de aplicaciones móviles, entre otras."
},
{
    titulo: "Diseño",
    descripcion: "nos apasiona la idea de un entorno innovador que sea agradable al usaurio en varios dispositivos para que tenga una experiencia agradable al utilizar las aplicaciones que desarrollamos."
}];
</script>

<template>
    <div class="intereses_container">
        <ul class="list_intereses">
            <li v-for="interes in intereses" :key="interes">
                <span>{{ interes.titulo }}</span> : {{ interes.descripcion }}
            </li>
        </ul>
    </div>
</template>

<style scoped>
.intereses_container {
    display: flex;
    justify-content: center;
    padding: 1rem;
    border-radius: 1.2rem;
    background-color: var(--vt-c-indigo);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
}

.list_intereses {
    max-width: 1000px;
    list-style: none;
    gap: 0.7rem;
    padding: 1.5rem;
    text-align: left;
}

.list_intereses li {
    color: rgb(223, 223, 223);
    font-size: 1.1rem;
    font-weight: 500;
    list-style: circle;
}

.list_intereses li span {
    color: #ceb793;
    font-weight: bold;
}
</style>
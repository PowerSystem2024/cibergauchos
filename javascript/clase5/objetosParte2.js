// Objeto (Forma más utilizada y más básica)
let persona = {
    nombre: 'Ulises',
    apellido: 'Sánchez',
    email: 'ulisessanchezcarp2004@gmail.com',
    edad: 20,
    idioma: 'es',
    nombreCompleto: function(){ // Agregamos un método o funcion a un objeto.
        return this.nombre+' '+this.apellido;
    },
    set lang(lang){
        this.idioma = lang.toUpperCase();
    },
    get nombreEmail(){ // Este es el método Get
        return 'El nombre es: '+this.nombre+' y su email es: '+this.email;
    },
    get lang(){
        return this.idioma.toUpperCase();
    }
}

// Método Get "Obtener"  (Llamar una función) (Línea 14)
console.log('COMENZAMOS A USAR EL MÉTODO GET: ');
console.log(persona.nombreEmail);

// Método Set () (Linea 11)
console.log('COMENZAMOS A USAR EL MÉTODO SET PARA IDIOMAS');
persona.lang = "en";
console.log(persona.lang);

function Persona3(nombre, apellido, email){ // (Constructor) 
    this.nombre = nombre;
    this.apellido = apellido;
    this.email = email;
    this.nombreCompleto = function(){
        return this.nombre+' '+this.apellido;
    }
}
let padre = new Persona3('Agustin', 'Lorca', 'agustinlorca@probando.com'); // Método para creacion de objetos
console.log(padre);
console.log(padre.nombreCompleto())
// Modificamos el nombre
padre.nombre = 'Agustinnn';
console.log(padre.nombreCompleto());
// Asignamos un nuevo id a la funcion:
padre.telefono = 12345678;
console.log(padre);

let madre = new Persona3('Laura', 'Contrera', 'laucontrera@probando.com');
console.log(madre);
console.log(madre.nombreCompleto());
// Si mostramos un id sin datos se muestra undefined.
console.log(madre.telefono);

// Diferentes formas de crear objetos:
// N° 1.
let miObjeto = new Object(); // Opcion Formal.

// N° 2.
let miObjeto2 = {}; // Breve y Recomendada.

// Caso Tipo String:
// N° 1.
let miCadena1 = new String('Hola Mundo'); // Sintaxis formal tipo String.

// N° 2.
let miCadena2 = 'Hola Mundo'; // Sintaxis simplificada y recomendada.

// Caso con Números:
// N° 1.
let miNumero = new Number(1); // Sintaxis Formal, pero no recomendable.

// N° 2.
let miNumero2 = 1; // Sintaxis recomendada.

// Caso Booleanos:
// N° 1:
let miBoolean1 = new Boolean(false); // Sintaxis Formal.

// N° 2: 
let miBoolean2 = false; // Sintaxis Recomendada.

// Caso arrays:
// N° 1:
let miArreglo1 = new Array(); // Sintaxis Formal.

// N° 2:
let miArreglo2 = []; // Sintaxis Recomendada.

// Caso Fuction:
// N° 1:
let miFuction1 = new function(){}; // Tener en cuenta que todo despues del new es considerado objeto.

// N° 2:
let miFuction2 = function(){}; // Notación Simplificada y recomendada.
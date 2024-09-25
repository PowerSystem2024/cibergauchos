let x = 10; //variable de tipo primitiva
console.log(x.length); 
console.log('Tipos primitivos');
//Objeto
let persona = {
    nombre: 'Ulises',
    apellido: 'Sánchez',
    email: 'ulisessanchezcarp2004@gmail.com',
    edad: 20,
    idioma: 'es',
    get lang(){
        return this.idioma.toUpperCase(); //Convierte las minusculas en mayusculas
    },
    set lang(lang){
        this.idioma = lang.toUpperCase();
    },
    nombreCompleto: function(){ //metodo o funcion en JavaScript
        return this.nombre+' '+this.apellido;
    },
    get nombreEdad(){ //Este es el metodo get
        return 'El hombre es: '+this.nombre+', Edad: '+this.edad;
    },
 
}

console.log(persona.nombre);
console.log(persona.apellido);
console.log(persona.email);
console.log(persona.edad);
console.log(persona)
console.log(persona.nombreCompleto());
console.log('Ejecutando con un objeto');

//1.3
let persona2 = new Object(); //Debe crear un nuevo objeto en memoria
persona2.nombre = 'Juan';
persona2.direccion = 'Salada 14';
persona2.telefono = '5492604092853';
console.log(persona2.telefono);
console.log('Creamos un nuevo objeto');
console.log(persona['apellido']); //Accedemos como si fuera un arreglo
console.log('Usamos el ciclo for in');
//for in y accedemos al objeto como si fuera un arreglo
for(propiedad in persona){
    console.log(propiedad);
    console.log(persona[propiedad]);

}
console.log('cambiamos y eliminamos un error');
persona.apellida = 'Gonzalez'; //Cambiamos dinamicamente un valor del objeto
delete persona.apellida; //Eleiminamos el error
console.log(persona);

//Distinta formas de imprimir un objeto
//Numero 1: la mas sencilla: concatenar cada valor de cada propiedad
console.log('Distinta formas de imprimir un objeto: forma 1');
console.log(persona.nombre+', '+persona.apellido);

//Numero 2: A travez del ciclo for in
console.log('Distinta formas de imprimir un objeto: forma 2');
for(nombrePropiedad in persona){
    console.log(persona[nombrePropiedad]);
}

//Numero 3: La funcion Objetct.values()
console.log('Distinta formas de imprimir un objeto: forma 3');
let personaArray = Object.values(persona);
console.log(personaArray);

//Numero 4: Utilizaremos el metodo JSON.stringify
console.log('Distinta formas de imprimir un objeto: forma 4');
let personaString = JSON.stringify(persona);
console.log(personaString);


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
let padre = new Persona3('Leo', 'Lopez','lopez@gmail.com' );
padre.nombre = 'Luis'; //modificamos el nombre
padre.telefono = '5492604657835'; //Una propiedad exclusiva del objeto padre
console.log(padre);
console.log(padre.nombreCompleto()); //Utilizamos la funcion
let madre = new Persona3('Laura', 'Contrera', 'contrera@gmail.com');
console.log(madre);
console.log(madre.telefono); //la propiedad no esta definida
console.log(madre.nombreCompleto());

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

//Uso de prototype
Persona3.prototype.telefono = '2604277671';
console.log(padre);
console.log(madre.telefono);
madre.telefono = '5492604277671';
console.log(madre.telefono);

//Uso de call
let persona4 = {
    nombre: 'Juan',
    apellido: 'Perez',
    nombreCompleto2: function(titulo, telefono){
        return titulo+': '+this.nombre+' '+this.apellido+' '+telefono;
        //return this.nombre+' '+this.apellido;
    }
}

let persona5 = {
    nombre: 'Carlos',
    apellido: 'Lara'
}

console.log(persona4.nombreCompleto2('Lic.', '5492604848401'));
console.log(persona4.nombreCompleto2.call(persona5, 'Ing.', '5492604505152'));

//Metodo Apply
let arreglo = ['Ing.', '5492604313233'];
console.log(persona4.nombreCompleto2.apply(persona5, arreglo));


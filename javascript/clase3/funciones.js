//FUNCIONES:Clase 3 
miFuncion(8, 2); //Esto se le conoce hoisting

function miFuncion(a, b){
   // console.log("Sumamos: "+ (a + b));
   return a + b;
}

//Llamando la funcion
miFuncion(5, 4);

let resultado = miFuncion(6, 7);
console.log(resultado);

//Declaramos una funcion de tipo expresion o anonima 
let x = function(a, b){ return a + b}; //necesita cierre con punto y coma 
resultado = x(5, 6); //al llamarla se pone la variable y parentesis 
console.log(resultado);

//Funciones de tipo self y invoking
(function(a, b){
    console.log('Ejecutando la funcion: '+ (a + b));
})(9, 6);

console.log(typeof miFuncion);
function miFuncionDos(a, b){
    console.log(arguments.lenght);
}

miFuncionDos(5, 7, 3, 6);

//toString
var miFuncionTexto = miFuncionDos.toString();
console.log(miFuncionTexto);

// ---------- Funciones flechas ----------------
// No se usa la palabra reservada "function" ni "return"
// No se usan las llaves

const sumarFuncionFlecha = (a,b) => a * b;
resultado = sumarFuncionFlecha(3,5); //La asignamos a una variable
console.log(resultado);


// Parámetros: es la lista de variables que definimos en una función
// Argumentos: son los valores que pasamos cuando llamamos a una función

// Función tipo expresión
let sumar = function(a = 1, b = 2){ 

    // muestra el parámetro de a
    console.log(arguments[0]);

    // muestra el parámetro de b
    console.log(arguments[1]);

    // muestra el tercer argumento
    console.log(arguments[2]);

    return a + b + arguments[2];
}

// en JS no es requerido que coincidan el n° de argumentos con el n° de parámetros

resultado = sumar(2,6,7); 

console.log(resultado);


// ------------ Concepto de hoisting -------------------

// En JS, siempre y cuando no usemos la sintaxis de función de flecha, podemos aplicar el concepto de "hoisting"
// Esto quiere decir que podemos usar la función en una parte del archivo antes de haberla declarado

// Primero llamamos a la función

let respuesta = sumarTodo (2,4,6,8,10);

console.log(respuesta);

// Luego la declaramos

function sumarTodo(){
    let suma = 0;
    for(let i = 0; i < arguments.length ; i++){
        suma += arguments[i];
    }
    return suma;
}


// ------------- Paso por valor -------------------
// Los tipos primitivos se pasan por valor (number, sring, boolean, undefined, null, symbol)

let y = 10;

function cambiarValor(a){ // Pasamos una copia del valor de la variable y
    a = 20;
}
// La variable y al ser un tipo primitivo, JS los pasa por valor, es decir, se pasa una copia
// del valor a la función, y los cambios realizados en el parámetro dentro de la función no afectan
// a la variable original fuera de la función

cambiarValor(y);

console.log(y); // La variable y no sufre cambios

// ------------- Paso por referencia -------------------
// Los objetos y los arrays se pasan por referencia

const persona = { 
    nombre: "Jorge",
    apellido: "Perez",
    edad: 42
}
console.log(persona);

function cambiarValorObjeto(p1){ // Paso del objeto persona por referencia
    p1.nombre = "Jose";
    p1.apellido = "Lopez";
    p1.edad = 50
}
// Cuando pasamos el objeto persona, no se crea una copia del objeto, sino que la variable p1
// apunta a la misma dirección en memoria que el objeto persona. Esto quiere decir que,
// cualquier modificación en el objeto dentro de la función, afecta al objeto original

cambiarValorObjeto(persona); 

console.log(persona);


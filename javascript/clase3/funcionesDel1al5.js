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



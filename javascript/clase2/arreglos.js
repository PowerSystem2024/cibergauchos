//* Arreglos */


//let autos = new Array('Ford','BMW','Fiat'); // sintaxis antigua

const autos = ['Ford','BMW','Fiat'];
console.log(autos);

// Acceder a un elemento del arreglo con un índice de forma manual

console.log("autos[0] = " + autos[0]);
console.log("autos[2] = " + autos[2]);

// Iterar mediante ciclo for

for(let i = 0; i < autos.length; i++){
    console.log(i + ": " + autos[i]);
}

// Modificar los elementos de un arreglo

autos[1] = "Audi";
console.log(autos);

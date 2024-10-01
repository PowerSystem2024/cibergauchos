class Person{ // Clase Padre
  constructor(nombre, apellido){
      this._nombre = nombre; // Tener en cuenta que inicializamos con el _ para que no sea igual al del método get.
      this._apellido = apellido;
  } 

  get nombre(){
      return this._nombre;  
  }

  set nombre(nombre){
      this._nombre = nombre;
  }

  get apellido(){
      return this._apellido;  // Inicializamos el método get para apellido
  }

  set apellido(apellido){
      this._apellido = apellido; // Inicializamos el método get para apellido
  }  

}

let personOne = new Person('Nahuel', 'Molino');
console.log(personOne.nombre);
personOne.nombre = "Danilo";
console.log(personOne.nombre)
//console.log(personOne);
let personTwo = new Person('Ulises', 'Sánchez');
console.log(personTwo.nombre);
personTwo.nombre = "Agustin";
console.log(personTwo.nombre)
//console.log(personaTwo);


// A PARTIR DE ACÁ MI PARTE:
personOne.apellido = "PietroPaolo";  //Mediante el set cambiamos el apellido y luego lo mostramos por consola.
console.log(personOne.apellido)

personTwo.apellido = "Lorca";      //Mediante el set cambiamos el apellido y luego lo mostramos por consola.
console.log(personTwo.apellido)

class Empleado extends Person{ // Clase Hija
  constructor(nombre, apellido, departamento){ //Tener en cuenta que hay que llamar al constructor de la clase padre y sus parámetros.
      super(nombre, apellido);
      this.departamento = departamento;
  }
  
  get departamento(){
      return this._departamento;
  }

  set departamento(departamento){
      this._departamento = departamento;
  }
}

let empleado1 = new Empleado('Lionel Andres', 'Messi', 'Jugador Profesional');
console.log(empleado1); // Mostramos por consola el objeto empleado 1.
console.log(empleado1.nombre) // Mostramos solo el nombre del objeto empleado 1

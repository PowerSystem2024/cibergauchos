class Persona {
  constructor(name, lastName) {
    this._name = name;
    this._lastName = lastName;
  }

  get name() {
    return this._name;
  }

  set name(name) {
    this._name = name;
  }

  get lastName() {
    return this._lastName;
  }

  set lastName(lastName) {
    this._lastName = lastName;
  }
}

let persona1 = new Persona("Mariano", "Bondar");
console.log(persona1.name);
console.log(persona1.lastName);
persona1.name = "Juan";
console.log(persona1.name);
persona1.lastName = "Perez";
console.log(persona1.lastName);
//console.log(persona1);
let persona2 = new Persona("Agusto", "Martinez");
console.log(persona2.name);
persona2.name = "Pedro";
console.log(persona2.name);
persona2.lastName = "Enriquez";
console.log(persona2.lastName);
//console.log(persona2);

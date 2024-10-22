class Persona{//clase Padre

    static contadorObjetosPersona = 0;//Atributo estático
    email = 'Valor default email';//Atributo no estático
    
    constructor(nombre, apellido){
        this._nombre = nombre;
        this._apellido = apellido;
        Persona.contadorObjetosPersona++;
        console.log('Se incrementa el contador: '+Persona.contadorObjetosPersona);
    }

    get nombre(){
        return this._nombre;
    }

    set nombre(nombre){
        this._nombre = nombre;
    }

    get apellido(){
        return this._apellido;
    }

    set apellido(apellido){
        this._apellido = apellido;
    }

    nombreCompleto(){
        return this._nombre+' '+this._apellido;
    }
    //Sobreescribiendo el método de la clase padre (Object)
    toString(){//regresa un String
        //Se aplica el polimorfismo que significa = multiples formas en tiempo de ejecución
        //El método que se ejecuta depende si es una referencia de tipo padre o hija
        return this.nombreCompleto();
    }

    static saludar(){
        console.log('saludos desde este método static');
    }

    static saludar2(persona){
        console.log(persona.nombre+' '+persona.apellido);
    }
}

class Empleado extends Persona{//clase hija
    constructor(nombre, apellido, departamento){
        super(nombre, apellido);
        this._departamento = departamento;
    }

    get departamento(){
        return this._departamento;
    }

    set departamento(departamento){
        this._departamento = departamento;
    }

    //sobreescritura
    nombreCompleto(){
        return super.nombreCompleto()+', '+this._departamento;
    }
}

let persona1 = new Persona('Martin', 'Palermo');
console.log(persona1.nombre);
persona1.nombre = 'Titan';
console.log(persona1.nombre);
//console.log(persona1);
let persona2 = new Persona('Juan', 'Riquelme');
console.log(persona2.nombre);
persona2.nombre = 'Juan Roman';
console.log(persona2.nombre);
//console.log(persona2);

let empleado1 = new Empleado('Luciano', 'Marquez', 'Sistemas');
console.log(empleado1);
console.log(empleado1.nombreCompleto());

//Object.prototype.toString Esta es la manera de acceder a atributos y métodos de manera dinamica
console.log(empleado1.toString());
console.log(persona1.toString());

//persona1.saludar(); no se utiliza desde el Objeto
Persona.saludar();
Persona.saludar2(persona1);

Empleado.saludar();
Empleado.saludar2(empleado1);

//console.log(persona1.contadorObjetosPersona);
console.log(Persona.contadorObjetosPersona);
console.log(Empleado.contadorObjetosPersona);

console.log(persona1.email);
console.log(empleado1.email);
//console.log(Persona.email); No puede acceder desde la clase


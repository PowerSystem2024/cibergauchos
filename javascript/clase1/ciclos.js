// while

let counter = 0;

while(counter < 3){
    console.log(counter)
    counter++;
}

console.log("End of while cycle")

// do while

let counter2 = 0;

do{
    console.log(counter2)
    counter2++;
} while (counter2 < 3)

console.log("End of do while cycle")

// for

for (let i = 0; i < 3 ; i++ ) {
    console.log(i)
}

console.log("End of for cycle")

// reserved word break

for(let j=0; j<=10; j++){
    if(j % 2 == 0){
        console.log(j)
        break;
    }
}
console.log("first even number found")

// reserved word continue

for(let j=0; j<=10; j++){
    if(j % 2 !== 0){
        continue; // goes to next iteration
    }
    console.log(j)
}
console.log("shows even numbers")

// labels

start:
for(let j=0; j<=10; j++){
    if(j % 2 !== 0){
        break start; // goes to next iteration
    }
    console.log(j)
}
console.log("completed cycle")
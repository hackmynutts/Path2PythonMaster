////////////MAP////////////
let x = [1, 2, 3, 55, 334, 5667];

let y = x.map((x) => x * x);

for (const valor of y) {
  console.log("El cuadrado del numero es: " + valor);
}

console.log("\n");

//////////FILTER////////////

let numeros = [1, 2, 3, 55, 334, 5667];

console.log("\n");
console.log("El arreglo es: " + numeros);
let pares = numeros.filter((x) => x % 2 === 0);
for (const valor of pares) {
  console.log("El par en el arreglo es: " + valor);
}
console.log("\n");

//////////REDUCE////////////

console.log("\n");
let platosCena = [12300, 10200, 13330, 10245, 8450, 9900];

console.log("Los precios de cada plato fueron de: " + platosCena);

let total = platosCena.reduce((a, b) => a + b, 0);
let propina = total * 0.13;

console.log("La cena ha salido en un total de: " + total + " ya con IVA.");

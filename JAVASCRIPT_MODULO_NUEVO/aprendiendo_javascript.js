// 1. Tortilla de patatas
function tortilla() {
  let c = +prompt("Número de comensales:");
  alert(`Para ${c} comensales necesitas:
  ${c * 300}g de patatas, ${Math.ceil((c * 300 / 1000) * 4)} huevos, ${(c * 300 / 1000) * 250}g de cebolla`);
}

// 2. Intercambio de variables
function intercambiar() {
  let a = prompt("Valor de A:");
  let b = prompt("Valor de B:");
  [a, b] = [b, a]; // más fácil con destructuring
  alert(`Ahora A=${a}, B=${b}`);
}

// 3. Edad de perro a humanos
function edadPerro() {
  let edad = +prompt("Edad del perro en años:");
  alert(`La edad del perro en años humanos es ${edad * 7} años.`);
}

// 4. Triángulo de asteriscos
function triangulo() {
  let out = "";
  for (let i = 1; i <= 9; i++) out += "*".repeat(i) + "\n";
  alert(out);
}

// 5. Calcular impuestos
function calcularImpuestos() {
  let edad = +prompt("Edad:");
  let ingresos = +prompt("Ingresos:");
  alert("Impuesto: " + (edad >= 18 && ingresos >= 1000 ? ingresos * 0.4 : 0));
}

// 6. Likes
function likes() {
  let n = +prompt("Número:");
  if (n < 1000) alert(n.toString());
  else if (n < 1_000_000) alert((n / 1000).toFixed(1) + "K");
  else alert((n / 1_000_000).toFixed(1) + "M");
}

// 7. FizzBuzz
function fizzBuzz() {
  let n = +prompt("Número:");
  alert(n % 15 === 0 ? "fizzbuzz" : n % 3 === 0 ? "fizz" : n % 5 === 0 ? "buzz" : n);
}

// 8. Número de "a"
function numeroDeAes() {
  let texto = prompt("Texto:");
  alert(`Número de 'a': ${texto.toLowerCase().split("a").length - 1}`);
}

// 9. Remover ceros
function removerCeros() {
  let arr = prompt("Números separados por comas:").split(",").map(Number);
  alert("Sin ceros: " + arr.filter(Boolean).join(", "));
}

// 10. Transcribir ADN a ARN
function transcribir() {
  let mapa = { G: "C", C: "G", T: "A", A: "U" };
  let adn = prompt("Cadena de ADN:").toUpperCase();
  alert("ARN: " + adn.split("").map(c => mapa[c] || "").join(""));
}

// 11. Password
function password() {
  let res = prompt("Texto:")
    .toLowerCase()
    .replace(/\s/g, "")
    .replace(/a/g, "4")
    .replace(/e/g, "3")
    .replace(/i/g, "1")
    .replace(/o/g, "0");
  alert("Password: " + res);
}

password()
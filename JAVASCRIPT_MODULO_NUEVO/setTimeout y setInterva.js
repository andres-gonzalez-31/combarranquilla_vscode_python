
// Ejercicios con setTimeout y setInterval en
///////////////////JavaScript////////////////


// 1.Muestra un mensaje de 'Bienvenido!' después de 3 segundos usando setTimeout.

// function saludos() {
//   console.log('Bienvenido');
// }
// setTimeout(saludos, 3000);


// 2. Crea un contador regresivo de 5 a 0 que muestre los números en la consola cada segundo con
// setTimeout.
// function contadorRegresivo() {
//   for (let i = 5; i >= 0; i--) {
//     setTimeout(() =>{
//         console.log(i);
//     }, (5 - i) * 1000);
//     };
//   } 
// contadorRegresivo();


// 3.Usa setTimeout para mostrar tres mensajes diferentes: 'Hola' (1s), '¿Cómo estás?' (2s) y
// 'Adiós' (3s).
//   setTimeout(() => {
//     console.log('Hola');
//   }, 1000);
//   setTimeout(() => {
//     console.log('como estas? ');
//   }, 2000);
//   setTimeout(() => {
//     console.log('adios');
//   }, 3000);

// 4.Crea una función temporizador(mensaje, tiempo) que muestre un mensaje en consola después
// del tiempo indicado en milisegundos.

// function temporizador(mensaje, tiempo) {
//   setTimeout(() => {
//     console.log(mensaje);
//   }, tiempo);
// }

// temporizador('Este es un mensaje de prueba', 2000);



//5. Simula la carga de datos mostrando 'Cargando...' y después de 3 segundos 'Datos cargados
// ■'.

// function cargarDatos() {
//    console.log('Cargando...');
//    setTimeout(() => {
//       console.log('Datos cargados');
//    }, 3000); // <- aquí va el tiempo
// }

// cargarDatos();


//6. Haz una ejecución en cadena con setTimeout para mostrar 'Paso 1', luego 'Paso 2' al segundo
// siguiente y 'Paso 3' al otro segundo.

// function pasos() {
//   setTimeout(() => {
//     console.log("Paso 1");
//     setTimeout(() => {
//       console.log("Paso 2");
//       setTimeout(() => {
//         console.log("Paso 3");
//       }, 1000); 
//     }, 1000); 
//   }, 1000);
// }

// pasos();


//7.  Crea un reloj digital que muestre la hora actual en consola actualizada cada segundo con
// setInterval.

// function relojDigital() {
//   setInterval(() => {
//     let ahora = new Date(); // obtiene la fecha y hora actual
//     let horas = ahora.getHours().toString().padStart(2, '0');
//     let minutos = ahora.getMinutes().toString().padStart(2, '0');
//     let segundos = ahora.getSeconds().toString().padStart(2, '0');

//     console.log(`${horas}:${minutos}:${segundos}`);
//   }, 1000); // se ejecuta cada 1 segundo
// }

// relojDigital();


//8. Haz un reloj digital con setTimeout usando recursividad.

function relojConsola() {
  const ahora = new Date();
  const h = String(ahora.getHours()).padStart(2, '0');
  const m = String(ahora.getMinutes()).padStart(2, '0');
  const s = String(ahora.getSeconds()).padStart(2, '0');

  console.clear();             // opcional: limpiar la consola para ver solo la última hora
  console.log(`${h}:${m}:${s}`);

  // Llamada recursiva con setTimeout para ejecutar otra vez en ~1s
  setTimeout(relojConsola, 1000);
}

// Inicia el reloj
relojConsola();
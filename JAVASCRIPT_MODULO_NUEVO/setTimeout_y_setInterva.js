
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
// function relojConsola() {
//   const ahora = new Date();
//   const h = String(ahora.getHours()).padStart(2, '0');
//   const m = String(ahora.getMinutes()).padStart(2, '0');
//   const s = String(ahora.getSeconds()).padStart(2, '0');
//   console.clear();             
//   console.log(`${h}:${m}:${s}`);
//   // Llamada recursiva con setTimeout para ejecutar otra vez en ~1s
//   setTimeout(relojConsola, 1000);
// }
// // Inicia el reloj
// relojConsola();


// 9 Crea un cronómetro que inicie desde 0 y vaya aumentando cada segundo en consola con setInterval.

// let segundos = 0;
// let cronometro = setInterval(() => {
//   console.log(segundos++);
// }, 1000);


// 10 Haz que un mensaje parpadee en consola alternando 'ON' y 'OFF' cada 500ms usando setInterval.
// let estado = true;
// setInterval(() => {
//   console.log(estado ? "ON" : "OFF");
//   estado = !estado;
// }, 500);

// 11 Usa setInterval para mostrar una tabla de multiplicar del 5, mostrando un resultado nuevo cada 2 segundos.
// let i = 1;
// let tabla = setInterval(() => {
//   console.log(`5 x ${i} = ${5 * i}`);
//   i++;
//   if (i > 10) clearInterval(tabla);
// }, 2000);

// 12 Crea una animación de texto que vaya mostrando las letras de la palabra 'JAVASCRIPT' una por una cada 700ms.
// let texto = "JAVASCRIPT";
// let pos = 0;
// let animacion = setInterval(() => {
//   console.log(texto[pos]);
//   pos++;
//   if (pos >= texto.length) clearInterval(animacion);
// }, 700);

// 13 Haz que se muestre un chiste diferente de un array de 5 chistes cada 3 segundos con setInterval. 
// let chistes = [
//   "¿Qué le dijo un techo a otro? Techo de menos.",
//   "¿Por qué la computadora fue al médico? Porque tenía un virus.",
//   "¿Qué le dijo una impresora a otra? ¿Esa hoja es tuya o es una impresión mía?",
//   "¿Por qué los pájaros no usan Facebook? Porque ya tienen Twitter.",
//   "¿Qué hace una abeja en el gimnasio? ¡Zum-ba!"
// ];
// let idx = 0;
// setInterval(() => {
//   console.log(chistes[idx]);
//   idx = (idx + 1) % chistes.length;
// }, 3000);


// 14 Usa setTimeout para simular un semáforo: 'Rojo' (3s), 'Verde' (2s), 'Amarillo' (1s), y vuelve a comenzar.
// function semaforo() {
//   console.log("Rojo");
//   setTimeout(() => {
//     console.log("Verde");
//     setTimeout(() => {
//       console.log("Amarillo");
//       setTimeout(semaforo, 1000);
//     }, 1000);
//   }, 2000);
// }
// semaforo();

//  15 Crea un programa que detenga un setInterval después de que haya ejecutado 10 repeticiones.
// let count = 0;
// let intervalo = setInterval(() => {
//   console.log("Repetición:", ++count);
//   if (count === 10) clearInterval(intervalo);
// }, 1000);

  // 16 Simula un cargador de progreso que muestre en consola: '10%', '20%', ..., '100%' usando setInterval.
// let progreso = 10;
// let loader = setInterval(() => {
//   console.log(progreso + "%");
//   progreso += 10;
//   if (progreso > 100) clearInterval(loader);
// }, 500);

  //  17 Crea una función que use setTimeout para mostrar un recordatorio cada 10 segundos, pero solo 3 veces.
// let veces = 0;
// function recordatorio() {
//   if (veces < 3) {
//     console.log(" Recordatorio número " + (veces + 1));
//     veces++;
//     setTimeout(recordatorio, 10000);
//   }
// }
// recordatorio();


    // 18 Haz un programa que muestre los números pares del 2 al 20 con un retardo de 1 segundo entre cada número. 
// let num = 2;
// let pares = setInterval(() => {
//   console.log(num);
//   num += 2;
//   if (num > 20) clearInterval(pares);
// }, 1000);



    // 19 Usa setInterval para mostrar la fecha completa (día, mes, año, hora, minuto, segundo) cada 5 segundos.
// setInterval(() => {
//   let ahora = new Date();
//   console.log(ahora.toLocaleString()); 
// }, 5000);


    //  20 Combina setTimeout y setInterval para iniciar un cronómetro después de 5 segundos de espera.
// setTimeout(() => {
//   let t = 0;
//   setInterval(() => {
//     console.log("Cronómetro:", t++);
//   }, 1000);
// }, 5000);

  
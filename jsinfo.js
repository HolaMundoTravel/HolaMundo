

function TraerDatosBariloche() {
    fetch("https://api.openweathermap.org/data/2.5/weather?lat=-41.133472&lon=-71.310280&lang=es&units=metric&appid=e0221905178300ae64543a4636e22847")

        .then(datos => datos.json())
        .then(datos => {
            console.log(datos)
            apibar.innerHTML +=
            `<div class="contenedor-api"> 
                <u class="hola">- Temperatura actual en ${datos.name} -</u> 
                <span class="grados">${Math.trunc(datos.main.temp_max)}ºc </span>
                <span class="humedad">${datos.main.humidity}% de humedad</span>
                <div class="contenedor-iconapi">
 <span><img class="iconAPI" src="https://openweathermap.org/img/w/${datos.weather[0].icon}.png"></span>
            <span>${datos.weather[0].description}</span>
            </div>
            </div>
            `
})
}
console.log(TraerDatosBariloche())


function TraerDatosRio() {
    fetch("https://api.openweathermap.org/data/2.5/weather?lat=-22.906847&lon=-43.172897&lang=es&units=metric&appid=e0221905178300ae64543a4636e22847")

        .then(datos => datos.json())
        .then(datos => {
            console.log(datos)
            apibr.innerHTML +=
            `<div class="contenedor-api"> 
                <u class="hola">- Temperatura actual en ${datos.name} -</u> 
                <span class="grados">${Math.trunc(datos.main.temp_max)}ºc </span>
                <span class="humedad">${datos.main.humidity}% de humedad</span>
                <div class="contenedor-iconapi">
 <span><img class="iconAPI" src="https://openweathermap.org/img/w/${datos.weather[0].icon}.png"></span>
            <span>${datos.weather[0].description}</span>
            </div>
            </div>
            `
})
}
console.log(TraerDatosRio())

function TraerDatosCol() {
    fetch("https://api.openweathermap.org/data/2.5/weather?lat=4.60971&lon=-74.08175&lang=es&units=metric&appid=e0221905178300ae64543a4636e22847")

        .then(datos => datos.json())
        .then(datos => {
            console.log(datos)
            apicol.innerHTML +=
            `<div class="contenedor-api"> 
                <u class="hola">- Temperatura actual en ${datos.name} -</u> 
                <span class="grados">${Math.trunc(datos.main.temp_max)}ºc </span>
                <span class="humedad">${datos.main.humidity}% de humedad</span>
                <div class="contenedor-iconapi">
 <span><img class="iconAPI" src="https://openweathermap.org/img/w/${datos.weather[0].icon}.png"></span>
            <span>${datos.weather[0].description}</span>
            </div>
            </div>
            `
})
}
console.log(TraerDatosCol())

function TraerDatosMen() {
    fetch("https://api.openweathermap.org/data/2.5/weather?lat=-32.89084&lon=-68.82717&lang=es&units=metric&appid=e0221905178300ae64543a4636e22847")

        .then(datos => datos.json())
        .then(datos => {
            console.log(datos)
            apimen.innerHTML +=
            `<div class="contenedor-api"> 
                <u class="hola">- Temperatura actual en ${datos.name} -</u> 
                <span class="grados">${Math.trunc(datos.main.temp_max)}ºc </span>
                <span class="humedad">${datos.main.humidity}% de humedad</span>
                <div class="contenedor-iconapi">
 <span><img class="iconAPI" src="https://openweathermap.org/img/w/${datos.weather[0].icon}.png"></span>
            <span>${datos.weather[0].description}</span>
            </div>
            </div>
            `
})
}
console.log(TraerDatosMen())

function TraerDatosLis() {
    fetch("https://api.openweathermap.org/data/2.5/weather?lat=38.71667&lon=-9.13333&lang=es&units=metric&appid=e0221905178300ae64543a4636e22847")

        .then(datos => datos.json())
        .then(datos => {
            console.log(datos)
            apilis.innerHTML +=
            `<div class="contenedor-api"> 
                <u class="hola">- Temperatura actual en Lisboa -</u> 
                <span class="grados">${Math.trunc(datos.main.temp_max)}ºc </span>
                <span class="humedad">${datos.main.humidity}% de humedad</span>
                <div class="contenedor-iconapi">
 <span><img class="iconAPI" src="https://openweathermap.org/img/w/${datos.weather[0].icon}.png"></span>
            <span>${datos.weather[0].description}</span>
            </div>
            </div>
            `
})
}
console.log(TraerDatosLis())

function mostrarInfo(){
    document.querySelector(".Evento-info").classList.toggle("hover-eventoinfo");
    document.querySelector(".evento-img").classList.toggle("hover-img");
}

function ocultarInfo(){
    document.querySelector(".Evento-info").classList.toggle("hover-eventoinfo");
    document.querySelector(".evento-img").classList.toggle("hover-img");
}

var productImg = document.querySelector(".evento-img")
productImg.addEventListener("mouseover",mostrarInfo)
productImg.addEventListener("mouseout",ocultarInfo)
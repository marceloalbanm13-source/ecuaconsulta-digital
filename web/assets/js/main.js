/*==================================================
ECUACONSULTA DIGITAL
Landing Oficial v1.0
==================================================*/

document.addEventListener("DOMContentLoaded", () => {

    /*=========================================
    HEADER
    =========================================*/

    const header = document.querySelector(".header");

    window.addEventListener("scroll", () => {

        header.classList.toggle("scrolled", window.scrollY > 40);

    });

    /*=========================================
    MENÚ MÓVIL
    =========================================*/

    const menuButton = document.querySelector(".menu-toggle");
    const navbar = document.querySelector(".navbar");

    menuButton.addEventListener("click", () => {

        navbar.classList.toggle("active");

    });

    /*=========================================
    CERRAR MENÚ
    =========================================*/

    document.querySelectorAll(".navbar a").forEach(link => {

        link.addEventListener("click", () => {

            navbar.classList.remove("active");

        });

    });

    /*=========================================
    BOTÓN VOLVER ARRIBA
    =========================================*/

    const backTop = document.createElement("button");

    backTop.className = "back-top";

    backTop.setAttribute("aria-label", "Volver arriba");

    backTop.innerHTML = '<i class="fa-solid fa-arrow-up"></i>';

    document.body.appendChild(backTop);

    window.addEventListener("scroll", () => {

        backTop.classList.toggle("show", window.scrollY > 500);

    });

    backTop.addEventListener("click", () => {

        window.scrollTo({

            top:0,

            behavior:"smooth"

        });

    });

    /*=========================================
    ANIMACIONES
    =========================================*/

    const observer = new IntersectionObserver((entries)=>{

        entries.forEach(entry=>{

            if(entry.isIntersecting){

                entry.target.classList.add("visible");

            }

        });

    },{

        threshold:.15

    });

    document.querySelectorAll(

        ".card,.timeline-item,.guide-book,.solution-card,.why-card"

    ).forEach(el=>{

        observer.observe(el);

    });

});
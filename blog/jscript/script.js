let nav = document.querySelector(".nav");
let blank = document.querySelector(".blank");
let logo = document.getElementById("darklogo");
let header = document.getElementById("header");

// -----------------------------------------Header nav----------------------------------------
window.onscroll = function () {
    scrollFunction();
};

function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        logo.setAttribute("src", "img/logo-dark.png");
        nav.style.transition = 'all 0.5s ease-in-out';
        nav.style.padding = ('15px 0px');
        nav.style.background = "white";
        nav.style.boxShadow = "0 2px 8px 3px rgba(0, 0, 0, 0.05)";
        blank.style.color = "black";
    } else {
        logo.setAttribute("src", "img/logo.png");
        nav.style.transition = 'all 0.5s ease-in-out';
        nav.style.padding = ('20px 0px');
        nav.style.background = "none";
        nav.style.boxShadow = "none";
        blank.style.color = "white";
    };
};
//--------------------------------------------

document.addEventListener('DOMContentLoaded', function () {
    var typed = new Typed('#typed', {
        stringsElement: '#typed-strings',
        typeSpeed: 200,
        backSpeed: 100,
        startDelay: 1000,
        cursorChar: '|',
        loop: true,
        fadeOut: false,
        loopCount: Infinity,
    });
});
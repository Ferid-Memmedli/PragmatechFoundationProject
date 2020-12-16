let nav = document.querySelector(".nav");
let mybutton = document.getElementById("myBtn");
let blanks = document.querySelectorAll(".blank");
let logo = document.getElementById("darklogo");
let sections = document.querySelectorAll("section");
let header = document.getElementById("header");

// -----------------------------------------Header nav----------------------------------------
window.onscroll = function () {
    scrollFunction();
    scrl();
};

function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        logo.setAttribute("src", "img/logo-dark.png");
        nav.style.transition = 'all 0.5s ease-in-out';
        nav.style.padding = ('15px 0px');
        nav.style.background = "white";
        nav.style.boxShadow = "0 2px 8px 3px rgba(0, 0, 0, 0.05)";
        mybutton.style.display = "block";
        blanks.forEach(i => {
            i.style.color = "black";
        });
    } else {
        logo.setAttribute("src", "img/logo.png");
        nav.style.transition = 'all 0.5s ease-in-out';
        nav.style.padding = ('20px 0px');
        nav.style.background = "none";
        nav.style.boxShadow = "none";
        mybutton.style.display = "none";
        blanks.forEach(i => {
            i.style.color = "white";
        });
    };
};
// -------------------------------button top---------------------------------
mybutton.onclick = function () {
    var a = document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
};

// ------------------------------- Our client bolmesi ucun yazilmis JS kodlari
let dots = document.querySelectorAll('.aktiv1');
dots.forEach(i => {
    i.addEventListener('click', e => {
        dots.forEach(i => i.classList.remove('active'))
        e.target.classList.add('active')
    })
})


let akt1 = document.querySelector('#active1');
let akt2 = document.querySelector('#active2');
let akt3 = document.querySelector('#active3');
let ata = document.querySelector('#ata');

akt1.onclick = function () {
    ata.style.left = '0px';
};
akt2.onclick = function () {
    ata.style.left = '-1100px';
};
akt3.onclick = function () {
    ata.style.left = '-2200px';
};

//----------------------Scroll menu--------------------
function scrl() {
    if  (scrollY > header.offsetTop) {
        blanks[0].classList.add("isik");
        blanks[1].classList.remove("isik");
    }
    if (scrollY > sections[0].offsetTop - 40) {
        blanks[0].classList.remove("isik");
        blanks[1].classList.add("isik");
        blanks[2].classList.remove("isik");
    }
    if (scrollY > sections[1].offsetTop - 40) {
        blanks[1].classList.remove("isik");
        blanks[2].classList.add("isik");
        blanks[3].classList.remove("isik");
    }
    if (scrollY > sections[2].offsetTop - 40) {
        blanks[2].classList.remove("isik");
        blanks[3].classList.add("isik");
        blanks[4].classList.remove("isik");
    }
    if (scrollY > sections[3].offsetTop - 40) {
        blanks[3].classList.remove("isik");
        blanks[4].classList.add("isik");
        blanks[5].classList.remove("isik");
    }
    if (scrollY > sections[4].offsetTop - 40) {
        blanks[4].classList.remove("isik");
        blanks[5].classList.add("isik");
        blanks[6].classList.remove("isik");
    }
    if (scrollY > sections[5].offsetTop - 40) {
        blanks[5].classList.remove("isik");
        blanks[6].classList.add("isik");
    }
};

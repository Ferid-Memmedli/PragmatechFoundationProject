// -----------------------------------------Header nav----------------------------------------
let nav = document.querySelector(".nav");
let mybutton = document.getElementById("myBtn");
let blanks = document.querySelectorAll(".blank");
let logo = document.getElementById("darklogo");
let sections = document.querySelectorAll(".section");
window.onscroll = function () {
    scrollFunction();
    scrl();
};

function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        logo.setAttribute("src", "img/logo-dark.png");
        nav.style.transition = 'all 0.5s ease-in-out';
        nav.style.background = "white";
        nav.style.boxShadow = "0 2px 8px 3px rgba(0, 0, 0, 0.05)";
        mybutton.style.display = "block";
        blanks.forEach(i => {
            i.style.color = "black";
        });
    } else {
        logo.setAttribute("src", "img/logo.png");
        nav.style.transition = 'all 0.5s ease-in-out';
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

//----------------------Problem-----------------
// let sections = document.querySelectorAll("section");
// let blanks = document.querySelectorAll(".blank");
// for (let i = 0; i < sections.length; i++) {
//     for (let b = 0; b < blanks.length; b++) {
//         if (scrollY > sections[i].offsettop) {
//             blanks[b].classList("isik");
//         }
//     }
// }
function scrl() {
    if (scrollY > 0) {
        blanks[0].classList.add("isik");
        blanks[1].classList.remove("isik");
    }
    if (scrollY > 610) {
        blanks[0].classList.remove("isik");
        blanks[1].classList.add("isik");
        blanks[2].classList.remove("isik");
    }
    if (scrollY > 1230) {
        blanks[1].classList.remove("isik");
        blanks[2].classList.add("isik");
        blanks[3].classList.remove("isik");
    }
    if (scrollY > 2420) {
        blanks[2].classList.remove("isik");
        blanks[3].classList.add("isik");
        blanks[4].classList.remove("isik");
    }
    if (scrollY > 3130) {
        blanks[3].classList.remove("isik");
        blanks[4].classList.add("isik");
        blanks[5].classList.remove("isik");
    }
    if (scrollY > 4000) {
        blanks[4].classList.remove("isik");
        blanks[5].classList.add("isik");
        blanks[6].classList.remove("isik");
    }
    if (scrollY > 4840) {
        blanks[5].classList.remove("isik");
        blanks[6].classList.add("isik");
    }
};
// -----------------------------------------Header nav----------------------------------------
let nav = document.querySelector(".nav");
let a = document.querySelectorAll(".blank");
let mybutton = document.getElementById("myBtn");

window.onscroll = function () {
    scrollFunction();
};

function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        nav.style.transition = 'all 0.5s ease-in-out';
        nav.style.background = "white";
        nav.style.boxShadow = "0 2px 8px 3px rgba(0, 0, 0, 0.05)";
        mybutton.style.transition = 'all 0.5s ease';
        mybutton.style.display = "block";
        // a.forEach(i => {
        //     i.addEventListener('mouseover', function () {
        //         i.style.transition = "all 0.5s";
        //         i.style.color = "#e65f78";
        //     });
        //     i.addEventListener('mouseout', function () {
        //         i.style.transition = "all 0.5s";
        //         i.style.color = "black";
        //     });
        // });
        a.forEach(i => {
            i.style.color = "black";
        });
    } else {
        nav.style.transition = 'all 0.5s ease-in-out';
        nav.style.background = "none";
        nav.style.boxShadow = "none";
        mybutton.style.transition = 'all 0.5s ease';
        mybutton.style.display = "none";
        // a.forEach(i => {
        //     i.addEventListener('mouseover', function () {
        //         i.style.transition = "all 0.5s";
        //         i.style.color = "#e65f78";
        //     });
        //     i.addEventListener('mouseout', function () {
        //         i.style.transition = "all 0.5s";
        //         i.style.color = "white";
        //     });
        // });
        a.forEach(i => {
            i.style.color = "white";
        });
    };
};

// ------------------------------- Our client bolmesi ucun yazilmis JS kodlari
let dots = document.querySelectorAll('.aktiv1')
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

akt1.addEventListener('click', function () {
    ata.style.left = '0px';
});

akt2.addEventListener('click', function () {
    ata.style.left = '-1100px';
});

akt3.addEventListener('click', function () {
    ata.style.left = '-2200px';
});

// -------------------------------button top---------------------------------

function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
};

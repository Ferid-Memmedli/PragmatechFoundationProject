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

//----------------------Scroll menu--------------------
function scrl() {
    blanks.forEach(i => i.classList.remove('isik'));
    if (scrollY > sections[5].offsetTop - 45) {
        blanks[6].classList.add("isik");
    } else if (scrollY > sections[4].offsetTop - 45) {
        blanks[5].classList.add("isik");
    } else if (scrollY > sections[3].offsetTop - 45) {
        blanks[4].classList.add("isik");
    } else if (scrollY > sections[2].offsetTop - 45) {
        blanks[3].classList.add("isik");
    } else if (scrollY > sections[1].offsetTop - 45) {
        blanks[2].classList.add("isik");
    } else if (scrollY > sections[0].offsetTop - 45) {
        blanks[1].classList.add("isik");
    } else {
        blanks[0].classList.add("isik");
    }
};

// ---------------------------Formdan melumat goturmeq-------------------------------------
// const form = document.forms[0];

// form.addEventListener("submit", function (event) {
//     event.preventDefault();
//     const { name, email, subject, comments } = this.elements;
//     console.log(name.value, email.value, subject.value, comments.value);
// });

const form = document.forms[0];

form.addEventListener("submit", function (event) {
    event.preventDefault();
    const formData = new FormData(this);

    for (const formElement of formData) {
        console.log(formElement);
    }
});

let nav = document.querySelector(".nav");
let blanks = document.querySelectorAll(".blank");

// -----------------------------------------Header nav----------------------------------------
window.onscroll = function () {
    scrollFunction();
};

function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        nav.style.transition = 'all 0.5s ease-in-out';
        nav.style.padding = ('15px 0px');
        nav.style.background = "white";
        // nav.style.boxShadow = "0 2px 8px 3px rgba(0, 0, 0, 0.05)";

    } else {
        nav.style.transition = 'all 0.5s ease-in-out';
        nav.style.padding = ('20px 0px');
        nav.style.background = "none";
        // nav.style.boxShadow = "none";

    };
};

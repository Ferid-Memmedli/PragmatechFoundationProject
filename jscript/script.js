/* let a=50;
document.querySelector(".btn").addEventListener('click',function(){
    // let box=document.createElement("div")
    // box.className="box"
    // a++
    // box.innerHTML=a
    // let container=document.querySelector('.container')
    // container.appendChild(box)
})
    a=a+100
    let box=document.querySelector(".box");
    box.style.left=a+"px";
------------------------------------------------------
x=1
setInterval(function(){
var randX=Math.floor(Math.random()*1000);
var randY=Math.floor(Math.random()*1000);
console.log(randX,randY)
let div=document.createElement("div")
div.className="circle";
div.style.left=randX+'px'
div.style.top=randY+'px'
document.body.appendChild(div)
},100)*/

// -----------------------------------------Header nav----------------------------------------
let nav = document.querySelector(".nav");
let a = document.querySelectorAll(".blank");


window.onscroll = function () {
    scrollFunction()
};

function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        nav.style.transition = 'all 0.5s ease-in-out';
        nav.style.background = "white";
        nav.style.boxShadow = "0 2px 8px 3px rgba(0, 0, 0, 0.050980392156862744)";
        a.forEach(i => {
            i.addEventListener('mouseover', function() {
                i.style.color = "#e65f78";
            });
            i.addEventListener('mouseout', function() {
                i.style.color = "black";
            });
        });
        for (i in a) {
            a[i].style.color = "black";
        }
    } else {
        nav.style.transition = 'all 0.5s ease-in-out';
        nav.style.background = "none";
        nav.style.boxShadow = "none";
        a.forEach(i => {
            i.addEventListener('mouseover', function() {
                i.style.color = "#e65f78";
            });
            i.addEventListener('mouseout', function() {
                i.style.color = "white";
            });
        }); 
        for (i in a) {
            a[i].style.color = "white"
        }
    }
}

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

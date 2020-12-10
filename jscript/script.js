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
-----------------------------------------------------------------
function ClickEvent(){
    console.log("Hello World")
}
let nextBtn=document.querySelector(".btn-next");
let prevBtn=document.querySelector(".btn-prev");
let slider=document.querySelector('.slider-items');
a=1;
nextBtn.addEventListener("click",function(){

    a+=600;
    slider.style.left=a+'px';
})

prevBtn.addEventListener("click",function(){

    a-=600;
    slider.style.left=a+'px';
})
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

// ------------------------------- Our client bolmesi ucun yazilmis JS kodlari
var dots = document.querySelectorAll('.aktiv1')
dots.forEach(i => {
    i.addEventListener('click', e => {
        dots.forEach(i => i.classList.remove('active'))
        e.target.classList.add('active')
    })
})

var akt1 = document.querySelector('#active1');
var akt2 = document.querySelector('#active2');
var akt3 = document.querySelector('#active3');
var ata = document.querySelector('#ata')

akt1.addEventListener('click',function(){
    ata.style.left = '0px'
});

akt2.addEventListener('click', function () {
    ata.style.left = '-1100px'
});

akt3.addEventListener('click',function(){
    ata.style.left = '-2200px'
});

var counter=document.querySelector('.counter')
var count = 0

function add_1() {
   // alert("+1")
   count+=1
   counter.textContent=count
}

var counter2=document.querySelector('.counter2')

function add_2() {
   // alert("+2")
   count+=2
   counter2.textContent=count
   document.write(x, "\n");
   document.write(y, "\n");
}

let saved = document.querySelector(".saved")
function save(){
   let saveStr = count + "--"
   saved.textContent += saveStr
   count=0
   counter.textContent=count
}

let rand_button = document.querySelector(".rand_but")

function teleport(){
   let x= window.innerWidth* Math.random() //mult width  with random number
   let y = window.innerHeight * Math.random()
   rand_button.style.left = x + 'px' // left & top  - css settings
   rand_button.style.top = y + 'px'

}
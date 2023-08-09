
let counter=document.querySelector('.counter')
let count = 0

function add_1() {
   // alert("+1")
   count+=1
   counter.textContent=count
}
let saved = document.querySelector(".saved")
function save(){
   let saveStr = count + "--"
   saved.textContent += saveStr
   count=0
   counter.textContent=count
}
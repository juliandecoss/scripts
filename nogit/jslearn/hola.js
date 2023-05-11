let a = 1;
let b = 1;
a+=1;

//console.log("Hola mundo perracos: "+`${a}`);
//console.log("Hola mundo perracos: "+`${b++}`);
// alt ? para sacar el alrevés \ y alt+ } para sacarlos ``
//console.log("Escapando de los \"strings\" o 'strings'"+`${b++}`);
// length
let len = "Tengo un len de 18"
//console.log(len.length)
//console.log(len[len.length-1])
function miprimerfuncion(a,b){
   return a+b
}
//console.log(miprimerfuncion(13,6))
obj ={"hoola":{"vamos a ver":12}}
var str = JSON.stringify(obj, null, 2);

//console.log(str)
let arrei = ["hola","pedro"]
arrei.unshift("saber")
//console.log(arrei)
console.log(1!=true)
console.log(true!==1)
let prue = ""
console.log(typeof(prue))
if(!prue){
   console.log("EL NOT DE JS")
}
if(prue){
   console.log("ME PARESCO A PYTHON");
}
else if(typeof(prue)=="string"){
   console.log("Te CACHÉ perraco");
}
if(typeof(prue)=="string"){
   console.log("TE CACHÉ 2 VECES CAMARADA")
}
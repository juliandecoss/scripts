function spinWords(string){
   solucc2 = ""
   spliteado = string.split(" ");
   for(word of spliteado){
    if(word.length >= 5){word = word.split("").reverse().join("");}
    if(spliteado.indexOf(word)!= 0){solucc2 += " ";}
    solucc2 += word;
   }
   return solucc2;
}

console.log(spinWords("Hey fellow warriors"))
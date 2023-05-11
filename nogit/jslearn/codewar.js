//9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
function parseodenum(num){
    let new_num = "";
    let string_num = num.toString();
    concatenado = string_num.split("");
    concatenado.forEach(element => {
        new_num += (Math.pow(parseInt(element),2)).toString();
    });
    return new_num;
}
console.log(parseodenum(9119))
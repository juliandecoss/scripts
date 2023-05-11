
var hexadecimal = {0:"0",1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
function convert_rgb_to_hex(number){
    if (number > 255){
        return "FF";
    }
    f= number/16;
    f1 = hexadecimal[Math.floor(f)];
    f2 = hexadecimal[f%1*16];
    return f1+f2;
}
function rgb(r,g,b){
    r = convert_rgb_to_hex(r)
    g = convert_rgb_to_hex(g)
    b = convert_rgb_to_hex(b)
    return r+g+b;
}
console.log(rgb(121,191,299)) // returns 79BFFF
console.log(Math.floor(11.9375))
a = 15
console.log(a.toString(16))
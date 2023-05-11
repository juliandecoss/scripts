function solution(number){
    var dicci = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    var dicci2 = {1000:"M",900:"CM",500:"D",400:"CD",100:"C",90:"XC",50:"L",40:"XL",10:"X",9:"IX",5:"V",4:"IV",1:"I"}
    var solucc = ""
    for(i=0;i<dicci.length;i++){
        result = number/dicci[i]
        if(result>=1){
            number = number - dicci[i]
            solucc += dicci2[dicci[i]]
            if(result == 0){break}else{i-= 1};
        }
    }
    console.log(solucc)
  }
for(j=0;j<=5000;j+=353){
    console.log(j)
    solution(j)
}
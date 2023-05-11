function SeriesSum(n){
  nums = (n-2.00)*3.00+4.00
  let solucc = 0.00
  for(i=n;i>0;i--){
      solucc += 1.00/nums;
      nums -= 3.00;
  }
  up =solucc.toString().substr(4,1)
  if(parseInt(up)>=5){
      solucc += 0.01
  }
  solu = solucc.toString().substr(0,4)
  if(solu.length == 1){
      solu += ".00"
  }
  return solu
}
for(j=1;j<=5;j++){
    console.log(SeriesSum(j))
}

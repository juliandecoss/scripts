function pickPeaks(graph){
    let response = {pos:[], peaks:[]};
    if(!graph.length){return response};
    for(let i=1;i<=graph.length;++i){
        if(i == graph.length){}
        else{
            var repastValue = graph[i-2]
            var pastValue= graph[i-1]
            var value = graph[i]
            var nextValue = graph[i+1]
            //2 6 5 6
            if(pastValue>value || (pastValue == value && i != graph.length-1)){
                if(nextValue>value && value>=pastValue){}
                else if(repastValue<pastValue){
                    if(pastValue == nextValue){
                        
                        for(let j=i+1;j<=graph.length-1;++j){
                            if(pastValue<graph[j]){
                                console.log(i-1)
                                console.log(pastValue)
                                console.log(j)
                                console.log(graph[j])
                                break;
                            }
                            else if(pastValue>graph[j]){
                                response.peaks.push(pastValue);
                                response.pos.push(i-1);
                                break;
                            }
                        }
                    }else{
                        console.log()
                        if(i != graph.length){
                            //console.log(i-1)
                            response.peaks.push(pastValue);
                            response.pos.push(i-1);
                        }
                    }
                    
                }
            }
        }
        
    }
    return response;
}
arr = [
    0, 10,  5, 11,  3,  0,  2, 2, -4, -2,  4,
    7,  9,  5, -3, -3, -1, -2, 5,  3,  2,  6,
    5,  6, 15,  9, -3,  6,  0, 0,  1, 14,  8,
    8, 12,  4,  1, 10,  7, 10, 6,  3,  0, 10,
   -3, -4,  7,  1, 10,  9
 ]
// problemas en  SE SALTEA EL 21 con valor 6
a = pickPeaks(arr)
console.log(`len is: ${arr.length}`)
console.log(a)

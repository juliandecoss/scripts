function parseString(string) {
    string= string.replace(/[:,.*+\-?^$#"!%&/{}()|[\]\\]/g,''); // $& significa toda la cadena coincidente
    string = string.replace(/^\'|\'$/g,"");
    return string.toLowerCase()
  }
function checkRepeatedWords(top,repeated){
    var top3 = {}
    var realtop3 = []
    list_top = Object.keys(top).sort().reverse().slice(0,3)
    list_repeated = Object.keys(repeated).sort().reverse().slice(0,3)
    for(let j=0;j<3;j++){
        top3[top[list_top[j]]] = list_top[j]
        most_common_word = top[list_top[j]]
        if(!most_common_word){}
        else{
            realtop3.push(most_common_word)
        }
    }
    if(list_top.length == 3){
        find_place = list_top.indexOf(list_repeated[0])
        if( find_place!== -1 && find_place !== 2){
            realtop3[find_place+1] = repeated[list_repeated[0]]
        }
    }else if(list_top.length == 2){
        find_place = list_top.indexOf(list_repeated[0])
        if( find_place!== -1){
           realtop3.splice(find_place+1,0,repeated[list_repeated[0]])
        }
    }
    else if(list_top.length == 1){
        find_place = list_top.indexOf(list_repeated[0])
        if( find_place!== -1){
           realtop3.splice(find_place+1,0,repeated[list_repeated[0]])
        }
        find_place = list_top.indexOf(list_repeated[1])
        if( find_place!== -1){
           realtop3.splice(find_place+1,0,repeated[list_repeated[1]])
        }
    }
    return realtop3;
}
function topThreeWords(phrase){
    var words = {}
    var sort_words = {}
    var has_more_than_one = false
    a = phrase.split(" ")

    for(let i of a){
        i = parseString(i);
        b =words[i];
        if(!b){
            words[i] = 1
        }else{
            has_more_than_one = true
            words[i]++;
        }
    }
    if(!has_more_than_one){
        return Object.keys(words).slice(0,3);
    }
    the_repeated_words = {}
    var repeated_counter = 0;
    console.log(words)
    for(let word of Object.keys(words)){
        repeated = sort_words[words[word]]
        if(repeated){
            double_repeated = the_repeated_words[words[word]]
            if(double_repeated){
                repeated_counter++;
                the_repeated_words[words[word]].slice(repeated_counter,0,word)
            }else{
                the_repeated_words[words[word]]=[word];
            }
        }else{
         sort_words[words[word]] = word
        }
    }
    console.log(sort_words)
    console.log(the_repeated_words)
    return checkRepeatedWords(sort_words,the_repeated_words)
}
   

//A cat bolted of the cat of a rat 
//Expected: ['a', 'cat', 'of'], instead got: ['a', 'of', 'bolted']
a = topThreeWords("A cat bolted of the cat of a rat")
console.log(a)
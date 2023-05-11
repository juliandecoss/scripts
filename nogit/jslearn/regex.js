function escapeRegExp(string) {
    return string.replace(/[\'.*+\-?^$#"!%&/{}()|[\]\\]/g,''); // $& significa toda la cadena coincidente
  }

a = escapeRegExp("as'd")
console.log(a)
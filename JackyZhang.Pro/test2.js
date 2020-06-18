function updb2(done){
    setTimeout(()=>{done();
    },3000);

}

updb2(function(){
    console.log("updb2 successed");
});

console.log("I like node.js")
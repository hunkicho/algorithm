'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the 'cookies' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER k
 *  2. INTEGER_ARRAY A
 */

function cookies(k, A) {
    // Write your code here
    A.sort(function(comp1, comp2) {
        return comp1 - comp2; 
    });
    
    let check = -1;
    let count = 0;
    
    while(true){
        if(A[0] >= k){
            if(count === 0){
                check = 0;
            }else{
                check = A[0];
            }
            break;
        }
        if(A.length === 1){
            count = 0;
            break;
        }
        //console.log(A);
        count ++;
        //console.log(count);
        let a = A.shift();
        let b = A.shift();
        
        let sweet = a + (2 * b);
        
        for(let i=0; i<A.length; i++){
            if(sweet <= A[i]){
                console.log(A);
                A.splice(i, 0, sweet);
                console.log(A);
                break;
            }
        }
        
        
    }
    if(count > 0){
        console.log("qqqqq");
        check = count;
    }
    console.log(A);
    return check;
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const firstMultipleInput = readLine().replace(/\s+$/g, '').split(' ');

    const n = parseInt(firstMultipleInput[0], 10);

    const k = parseInt(firstMultipleInput[1], 10);

    const A = readLine().replace(/\s+$/g, '').split(' ').map(ATemp => parseInt(ATemp, 10));

    const result = cookies(k, A);

    ws.write(result + '\n');

    ws.end();
}

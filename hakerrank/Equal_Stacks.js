// https://studyalgorithms.com/array/hackerrank-equal-stacks/

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
 * Complete the 'equalStacks' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER_ARRAY h1
 *  2. INTEGER_ARRAY h2
 *  3. INTEGER_ARRAY h3
 */

function setStacks(aStack, h1, bStack, h2, cStack, h3){
    let h1Length = h1.length - 1;
    let h2Length = h2.length - 1;
    let h3Length = h3.length - 1;
    
    let aStackTotal = 0;
    let bStackTotal = 0;
    let cStackTotal = 0;
    
    for(let i=h1Length; i>=0; i--){
        aStackTotal += h1[i];
        aStack.push(aStackTotal);
    }
    for(let i=h2Length; i>=0; i--){
        bStackTotal += h2[i];
        bStack.push(bStackTotal);
    }
    for(let i=h3Length; i>=0; i--){
        cStackTotal += h3[i];
        cStack.push(cStackTotal);
    }
}

function equalStacks(h1, h2, h3) {
    // Write your code here
    let aStack = [];
    let bStack = [];
    let cStack = [];
    
    let aSum = 0;
    let bSum = 0;
    let cSum = 0;
    
    let check = 0;
    
    setStacks(aStack, h1, bStack, h2, cStack, h3);
    
    while(aStack.length !== 0 && bStack.length !== 0 && cStack.length !== 0){
        let aHeight = aStack[aStack.length - 1];
        let bHeight = bStack[bStack.length - 1];
        let cHeight = cStack[cStack.length - 1];
        
        if(aHeight === bHeight && bHeight === cHeight){
            check = aHeight;
            break;
        }
        
        if(aHeight >= bHeight && aHeight >= cHeight){
            aStack.pop();
        }else if(bHeight >= aHeight && bHeight >= cHeight){
            bStack.pop();
        }else if(cHeight >= aHeight && cHeight >= bHeight){
            cStack.pop();
        }
    }
    
    return check;
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const firstMultipleInput = readLine().replace(/\s+$/g, '').split(' ');

    const n1 = parseInt(firstMultipleInput[0], 10);

    const n2 = parseInt(firstMultipleInput[1], 10);

    const n3 = parseInt(firstMultipleInput[2], 10);

    const h1 = readLine().replace(/\s+$/g, '').split(' ').map(h1Temp => parseInt(h1Temp, 10));

    const h2 = readLine().replace(/\s+$/g, '').split(' ').map(h2Temp => parseInt(h2Temp, 10));

    const h3 = readLine().replace(/\s+$/g, '').split(' ').map(h3Temp => parseInt(h3Temp, 10));

    const result = equalStacks(h1, h2, h3);

    ws.write(result + '\n');

    ws.end();
}

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

function equalStacks(h1, h2, h3) {
    // Write your code here
    let aStack = [];
    let bStack = [];
    let cStack = [];
    
    let aSum = 0;
    let bSum = 0;
    let cSum = 0;
    
    let check = 0;
    
    aStack.push(h1.pop());
    bStack.push(h2.pop());
    cStack.push(h3.pop());
    
    while(true){
        aSum = aStack.reduce((a, b) => (a + b));
        bSum = bStack.reduce((a, b) => (a + b));
        cSum = cStack.reduce((a, b) => (a + b));
        
        check = aSum > bSum ? aSum > cSum ? aSum : cSum : bSum > cSum ? bSum : cSum;
        
        if(aSum == bSum && bSum == cSum){
            return check;
            //break;
        }
        
        if(h1.length < 1 || h2.length < 1 || h3.length < 1){
            return 0;
            //break;
        }
        
        if(check > aSum){
            if(h1.length > 0){
                aStack.push(h1.pop());
            }
        }
        if(check > bSum){
            if(h2.length > 0){
                bStack.push(h2.pop());
            }
        }
        if(check > cSum){
            if(h3.length > 0){
                cStack.push(h3.pop());
            }
        }
    }
    
    


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

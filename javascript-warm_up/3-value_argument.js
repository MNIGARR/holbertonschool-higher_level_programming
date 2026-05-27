#!/usr/bin/node
const firstArg = process.argv[2];
if (firstArg===undefined){
    console.log("No Argument");
} else {
    console.log(firstArg);
}

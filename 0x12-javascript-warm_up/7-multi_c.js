#!/usr/bin/node
const argC = process.argv.slice(2);
const xtimes = parseInt(argC);
if (!isNaN(xtimes)){
	for (i = 0; i < xtimes; i++){
		console.log('C is fun')
	}
}
else{
	console.log('Missing number of occurrences')
}

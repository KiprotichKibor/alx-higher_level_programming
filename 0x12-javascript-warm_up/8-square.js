#!/usr/bin/node
const size = parseInt(process.argv[2]);

if (!isNaN(size)) {
  if (size <= 0) {
    console.log('Size must be a positive integer');
  } else {
    for (let i = 0; i < size; i++) {
      let row = '';
      for (let j = 0; j < size; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }
} else {
  console.log('Missing size');
}

#!/usr/bin/node
const nm = parseInt(process.argv[2]);
if (nm) {
  console.log('My number: ' + nm);
} else {
  console.log('Not a number');
}

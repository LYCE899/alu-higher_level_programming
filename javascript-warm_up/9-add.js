#!/usr/bin/node
const args = process.argv.slice(2);
function add (a, b) {
  const result = a + b;
  console.log(result);
}
add(Number(args[0]), Number(args[1]));

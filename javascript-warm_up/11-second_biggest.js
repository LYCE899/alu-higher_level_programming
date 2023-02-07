#!/usr/bin/node
const args = process.argv.length;
const nm = [];
switch (args) {
  case 2:
  case 3:
    console.log(0);
    break;

  default:
    for (let i = 2; i < args; i++) {
      nm.push(process.argv[i]);
    }
    nm.sort((a, b) => b - a);
    console.log(nm[1]);
    break;
}

#!/usr/bin/node
function factorial (nm) {
  if (isNaN(nm) || nm <= 1) {
    return 1;
  }
  return nm * factorial(nm - 1);
}
console.log(factorial(parseInt(process.argv[2])));

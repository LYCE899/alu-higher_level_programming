#!/usr/bin/node
const n = parseInt(process.argv[2]);
function factorial () {
  if (n) {
    let a = 1;
    for (let i = 1; i <= n; i++) {
      a *= i;
    }
    console.log(a);
  } else {
    console.log(1);
  }
}
factorial.call();

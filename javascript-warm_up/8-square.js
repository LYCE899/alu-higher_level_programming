#!/usr/bin/node
function square () {
  const n = parseInt(process.argv[2]);
  if (n) {
    for (let i = 0; i < n; i++) {
      if (n > 0) {
        console.log('X'.repeat(n));
      } else {
        break;
      }
    }
  } else {
    console.log('Missing size');
  }
}
square.call();

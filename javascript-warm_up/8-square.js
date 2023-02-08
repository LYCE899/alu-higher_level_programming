#!/usr/bin/node
const nm = parseInt(process.argv[2]);
if (nm) {
  for (let i = 0; i < nm; i++) {
    console.log('X'.repeat(nm));
  }
} else if (nm < 0) {
  console.log();
} else {
  console.log('Missing size');
}

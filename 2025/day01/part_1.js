import fs from "fs";

let input = fs.readFileSync("input.txt", "utf8").split("\n").slice(0, -1);
let password = 0;
let dial = 50;

for (const code of input) {
  const delta = (code[0] == "L" ? -1 : 1) * parseInt(code.slice(1));
  dial = (((dial + delta) % 100) + 100) % 100;
  password += dial == 0 ? 1 : 0;
}

console.log(password);

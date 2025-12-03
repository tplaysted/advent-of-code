import fs from "fs";

const input = fs.readFileSync("input.txt", "utf8").split("\n").slice(0, -1);
let answer = 0;

for (const bank_str of input) {
  let bank = bank_str.split("").map((c) => parseInt(c));
  let dig_i = Math.max(...bank.slice(0, -11)); // similar to last time

  bank = bank.slice(bank.indexOf(dig_i) + 1);
  answer += 10 ** 11 * dig_i;

  for (let i = 10; i >= 0; i--) {
    dig_i = i != 0 ? Math.max(...bank.slice(0, -i)) : Math.max(...bank);
    bank = bank.slice(bank.indexOf(dig_i) + 1); // gradually shrink bank
    answer += 10 ** i * dig_i;
  }
}

console.log(answer);

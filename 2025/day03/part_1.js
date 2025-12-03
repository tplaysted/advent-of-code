import fs from "fs";

const input = fs.readFileSync("input.txt", "utf8").split("\n").slice(0, -1);
let answer = 0;

for (const bank_str of input) {
  const bank = bank_str.split("").map((c) => parseInt(c));

  const dig_1 = Math.max(...bank.slice(0, -1)); // first digit is largest before last digit
  const idx = bank.indexOf(dig_1) + 1;
  const dig_2 = Math.max(...bank.slice(idx));

  answer += 10 * dig_1 + dig_2;
}

console.log(answer);

import fs from "fs";

const input = fs.readFileSync("input.txt", "utf8").split("\n").slice(0, -1);
const ranges = input
  .slice(0, input.indexOf(""))
  .map((x) => x.split("-").map((n) => parseInt(n)));
const ids = input.slice(input.indexOf("") + 1).map((n) => parseInt(n));

let answer = 0;

for (const id of ids) {
  for (const range of ranges) {
    if ((id >= range[0]) & (id <= range[1])) {
      answer += 1;
      break;
    }
  }
}

console.log(answer);

import fs from "fs";

const input = fs.readFileSync("input.txt", "utf8").split(",");
const ranges = input.map((r) => r.split("-").map((n) => parseInt(n)));

let answer = 0;

for (const range of ranges) {
  for (let id = range[0]; id <= range[1]; id++) {
    const idstr = id.toString();
    if (idstr.length % 2 != 0) {
      continue;
    }

    if (idstr.slice(0, idstr.length / 2) == idstr.slice(idstr.length / 2)) {
      answer += id;
    }
  }
}

console.log(answer);

import fs from "fs";

const input = fs.readFileSync("input.txt", "utf8").split(",");
const ranges = input.map((r) => r.split("-").map((n) => parseInt(n)));

let answer = 0;

for (const range of ranges) {
  for (let id = range[0]; id <= range[1]; id++) {
    const idstr = id.toString();

    for (let i = 1; i <= idstr.length / 2; i++) {
      if (idstr.length % i != 0) {
        continue;
      }

      const substr = idstr.slice(0, i);
      let subs = [];
      let valid = true;

      for (let j = i; j < idstr.length; j += i) {
        valid = valid & (substr == idstr.slice(j, j + i));
      }

      if (valid) {
        answer += id;
        break; // only count each id once
      }
    }
  }
} // 4 loops, nice

console.log(answer);

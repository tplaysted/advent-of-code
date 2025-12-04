import fs from "fs";

const input = fs.readFileSync("input.txt", "utf8").split("\n").slice(0, -1);
const deltas = [
  [-1, -1],
  [-1, 0],
  [-1, 1],
  [0, -1],
  [0, 1],
  [1, -1],
  [1, 0],
  [1, 1],
];

let answer = 0;

for (let i = 0; i < input.length; i++) {
  for (let j = 0; j < input[0].length; j++) {
    const x = input[i][j];

    if (x == ".") {
      continue;
    }

    let count = 0;

    for (const d of deltas) {
      if (
        (i + d[0] < 0) |
        (j + d[1] < 0) |
        (i + d[0] >= input.length) |
        (j + d[1] >= input[0].length)
      ) {
        continue;
      }

      count += input[i + d[0]][j + d[1]] == "@" ? 1 : 0;
    }

    answer += count < 4 ? 1 : 0;
  }
}

console.log(answer);

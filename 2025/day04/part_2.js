import fs from "fs";

let input = fs
  .readFileSync("input.txt", "utf8")
  .split("\n")
  .slice(0, -1)
  .map((s) => s.split(""));

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

function remove(floor) {
  // one iteration of collecting rolls
  let answer = 0;
  let idxs = [];

  for (let i = 0; i < floor.length; i++) {
    for (let j = 0; j < floor[0].length; j++) {
      const x = floor[i][j];

      if (x != "@") {
        continue;
      }

      let count = 0;

      for (const d of deltas) {
        if (
          (i + d[0] < 0) |
          (j + d[1] < 0) |
          (i + d[0] >= floor.length) |
          (j + d[1] >= floor[0].length)
        ) {
          continue;
        }

        count += floor[i + d[0]][j + d[1]] == "@" ? 1 : 0;
      }

      if (count < 4) {
        answer += 1;
        idxs.push([i, j]);
      }
    }
  }

  for (const idx of idxs) {
    floor[idx[0]][idx[1]] = "x";
  }

  return [floor, answer];
} // a bit verbose but it works

let total = 0;
let answer = 0;

while (true) {
  [input, answer] = remove(input);

  if (answer == 0) {
    break;
  } else {
    total += answer;
  }
}

console.log(total);

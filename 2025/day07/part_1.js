import fs from "fs";

let input = fs
  .readFileSync("input.txt", "utf8")
  .split("\n")
  .slice(0, -1)
  .map((line) => line.split(""));

let splits = 0;

for (let i = 1; i < input.length; i++) {
  for (let j = 0; j < input[0].length; j++) {
    if ((input[i - 1][j] == "S") | (input[i - 1][j] == "|")) {
      input[i][j] = input[i][j] == "^" ? "^" : "|";
    }

    if (i < 2) {
      continue;
    }

    if ((input[i - 1][j] == "^") & (input[i - 2][j] == "|")) {
      input[i][j - 1] = "|"; // there'll never be a splitter on the edge
      input[i][j + 1] = "|";
      splits += 1;
    }
  }
}

const output = input.map((line) => line.join("")).join("\n");
// console.log(output);

console.log(splits);

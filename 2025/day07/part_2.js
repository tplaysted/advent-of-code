import fs from "fs";

let input = fs
  .readFileSync("input.txt", "utf8")
  .split("\n")
  .slice(0, -1)
  .map((line) => line.split(""));

const ones = Array(input[0].length).fill(1);
input = input.concat([ones]);

for (let row = input.length - 1; row >= 2; row -= 2) {
  // iterate from the bottom up, replace each '^' with the total number of timelines rooted at it
  for (let j = 0; j < input[0].length; j++) {
    if (input[row][j] == "^") {
      let sum = 0;
      for (let i = row + 1; i < input.length; i++) {
        if (input[i][j - 1] != ".") {
          sum += input[i][j - 1];
          break;
        }
      }

      for (let i = row + 1; i < input.length; i++) {
        if (input[i][j + 1] != ".") {
          sum += input[i][j + 1];
          break;
        }
      }

      input[row][j] = sum;
    }
  }
}

console.log(input[2][Math.floor(input[0].length / 2)]);

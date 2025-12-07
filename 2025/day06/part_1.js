import fs from "fs";

const input = fs.readFileSync("input.txt", "utf8").split("\n").slice(0, -1);
const problems = input.slice(0, -1).map((line) =>
  line
    .trimStart()
    .split(/\s+/)
    .map((s) => parseInt(s)),
);
const operators = input.at(-1).split(/\s+/);

let total = 0;

for (let j = 0; j < problems[0].length; j++) {
  let answer = operators[j] == "+" ? 0 : 1;

  for (let i = 0; i < problems.length; i++) {
    if (operators[j] == "+") {
      answer += problems[i][j];
    } else {
      answer *= problems[i][j];
    }
  }
  total += answer;
}

console.log(total);

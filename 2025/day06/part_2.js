import fs from "fs";

let input = fs.readFileSync("input.txt", "utf8").split("\n").slice(0, -1);
const linelen = Math.max(...input.map((line) => line.length));
const ops = input.at(-1).split(/\s+/);

input = input.map((line) => line.padEnd(linelen, " "));
const grid = input.slice(0, -1).map((line) => line.split(""));

let sum = 0;
const starts = [0]
  .concat(
    input
      .at(-1)
      .split(/\S+/)
      .map((s) => s.length + 1)
      .slice(1, -1)
      .map((n) => (sum += n)),
  )
  .concat(linelen + 1);

let problems = [];

for (let j = 0; j < starts.length - 1; j++) {
  let problem = [];

  for (let k = starts[j]; k < starts[j + 1] - 1; k++) {
    problem.push(
      parseInt(
        grid
          .map((row) => row[k])
          .join("")
          .replace(" ", ""),
      ),
    );
  }

  problems.push(problem);
}

let total = 0;

for (let i = 0; i < problems.length; i++) {
  let answer = ops[i] == "+" ? 0 : 1;

  for (const val of problems[i]) {
    if (ops[i] == "+") {
      answer += val;
    } else {
      answer *= val;
    }
  }

  total += answer;
}

console.log(total);

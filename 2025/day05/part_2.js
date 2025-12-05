import fs from "fs";

const input = fs.readFileSync("input.txt", "utf8").split("\n").slice(0, -1);
const ranges = input
  .slice(0, input.indexOf(""))
  .map((x) => x.split("-").map((n) => parseInt(n)));

const begin = Math.min(...ranges.map((range) => range[0]));
const end = Math.max(...ranges.map((range) => range[1]));

let reduced = []; // assume all ranges in this are mutually exclusive

for (const range of ranges) {
  const left = reduced.filter((r) => (r[0] <= range[0]) & (r[1] >= range[0]));
  const right = reduced.filter((r) => (r[0] <= range[1]) & (r[1] >= range[1]));

  // left inside, right inside
  if ((left.length > 0) & (right.length > 0)) {
    reduced = [
      ...reduced.filter((r) => r[1] < left[0][0]),
      [left[0][0], right[0][1]],
      ...reduced.filter((r) => right[0][1] < r[0]),
    ];
  }

  // left outside, right outside
  if ((left.length == 0) & (right.length == 0)) {
    reduced = [
      ...reduced.filter((r) => r[1] < range[0]),
      range,
      ...reduced.filter((r) => range[1] < r[0]),
    ];
  }

  // left inside, right outside
  if ((left.length > 0) & (right.length == 0)) {
    reduced = [
      ...reduced.filter((r) => r[1] < left[0][0]),
      [left[0][0], range[1]],
      ...reduced.filter((r) => range[1] < r[0]),
    ];
  }

  // left outside, right inside
  if ((left.length == 0) & (right.length > 0)) {
    reduced = [
      ...reduced.filter((r) => r[1] < range[0]),
      [range[0], right[0][1]],
      ...reduced.filter((r) => right[0][1] < r[0]),
    ];
  }
}

reduced.sort((a, b) => a[0] - b[0]);

//console.log(reduced);

const answer = reduced.reduce((a, c) => a + c[1] - c[0] + 1, 0);
console.log(answer);

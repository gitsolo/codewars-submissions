const sum = arr => arr.reduce((i, j) => i + j, 0);

const equalSidesArr = arr =>
  arr
    .map((i, j) => (sum(arr.slice(0, j)) === sum(arr.slice(j + 1)) ? j : null))
    .filter(i => i !== null)[0] ?? -1;

// Compile with babel

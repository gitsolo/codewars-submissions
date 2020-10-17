const repeats = arr =>
  arr
    .filter(i => arr.lastIndexOf(i) === arr.indexOf(i))
    .reduce((i, j) => i + j);

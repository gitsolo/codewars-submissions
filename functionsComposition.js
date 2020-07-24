const compose = (a, ...b) => c =>
  a ? [a, ...b].reverse().reduce((i, j) => j(i), c) : c;

const twoOldestAges = arr => {
  const f = arr.sort((a, b) => b - a);
  return [f[1], f[0]];
};

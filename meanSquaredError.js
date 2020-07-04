const solution = (arr1, arr2) =>
  arr1.map((i, j) => (i - arr2[j]) ** 2).reduce((i, j) => i + j) / arr1.length;

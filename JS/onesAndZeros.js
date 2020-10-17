const binaryArrayToNumber = arr =>
  arr.reverse().reduce((i, j, index) => i + j * 2 ** index);

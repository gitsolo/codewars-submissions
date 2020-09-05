const sorted = arr => arr.sort((a, b) => a - b);

const comp = (a, b) => {
  if (a && b) {
    const arr1 = sorted(a);
    const arr2 = sorted(b);
    return arr1.every((i, j) => arr2[j] === i * i);
  }
  return false;
};

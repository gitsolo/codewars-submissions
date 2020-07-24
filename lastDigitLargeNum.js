// aPowerB;
const getLastDigit = str => str.split('').reverse()[0];

const getDivisibilties = num => [
  ...new Set(
    Array(9)
      .fill(0)
      .map((_, j) => getLastDigit(String(num ** (j + 1))))
  ),
];

const modLargeNum = (num, mod) => {
  let res = 0;
  num.split('').forEach(i => (res = (res * 10 + Number(i)) % mod));
  return res;
};

const lastDigit = (a, b) => {
  if (a === '0' || b === '0') {
    return 1;
  }
  const f = getDivisibilties(getLastDigit(a));
  const rem = modLargeNum(b, 4);
  return Number(rem === 0 ? f[f.length - 1] : f[rem - 1] || f[0]);
};

// BigInt

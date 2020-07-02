const convToBin = num => {
  const arr = [];
  let x = num;
  while (Math.floor(x / 2 > 0)) {
    arr.push(x % 2);
    x = Math.floor(x / 2);
  }
  return arr.filter(i => i === 1).length;
};

console.log(convToBin(1234));

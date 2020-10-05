const getOperationName = ([x, y, z]) => {
  if (x + y === z) {
    return 'addition';
  } else if (x - y === z) {
    return 'subtraction';
  } else if (x * y === z) {
    return 'multiplication';
  } else {
    return 'division';
  }
};

const sayMeOperations = (numbersString = 's') => {
  const numbersArr = numbersString.split(' ').map(i => Number(i));

  const newArr = [];

  numbersArr.forEach((_, j) => {
    let firstInd = j;
    let lastInd = firstInd + 3;

    const nums = numbersArr.slice(firstInd, lastInd);

    newArr.push(nums);
  });

  console.log(newArr);

  return newArr
    .map(i => (i.length === 3 ? getOperationName(i) : null))
    .filter(i => i !== null)
    .join(', ');
};

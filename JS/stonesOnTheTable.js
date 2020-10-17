const solve = (stones = 's') => {
  const arr = stones.split('');

  let value = 0;

  for (let i = 0; i < arr.length; i++) {
    arr[i] === arr[i + 1] ? value++ : null;
  }

  return value;
};

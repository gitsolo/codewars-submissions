const toNum = str => str.reduce((i, j) => Number(i) + Number(j));

const dm = numString => {
  let newNum = toNum(numString);

  while (newNum >= 10) {
    newNum = toNum(String(newNum).split(''));
  }

  return newNum;
};

const lifePathNumber = dateString =>
  dm(dateString.split('').filter(i => i !== '-'));

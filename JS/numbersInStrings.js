const solve = str =>
  Math.max(
    ...str
      .replace(/[^0-9]/gi, 'loki')
      .split('loki')
      .map(i => Number(i))
  );

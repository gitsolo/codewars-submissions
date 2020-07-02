const toCamelCase = str =>
  str
    ? str
        .split(/[-|_]/g)
        .map((i, j) =>
          (j === 0 && i[0].match(/[A-Z]/g)) || j > 0
            ? i[0].toUpperCase() + i.slice(1)
            : i
        )
        .join('')
    : '';

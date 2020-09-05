const abbreviate = str =>
  str
    .split(/([^a-zA-Z])/g)
    .map(i =>
      i.length > 3 ? i.slice(0, 1) + (i.length - 2) + i.slice(i.length - 1) : i
    )
    .join('');

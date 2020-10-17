const fix = (paragraph = 'string') =>
  paragraph
    ? paragraph
        .split('. ')
        .map(i => i[0].toUpperCase() + i.slice(1).toLowerCase())
        .join('. ')
    : paragraph;

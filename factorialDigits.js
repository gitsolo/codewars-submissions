const factDigits = n =>
  Math.floor(n * Math.log10(n / Math.E) + Math.log10(2 * Math.PI * n) / 2) +
    1 || 1;

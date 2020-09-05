const songDecoder = song =>
  song
    .split('WUB')
    .filter(i => i.match(/[A-Z]/g))
    .join(' ');

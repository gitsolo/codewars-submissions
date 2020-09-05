// https://www.codewars.com/kata/525f50e3b73515a6db000b83/train/dart

String createPhoneNumber(List<int> x) =>
    '(${x.sublist(0, 3).join()}) ' +
    '${x.sublist(3, 6).join()}-' +
    x.sublist(6).join();

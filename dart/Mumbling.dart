// https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/dart

String capitailise(String name) =>
    name[0].toUpperCase() + name.substring(1).toLowerCase();

String accum(String name) {
  final Map<int, String> obj = name.split('').asMap();
  return (obj.keys.map((e) => capitailise(obj[e] * (e + 1))).join('-'));
}

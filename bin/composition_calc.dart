import 'dart:io';

import 'package:trotter/trotter.dart';
void findSums(int length, List<int> numberSet) {
  Map<int, int> possibleSums = {};
  Map<int, List<List<int>>> possibleSumsWithComps = {};

  for (int i = (numberSet.first * length); i <= (numberSet.last * length); i++) {
    possibleSums[i] = 0;
    possibleSumsWithComps[i] = [];
  }

  var comps = Compositions(length, numberSet.toList());
  
  print('Finding summations for n = $length...');
  for (final composition in comps()) {
    var sum = 0;
    for (final number in composition) {
      sum += number;
    }
    possibleSums[sum] = possibleSums[sum]! + 1;
    possibleSumsWithComps[sum]!.add(composition);
  }

  Map<int, List<List<int>>> sumsWithComps = {};
  for (MapEntry e in possibleSumsWithComps.entries) {
    sumsWithComps[e.key] = e.value;
  }

  var file = File('n$length.txt');
  if (file.existsSync()) file.deleteSync();
  file.createSync();

  file.writeAsStringSync(sumsWithComps.toString());
  print('saved to ${file.path}');
}

void main(List<String> arguments) {
  const List<int> u = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
  print('universe = $u');

  for (int n = 0; n <= 5; n++) {
    findSums(n, u);
  }
}
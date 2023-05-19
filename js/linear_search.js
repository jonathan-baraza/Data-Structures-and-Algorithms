const linearSearch = (arr, target) => {
  let result = null;
  arr.forEach((item, index) => {
    if (item === target) {
      result = index;
    }
  });

  result === 0 ? (result = "0") : (result = result);
  return result;
};

const verifySearch = (result) => {
  result
    ? console.log(`The target was found on index ${result}`)
    : console.log("The target was not found on the provided list.");
};

myArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
target = 1;

verifySearch(linearSearch(myArray, target));

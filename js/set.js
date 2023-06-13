/*Sets*/

function mySet() {
  //the var collection will hold the set
  var collection = [1, 2, 3, 4, 5];

  //this method will check for the presence of an element and return true or false
  this.has = function (element) {
    return collection.indexOf(element) !== -1;
  };

  //this method will return all values in a set
  this.values = function () {
    return collection;
  };

  //this method will add an element to the set
  this.add = function (element) {
    if (!this.has(element)) {
      collection.push(element);
      return true;
    }
    return false;
  };
}

var obj = new mySet();
console.log(obj.add(1));
console.log(obj.values());

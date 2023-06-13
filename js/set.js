/*Sets*/

function mySet() {
  //the var collection will hold the set
  var collection = ["1", 2, "dog", "cat"];

  //this method will check for the presence of an element and return true or false
  this.has = function (element) {
    return collection.indexOf(element) !== -1;
  };

  //this method will return all values in a set
  this.values = function () {
    return collection;
  };
}

var obj = new mySet();
console.log(obj.has("1"));
console.log(obj.has("bike"));
console.log(obj.values());

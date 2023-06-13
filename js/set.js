/*Sets*/

function mySet() {
  //the var collection will hold the set
  var collection = [];

  //this method will check for the presence of an element and return true or false
  this.has = function (element) {
    return collection.indexOf(element) !== -1;
  };
}

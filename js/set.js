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

  this.remove = function (element) {
    if (!this.has(element)) {
      return false;
    }
    var idx = collection.indexOf(element);
    var newCollection = [];
    for (i = 0; i < collection.length; i++) {
      if (i !== idx) {
        newCollection.push(collection[i]);
      }
    }
    collection = newCollection;
    return idx;

    //remove with splice
    // collection.splice(idx,1)
  };

  this.size = function () {
    return collection.length;
  };

  this.union = function (otherSet) {
    var unionSet = new mySet();
    var firstSet = this.values();
    var secondSet = otherSet.values();

    firstSet.forEach(function (e) {
      unionSet.add(e);
    });
    secondSet.forEach(function (e) {
      unionSet.add(e);
    });

    collection = unionSet;
    return unionSet;
  };

  this.intersection = function (otherSet) {
    var intersectionSet = new mySet();
    var firstSet = this.values();

    firstSet.forEach(function (e) {
      if (otherSet.has(e)) {
        intersectionSet.add(e);
      }
    });
    return intersectionSet;
  };
}

var obj = new mySet();
// console.log(obj.union([6, 7, 8, 9]));

// console.log(obj.remove(4));
// console.log(obj.remove(1));
// console.log(obj.values());

#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      // Create an empty object if width or height is not valid
      this.width = undefined;
      this.height = undefined;
    }
  }
}

module.exports = Rectangle;

#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    // if (w <= 0 || h <= 0) {
    //  throw new Error('Width and height must be positive numbers');
    // }
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;

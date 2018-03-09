// import everything as methods or properties of an object
import * as h from './helpers';
// and then use them
const displayTotal = h.formatPrice(5000);
console.log(displayTotal);


// Or import everything into the module scope:
import _ from './helpers';
const displayTotal2 = addTax(1000);
console.log(displayTotal2);
// I'd recommend against this style because it's less explicit
// and could lead to code that's harder to maintain

// or cherry pick only the things you need:
// import { couponCodes, discountPrice } from './helpers';
import { couponCodes, discountPrice } from './helpers';
const discount = discountPrice(500, 0.33);
console.log(discount);

// Look into @std/esm
// require("@std/esm")

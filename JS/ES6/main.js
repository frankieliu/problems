// import everything as methods or properties of an object
import _ as h from './helpers';
// and then use them
const displayTotal = h.formatPrice(5000);


// Or import everything into the module scope:
// import * from './helpers';
// const displayTotal = addTax(1000);
// I'd recommend against this style because it's less explicit
// and could lead to code that's harder to maintain


// or cherry pick only the things you need:
// import { couponCodes, discountPrice } from './helpers';
// const discount = discountPrice(500, 0.33);

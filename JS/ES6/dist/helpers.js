'use strict';

Object.defineProperty(exports, "__esModule", {
    value: true
});

var taxRate = 0.13;

var couponCodes = ['BLACKFRIDAY', 'FREESHIP', 'HOHOHO'];

function formatPrice(price) {
    // .. do some formatting
    return formattedPrice;
}

function addTax(price) {
    return price * (1 + taxRate);
}

function discountPrice(price, percentage) {
    return price * (1 - percentage);
}

exports.couponCodes = couponCodes;
exports.formatPrice = formatPrice;
exports.addTax = addTax;
exports.discountPrice = discountPrice;
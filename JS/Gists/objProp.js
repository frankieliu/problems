var map = {
    "s":"d", "m":"e",
    "e":"h", "x":"l",
    "z":"o", "i":"r",
    "a":"w", "o":"!",
    "-":" "
};
var reverseMap = {};

for (var j in map){
    if (!Object.prototype.hasOwnProperty.call(map, j)) continue;
    reverseMap[map[j]] = j;
}

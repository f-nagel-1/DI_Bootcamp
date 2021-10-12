for (let i = 0; i <= 15; i++){
    if (i%2 == 0){
	 console.log(`${i} is even`);
    } else {
     console.log(`${i} is even`);
    }
}



exercise 2

// loop over array and add to the array the end "s" at every fruit


let shopping = ["apple", "pear", "melon", "banana"];

for (let i = 0; i < shopping.length; i++){
    shopping[i] += "s"
}
console.log(shopping)

======

let sum = 0;

let prices = [23, 15, 34, 10];
for (let i = 0; i < prices.length; i++){
    sum += prices[i]
}

console.log(sum)

////EXERCISE 1//////

let fruits = ["Banana", "Apples", "Oranges", "Blueberries"];
/*removes banana = "Apples", "Oranges", "Blueberries"*/
fruits.shift();
/*sorts alphabetically = apples, blueberries, oranges*/
fruits.sort();
/*adds Kiwi to end apples, blueberries, oranges, kiwi*/
fruits.push("Kiwi");
/*removes apples: blueberries, oranges*, kiwi*/
fruits.splice(0, 1);
/*sorts in reverse order apples: kiwi, oranges, blueberries*/
fruits.reverse();
console.log(fruits);


////EXERCISE 2//////


let moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
console.log(moreFruits[1][1]);

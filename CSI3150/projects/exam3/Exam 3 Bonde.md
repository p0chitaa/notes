# Exam 3
Drew Bonde

<br>

## Q1. Explain in detail the differences in variable declaration and usage using JavaScript (JS) code snippetsfor the following use-case scenarios: **(4 points)**
1. `let`[^1]
    * Initialization is not necessary
    * "block scoped"
      * Trying to access it outside of its particular block will throw an error
    * Can be updated
2. `var`[^1]
    * Initialization is not necessary
    * Creates global (or function) variables
    * Can be updated
3. `const`[^1]
    * MUST BE INITIALIZED
    * `const` variables have the same properties as `let` variables, but they can ***NOT*** be updated.

[^1]: https://www.geeksforgeeks.org/difference-between-var-let-and-const-keywords-in-javascript/
   
<hr>

## Q2. With the help of JS code snippet explain what are JS object literals and declare a syntactically correct JS object literal. Explain the difference between a JS object literal and JSON object literal. What is the meaning and purpose of object destructuring in JS? Give a syntactically correct example of object destructuring. **(6 points)**
> A javascript object literal is a "list of zero or more pairs of property names and associated values of an object, enclosed in curly braces ( {} )" [^2]
* AKA a object with (possible) multiple attributes

<br>
JS Object Literal Syntax:

```js
const me = {
    firstName: "Drew",
    lastName: "Bonde"
}
```
> The variable `me` has two different attributes: `firstName` and `lastName`

Now, the difference between JS object literals and JSON object literals is somewhat large, however the syntax is extremely similar.

<br>
JSON Syntax:

```json
{
"firstName": "Drew",
"lastName": "Bonde"
}
```

* JSON stands for JavaScript Object Notation. I.e. this is typically how data looks when fetched from a server and thrown to a browser. There are multiple built in functions to turn JSON data into JS object literals and what not, but they are technically not JS object literals.

Object destructuring is a way to unpack values/properties from objects into their own variables. In other words, this saves a lot of time; instead of manually adding each value into a list or variable, through loops or otherwise, this will do it all for you.

Take a look at the code provided by Mozilla.[^3]
let a, b, rest;
[a, b] = [10, 20];

```js
console.log(a);
// 10

console.log(b);
// 20

[a, b, ...rest] = [10, 20, 30, 40, 50];

console.log(rest);
// [30, 40, 50]
```
> So instead of manually making a new array containing 30, 40, and 50, we saved some time using this instead.

[^2]: https://developer.mozilla.org/en-US/docs/Glossary/Literal
[^3]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment

<hr>

## Q3. Give an example of a syntactically correct Array declaration in JS. **(6 points)**
1. Using this example explain the following methods supported by syntactically correct code snippets: arrayName.push(), arrayName.pop(), arrayName.unshift().

`.push()` takes a parameter, and adds it to the end of an array:
```js
let things = [1, 2, 3, 4]
things.push(5)

console.log(things)
// Output: [1, 2, 3, 4, 5]
```

`.pop()` doesn't take a parameter, and removes the last value of an array:
```js
let things = [1, 2, 3, 4, 5]
things.pop()

console.log(things)
// Output: [1, 2, 3, 4]
```

`.unshift()` takes one or more parameters, and adds them to the **FRONT** of an array:
```js
let things = [4, 5]
things.unshift(1, 2, 3)

console.log(things)
// Output: [1, 2, 3, 4, 5]
```
2. Using this example explain the functionality of the following higher order Array methods supported by syntactically correct code snippets: .forEach(), .map(), .filter()

`.forEach()` executes a function for each value in an array:
```js
let sum = 0
let things = [1, 2, 3, 4, 5]
things.forEach(getSum)

function getSum(num) {
    sum += num
}
console.log(sum)
// Output: 15
```

`.map()` also calls a function for each value in an array, but creates a new array:
```js
let things = [1, 2, 3, 4, 5]
function subb(num) {
    return num-1
}

console.log(things.map(subb))
// Output: [0, 1, 2, 3, 4]
```

`.filter()` creates a new array filled with values that pass a conditional given by a function:[^4]
```js
let things = [1, 2, 3, 4, 5]
function myFunction(num) {
    return num <= 3
}

console.log(things.filter(myFunction))
// Output: [1, 2, 3]
```

[^4]: https://www.w3schools.com/jsref/jsref_filter.asp

<hr>

## Q4. Assume that you have designed a front-end web system using HTML and CSS. Thereafter, you want to add some dynamic interaction on your webpage using Vanilla JS. The first step towards this goal will be “grab” the relevant HTML elements and save them in your JS code as objects and/or object lists. Explain using syntactically correct JS code snippets the various ways in which this can be done. **(4 points)**

There are quite a few ways this can be done.[^5]

`.getElementById()`
```html
<!--say we have an element with an id of "first-paragraph"-->
<p id="first-paragraph">This is widely thought of, at least by the person who wrote this code, to be the first paragraph tag in this document.</p>

<!--we can save this into a javascript variable by using .getElementById()-->
<script>
    const firstParagraph = document.getElementById("first-paragraph");
</script>
```

`getElementsByTagName()`
```html
<!--say we have multiple p tags-->
<p>Here is the first p tag.</p>
<p>And here is the second.</p>

<!--we can use .getElementsByTagName() to get an array of each p tag!-->
<script>
    const x = document.getElementsByTagName("p");
</script>
```

`.getElementsByClassName()`
```html
<!--say we have 3 p tags. the first two have classname "firstClass" and the third has classname "secondClass"-->
<p class="firstClass">I am the first!</p>
<p class="firstClass">I am second but I am part of the first class!</p>
<p class="secondClass">I am third but I am part of the third class!</p>

<!--we can use .getElementsByClassName() to get a list of all elements of a specific class, lets say "firstClass-->
<script>
    const x = document.getElementsByClassName("firstClass");
</script>
```

There is also `querySelector('CSS selector formatted parameter')` and `querySelectorAll()` for selecting only one item or multiple items respectively. The syntax is the same.

Or you can find HTML elements directly (see w3schools[^6] for a list of all possible ways to do this):
```html
<script>
    //returns the body
    x = document.body;
    //returns the head
    y = document.head
    //returns all img elements
    z = document.images
    //and so on. there are quite a few
```
[^5]: https://www.w3schools.com/js/js_htmldom_elements.asp
[^6]: https://www.w3schools.com/js/js_htmldom_document.asp

<hr>

## Q5. Explain using JS code snippets what are arrow functions in JS and how do they differ from traditional functions in JavaScript? **(2 points)**

Arrow functions do not require the `return` keyword if the curly braces are omitted. For example:[^7]
```js
const subTwo = (num) => num - 2;
subTwo(3);
```

Also, parentheses are not required if only a single argument is passed.

There is also a bunch of other fun stuff with arrow functions. For example, regular functions are now constructible!
```js
function mult(a, b) {
    console.log(a*b);
}

let product = new mult(5, 5);
console.log(product);
// Output: 25
```

However, arrow functions are not constructible. There are also no duplicate parameters.

[^7]: https://www.w3schools.com/js/js_arrow_function.asp

<hr>

## Q6. Suppose you have a button type html element on your webpage that states “Click me to get a famous quote”. Write a Vanilla JS based program for your webApp where: (8 points) If a user left-clicks the html button on the page, your web user interface with the aid of either JS prompt or alert windows will show them a quote from a famous person. However, each time the user clicks the button, instead of showing the same quote, show a different quote selected at random by your program from a list of (say 10 quotes) quotes stored statically by your webApp.

```html
<!DOCTYPE html>
<html>
    <body>
        <h2>Random Quotes :D</h2>
        <button onclick="getRandomQuote(getRandomNumber(0,10))">Click me to get a famous quote!</button>
        <script>
            let quotes = [
                "When you reach the end of your rope, tie a knot in it and hang on. -Franklin D. Roosevelt",
                "Always remember that you are absolutely unique. Just like everyone else. -Margaret Mead",
                "The future belongs to those who believe in the beauty of their dreams. -Eleanor Roosevelt",
                "It is during our darkest moments that we must focus to see the light. -Aristotle",
                "The greatest glory in living lies not in never falling, but in rising every time we fall. -Nelson Mandela",
                "You have brains in your head. You have feet in your shoes. You can steer yourself any direction you choose. -Dr. Seuss",
                "Life is never fair, and perhaps it is a good thing for most of us that it is not. -Oscar Wilde",
                "Only a life lived for others is a life worthwhile. -Albert Einstein",
                "Do not let making a living prevent you from making a life. -John Wooden",
                "I find that the harder I work, the more luck I seem to have. -Thomas Jefferson"
            ]
            function getRandomQuote(index) {
                alert(quotes[index])
            }
            function getRandomNumber(min, max) {
                return Math.floor(Math.random() * (max - min)) + min;
            }
        </script>
    </body>
</html>
```
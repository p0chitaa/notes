# Tag Review and Basic Structure
##### jfc have we had 5 lectures already??
###### ~~also why the fuck am i in this class 5 years in~~

---
## Portfolio
* Home/landing page - img, about me/intro
* CV/vita - educational background, format any professionals
* Hobbies - music, movies, tv, books, etc (embed vid?)
* Project - tabulate (start date, end date, desc, etc.)
* Contact me

## Difference between `<div>` tag and `<section>` tag?
* You can apply some sort of styling and what not with `<div>`s (non-semantic tag)
* `<section>`s just split up pages (semantic tag). Everything enclosed in the `<section>` tag is correlated.

## More Design Criteria
* Each page should have a navigation menu
> For now, we are representing this with HTML lists until bro covers CSS

---
## `<div>` stuff
* Remember that you can give multiple `<div>`s the same class to share attributes.
For example:
```html
<div id="1" class="intro" />
<div id="2" class="intro" />
```


## 3 Parts
Ok so we know we can break down a webpage into 3 parts:
1. Heading
2. Body
3. Footer
> What should be the content of the header?
* Lets put the navbar in the header

---
## Block Tags vs. Inline Tags
* When block tags are rendered, the browser puts a newline after it.
* When you use an inline tag, the elements will be rendered side by side.

## The `<img>` tag
* `src` = path to image (remember that `./` brings you to the root directory)
* `alt` = alternative text
* `title` = text on hover
* `width` = specified by percentage or `px` (pixels)
* `height` = specified similarly to `width`

## `<nav>`
* Semantic
* Your average navbar tag

## There are two types of HTML lists you can use
1. Ordered lists, `<ol>`
2. Unordered lists `<ul>`

> Each item in the list is enclosed with the `<li>` tag (list item)

For example:
```html
<ol>
    <li>Apple</li>
    ...
</ol>
```

---
## The `<a>` (Anchor) Tag
* Essentially links to your other pages
> There is an attribute called `href`, which essentially does the same thing as the `src` attribute for the `<img>` tag.

## More Semantic Tags
* In addition to `<main>` there are two more we are covering.
1. `<article>`
2. `<aside>`

`<article>` is basically any standalone container.
* "If you do not require any further explaination and is kind of self contained...then you put it inside of `<article>`."

`<aside>`:
* "If you're giving any info not directly correlated with the main content on the page."

## HW?
> Translate what we did so far into a DOM.
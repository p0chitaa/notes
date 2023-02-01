# Exam 1
Drew Bonde

---
## Q1 : Discuss in detail the concept of DOM for an HTML page. **(5 points)**
The HTML DOM, or document object model, is a tree of objects that acts as a programming interface for HTML. It defines all HTML elements, their respective properties and events, and every method to access each element. [^1]
> I.e. this is how one modifies HTML elements.

[^1]: JavaScript HTML DOM, https://www.w3schools.com/js/js_htmldom.asp

## Q2 : Comment on the following statement, "Learning HTML is more about learning the semantic than the syntax." Explain your answer withthe help of an example use-case scenario. **(5 points)**
* Personally, I feel like this isn't as deep as it initially comes off to be. Semantic tags are simply tags that describe their contents for the sole purpose(s) of readability and convenience. So by learning the semantic, you learn how to structure your page in a cleaner, more efficient, and sometimes reusable manner.
For example:
1. Setting up a `<div>` as a header involves this managing/balancing act, where this `<div>` acts as a wrapper for virtually everything that appears under it.
```html
<body>
    <div id="header">
        <p>This is my header!</p>
        <div id="inner-content">
            wordswordswords
        </div>
        <div id="more-inner-content">
            these are more words inside the header div
            <div id="inner-inner-content">
                these are words inside a div inside the header div!
            </div>
        </div>
    </div>
</body>
```
![Image showing div-wrapper header](./images/div-wrapper-header.png)

(yes, there is a typo but I am NOT cropping another image rn lol)

2. Instead of implementing the above, why not just use the `<header>` tag?
```html
<body>
    <header id="page-header">
        <p>This is my header!</p>
    </header>
    <div id="inner-content">
        wordswordswords
    </div>
    <div id="more-inner-content">
        these are more words inside the header div
        <div id="inner-inner-content">
            these are words inside a div below the header!
        </div>
    </div>
</body>
```
![Image showing use of the header tag](./images/header-tag.png)

> Obviously, these code blocks produce identical output. However, the code block presenting the implementation of the `<header>` tag is much easier on the eyes.
* Other semantic tags have similar use cases.

## Q3 : What is the correct usage of the following HTML5 semantic elements: `<article>`, `<footer>`, `<header>`, `<section>`, and `<main>`? **(5 points)**
I'll just be listing these off in bullet points.
* `<article>`
    * Basically any standalone container.
        * "If you do not require any further explaination and is kind of self contained...then you put it inside of `<article>`." [^2]
* `<footer>`
    * This really just defines a footer for a page.
        * A block of anything defined that will appear at the *bottom* of the page.
* `<header>`
    * The same thing as the footer but at the top of the page. 
        * A block of anything defined that will appear at the *top* of the page.
* `<section>`
    * "`<section>`s just split up pages. Everything enclosed in the `<section>` tag is correlated." [^3]
* `<main>`
    * Indicates that the content enclosed is the main content of the page.

[^2]: Professor Sen (during lecture)
[^3]: Professor Sen again (during lecture)

## Q4 : Write the HTML5 code snipped to embed an audio file and a video file in your webpage. What are the acceptable audio formats for embedding on a webpage? **(5 points)**
```html
<audio src="./path/to/audio-file.mp3" controls>
    A sample of an audio file on this page.
</audio>
<video
    src="./path/to/video.webm"
    width="35%"
    controls
    autoplay
    loop
>
    A sample of a video file.
</video>
```
Supported audio extensions:[^4]
* .mp3
* .wav
* .ogg

[^4]: HTML `<audio>` Tag, https://www.w3schools.com/tags/tag_audio.asp

Supported video extensions:
> So this one is interesting, and I can't figure out which one is the case. During lecture you gave us a list that differs from nearly everything else I found on the internet:
* .avi
* .mov
* .mp4
* .webm
> And here is the list from nearly every source I could find:[^5]
* .mp4
* .webm
* .ogg

[^5]: (There were a ton of options, but here is w3schools for example) HTML `<video>` Tag, https://www.w3schools.com/tags/tag_video.asp

> I also ripped this code snippet from what we did in class, let me know if that will be an issue in the future.

## Q5: What is the difference between `<figure>` and `<img>` tags? **(3 points)**
* The `<img>` tag is for embedding an actual image into a page, whereas the `<figure>` tag "semantically organizes"[^6] the image contained within onto the page. 

[^6]: HTML5 - When to use `<figure>`, https://www.learningjournal.guru/article/html5/html5-when-to-use-figure-tag/

## Q6: What is the difference between Block display elements and inline display elements? Give examples of each. **(2 points)**
* When block tags are rendered, the browser puts a newline character at the end of it.

Some block display elements:[^7]
```html
<p>
<div>
<header>
<main>
```
* When inline tags are used, the elements will be rendered side by side.

Some inline display elements:[^7]
```html
<span>
<img>
<button>
<script>
```

[^7]: HTML Block and Inline Elements, https://www.w3schools.com/html/html_blocks.asp

## Q7 : What are meta tags used for? Briefly describe at least 3 of them? **(5 points)**
* Meta tags are used for defining information about your page or information about the content on your page.
1. `<meta name="title">` [^8]
    * Defines the title of a page, shows in page tab at the top of the web browser or on a search engine
2. `<meta name="description">` [^8]
    * Defines a description of a page, displayed below the title in a search engine.
3. `<meta name="author">` [^8]
    * Defines the author of a page

[^8]: HTML `<meta>` Tag, https://www.w3schools.com/tags/tag_meta.asp
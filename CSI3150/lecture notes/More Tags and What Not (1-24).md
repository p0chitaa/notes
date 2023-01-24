# More Tags and What Not

## `<video>`
So essentially, video has a few attributes:
* `src` : self explanatory
* `height`
* `width`
* `controls`
* `autoplay`
* `loop`
* And more.

## `<audio>`
Nearly identical attributes as the `<video>` tag except for `height` and `width`.

## Embedding Things
### The `<iframe>` Tag
Also has near identical attributes as the `<video>` and `<audio>` tags, with an exception or two:
* `allow` : research all different subattributes for this
* `allowfullscreen`
* prolly more idk

---
## Table(s)
### `<table>`
* Within a table tag, each row is created using the tag, `<tr>`
> There is no concept of "columns" here.

Table cells are represented by the tag, `<td>`, "table data."

* Whenever creating a table header, however, when making the table data (`<td>`) use the `<th>` tag instead (table header).

### `<thead>`, `<tbody>`, and `<tfoot>`
> I think these are just semantic changes.
* These just wrap around `<tr>` tags.

### The `rowspan` Atrribute
> Just check the projects page in my first project lol.

---
## Putting an Image on the Tab (At the top of the screen lmfao)
### `<link>`
> Goes under the `<head>` tag.
```html
<link:favicon>
```
This shortcut will automatically fill out most of it for you, minus the `href` path.
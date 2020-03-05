# JavaScript with HTML and CSS

At the beginning of this course we mentioned that JavaScript is the most widely used language on the web. So how can we use JavaScript on a website?

So far, we've only used JavaScript in isolation – not alongside other technologies. Javascript typically gets included with HTML and CSS (which structure and style web pages). All modern browsers know how to run JavaScript if we include it in an HTML and CSS project.

JavaScript also has some special functions to help us access the code inside HTML and CSS so that we can write JavaScript to make that output interactive and dynamic.

In this lesson, we will use the concepts we've learned throughout the course to make an HTML and CSS website dynamic.


# Linking JavaScript
We can link a JavaScript file to HTML by including it as the `src` of a `<script>` tag inside of an HTML file, like this:

```
<script src='js/main.js'></script>
```

This line of code will link the file located at **js/main.js**. You can find this file in the file navigator by clicking the file button located at the top left of the code editor. Within the navigator, there's a folder named **js**, and within that folder is the **main.js** file.

By linking **js/main.js** in the **index.html** file, we are asking the browser to run our JavaScript code each time **index.html** loads.

We've provided you with a sample website (and the corresponding HTML and CSS code). Our goal: use JavaScript to make this page more dynamic. We will add interactive features to it as we go through the lesson.

In the code editor, we've loaded the files for a static HTML and CSS website. If you've never seen HTML before, don't worry, we'll walk through how JavaScript is added to an existing HTML and CSS project in this lesson. This lesson won't require you to greatly modify the HTML and CSS code itself. (For a deeper dive, see our HTML & CSS course here.)

# Document Object Model
The *Document Object Model*, commonly referred to as the *DOM*, is the term for elements in an HTML file. Elements are any HTML code denoted by HTML tags, like `<div>`, `<a>`, or `<p>`. Let's use JavaScript to interact with the DOM.

We can select an HTML element with JavaScript by selecting its `class` attribute, like this:

```
var header = document.getElementsByClassName('example-class-name');
```

This would find an element like this in the HTML:

```
<div class='example-class-name'> ... </div>
```

# jQuery
We've just covered how to select HTML elements using the syntax: `document.getElementsByClassName`. This is verbose and clunky, however. If we were to select a lot of elements this way, our code would get dense and difficult to read.

Wouldn't it be nice if there was a simpler way to select DOM elements? As you might have guessed, there is!

To better interact with DOM elements, we can use a *library*. A library is a set of code that contains useful pre-written functions that help with certain tasks.

A great library for interacting with the DOM is *jQuery*.

jQuery is a library written in JavaScript. The syntax and functions it contains will help us interact with DOM efficiently. We'll walk through a few examples in the following exercises.

In order to use jQuery, we need to:

1. Include jQuery in our project. jQuery is a library, which means it is a set of code in a file, therefore we will need to link that file in our HTML in order to access it.

Once we link it in our HTML file, we can use its functions and syntax in our **js/main.js** file.

2. Once linked, we'll need to make sure our HTML is loaded before we run our jQuery and JavaScript code.

This will prevent our jQuery and JavaScript code from running before the elements they select are rendered.

# jQuery Selectors
With plain JavaScript we selected an HTML element with this code:

```
document.getElementsByClassName('skillset');
```

With jQuery we can select the same element with:

```
$('.skillset');
```

1. We can wrap any CSS selector, like class, id, or tag, with `$('.example-class')` to select it with jQuery.

2. The selectors jQuery uses are the exact same as CSS selectors. For instance, if there's an element with a class of `supporting-text`, you could select it with `$('.supporting-text')`. Another example, if an element had an id of 'header', you could select it with `$('#header')`.

# hide
Now that we can select an element with jQuery, we can use built-in jQuery functions to modify it. From here on, we will start building features into our skills website.

First off, it would be nice to make the page fade in when loaded.

To make a page fade in, it must first be hidden. We can hide elements with jQuery with a function named `hide`.

We can `hide` elements with jQuery, like this:

```
$('.my-selector').hide();
```

1. We attached the `hide` function directly to the jQuery selector.

2. The `hide` function will add the CSS property `display: none` to the DOM element from the page, which will hide it.

# fadeIn
In order to fade in the `skillset` element, we can use a the jQuery function named `fadeIn`.

True to its name, `fadeIn` will fade an element in over a period of time in milliseconds. It looks like this:

```
$('.example-class').fadeIn(400);
```

1. We must start with an element that is not currently displayed on the page.

2. Just like before, we can attach `fadeIn` directly to a jQuery selector.

3. Within `fadeIn`'s parentheses, we can specify how long we want the fade to last in milliseconds. `400` is the default.

4. The example code will fade in the `'.example-class'` element over 0.4 seconds.

# click
The next feature we'd like to build is making the 'Recent Projects' clickable. When clicked, the button should show the individual projects, and when clicked again, it should hide the projects.

In order to make an element clickable, we need to write jQuery that listens to an element for a click event. jQuery can do this with an event listener function named `on('click')`.

This function will wait for a click event, and when one occurs, it will execute a provided function. The syntax looks like this:

```
$('.example-class').on('click', function() {
  // execute the code here when .example-class is clicked.
});
```

1. `$('.example-class')` selects an HTML element with the class `example-class`.
2. `.on('click', function() { ... })` adds a click listener to the selector. When it's clicked the function will execute the code within its block.

# show
To make our projects visible when the 'Recent Projects' button is clicked, jQuery provides a function named `show`, which is the opposite of `hide`.

To show an element, the syntax looks as such:

```
$('.example-class').show();
```

1. `show` is attached directly to the jQuery selector.

2. `show` will change the CSS attribute `display: none` to a visible display property, therefore showing the element.

# toggle
When we click on a 'Recent Projects' button, the projects show. Next, let's hide the projects if we click the 'Recent Projects' button again.

jQuery provides a function named `toggle` that is helpful in this situation. `toggle` will hide or show an element, each time it is triggered. The syntax looks like this:

```
$('example-class').toggle();
```

1. `toggle` can be called directly on an jQuery selector.

2. When `toggle` is executed, it will hide or show the element that the selector points to. If the element is currently hidden, `toggle` will show the element, and vice versa.

# toggleClass
Let's add one more feature: when we click the 'Recent Projects' button the background color and text color should change.

We can toggle a CSS class with a jQuery function named `toggleClass`. The syntax looks like this:

```
$('.example-class').toggleClass('active')
```

1. `.toggleClass` is a function that will toggle a CSS class on the jQuery selector it's connected to. If the element has the class applied to it, `toggleClass` will remove it, and if the element does not have the class, it will add it.

2. `'active'` is the class that we will toggle on and off. Notice that `toggleClass` does not require us to include the period before `'active'` since it's already expecting a CSS class.

# this
In the last exercise, we were toggling every 'Recent Projects' button instead of only the one we clicked on.

We can select the specific element we clicked on with the jQuery selector `$(this)`.

The syntax looks like this:

```
$('.example-class').on('click', function() {
  $(this).toggleClass('active');
});
```

1. `$(this)` selects the clicked element. If there are multiple elements with a class of `.example-class`, `this` will only toggle the class of the one that is clicked on.

2. Notice that `$(this)` does not require quotes around it, since it is not a CSS class. Instead, `this` is a JavaScript keyword.

3. `$(this)` behaves just like our other selectors. We can attach `toggleClass` or `toggle` to it in the same way.

# next
In order to toggle the projects in each section, we will need to use `$(this)` to select the button we clicked on. The issue is that `$(this)` refers to the `projects-button` in our current code, and not the projects themselves.

We need a way to select the `projects` elements next to the button that we clicked.

Luckily, jQuery can select elements logically. In **index.html**, notice that the `projects-button` element is directly followed by the `projects` list. Therefore the `projects` element is next after it.

jQuery has a function named `next` to help us select elements that are next to another element. If we have this in our HTML:

```
<div class='item-one'> ... </div>
<div class='item-two'> ... </div>
```

If we wanted to hide `item-two`, we could write:

```
$('.item-one').next().hide();
```

1. We can attach `next` to any jQuery selector to select the next direct element.

2. Then, we can attach any jQuery function to `next()`. In this case, we attached `hide`, which would hide the next element after the `$('.item-one')` element.

# text
Since we have a few areas to click on, it may be helpful to show users which sections they have viewed by changing the text inside the 'Recent Projects' buttons.

When a user clicks on a button, we will permanently change the text of the button to 'Projects Viewed'.

We can change the text of an element with the jQuery function `text`. It's syntax looks like this:

```
$('.my-selector').text('Hello world!');
```

1. `text` attaches directly to a jQuery selector.

2. Inside of `text`'s parentheses, we can provide text that will become the text of our DOM element. The text we supply will replace any existing text, and if the element has no pre-existing text, `text` will add it.

# slideToggle
The last feature we'd like to add is an aesthetic one. Right now when we click the 'Recent Projects' buttons, the projects appear instantly.

Let's instead make the projects slide onto the page when we click the 'Recent Projects' button and then slide off the page when we click the button again.

jQuery provides a method named `slideToggle` that can animate an element's entrance and exit. The syntax looks like this:

```
$('.example-class').slideToggle(400);
```

1. `slideToggle` can be called directly on a jQuery selector.

2. `slideToggle` also takes a parameter of milliseconds that the animation should last. The default is 400 milliseconds, or 0.4 seconds.

# Review jQuery
Nice work! jQuery is a complete library, and we've only covered the basics. If you're interested in adding animations to websites and creating more dynamic elements, take our jQuery course here.

In this lesson we learned:

- How to link a JavaScript file to an HTML file using a <script> tag.

- jQuery is a library to help JavaScript interact with HTML elements.

- We can make sure our page is ready to go with `$(document).ready()`. Then, we can pass in a function to `ready` that will execute when the page is loaded.

- jQuery uses the same selector names as CSS.

- We can hide elements with `hide`, and show them with `show`.

- We can make elements appear with `fadeIn`.

- `on('click')` functions allow us to make HTML elements clickable. When an element is clicked, the click function will execute the function we provide. It's full syntax looks like:

```
$('.example-class').on('click', function() {
  // Execute when .example-class is clicked
});
```

- `toggle` will toggle an element on and off the page.

- `$(this)` will select the specific element that was clicked if placed inside a click function.

- `toggleClass` can toggle a class on and off.

- We can select elements next to each other with `next`.

- `text` will replace a DOM element's text with text we specify.

- `slideToggle` will make an element slide into and out of the page with an animation.

Impressive work on completing Learn *JavaScript*!

The next Javascript course, *Intermediate JavaScript*, is coming soon! In the course you'll learn how to write full-fledged programs in JavaScript.

Until then, try out our jQuery course to make websites more dynamic, or start building applications with JavaScript with our AngularJS course and our React course. AngularJS and React are two application frameworks written in JavaScript. With them, you'll be able to create web applications.

Congrats again on your progress in completing *Learn JavaScript*!

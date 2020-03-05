# Arrays

We’ve learned to do a number of interesting things with data using functions and using `<if/else>` statements. One thing that we haven't learned yet is how to organize and store data.

One way we organize data in real life is to make lists. Let's make one here:

```javascript
Bucket List:
0. Rappel into a cave
1. Take a falconry class
2. Learn to juggle
```

Let's now write this list in JavaScript, as an array:

```javascript
var bucketList = ['Rappel into a cave', 'Take a falconry class', 'Learn to juggle'];
```

Arrays are JavaScript's way of making lists. These lists can store different data types and they are ordered, meaning the position of each list item is numbered by JavaScript.

# Create an array

Let's start by making an array and then seeing what it can do throughout the rest of this lesson.

# Property Access
Great work. Now, what if we want to select one item from an array?

Luckily, each item in an array has a numbered position. We can access an item using its number, just like we would in an ordinary list. There’s one catch though!

JavaScript counts starting from `<0>`, not `<1>`, so the first item in an array will be at position `<0>`. This is because JavaScript is zero-indexed.

We can select the first item in an array like this:

```javascript
var bucketList = ['Rappel into a cave', 'Take a falconry class', 'Learn to juggle'];
var listItem = bucketList[0];
console.log(listItem);
// Output: 'Rappel into a cave'
```

If we wanted the second item, we'd write:

```javascript
var bucketList = ['Rappel into a cave', 'Take a falconry class', 'Learn to juggle'];
var listItem = bucketList[1];
console.log(listItem);
// Output: 'Take a falconry class'
```

# length property
It is often convenient to know how many items are inside of an array.

We can find this out by using one of an array's built in properties, called `<.length>`. We can attach this to any variable holding an array and it will return the number of items inside.

As an example:

```javascript
var bucketList = ['Rappel into a cave', 'Take a falconry class'];

console.log(bucketList.length);
// Output: 2
```

# push Method

JavaScript has a surprise for us: it has built in functions for arrays that help us do common tasks! Let's learn two of them.

First, `<push()>` allows us to add items to the end of an array. Here is an example of how this is used:

```javascript
var bucketList = ['item 0', 'item 1', 'item 2'];

bucketList.push('item 3', 'item 4');
```

The method `<push()>` would make the `<bucketList>` array look like:

```javascript
['item 0', 'item 1', 'item 2', 'item 3', 'item 4'];

```
Check out how `<push()>` works here:

1. It connects to `<bucketList>` with a period.
2. Then we call it like a function. That's because `<push()>` is a function and one that JavaScript allows us to use right on an array.

Connecting a function like this is common in JavaScript. Think: we've been connecting `<.log>` to `<console>` this whole time!

# pop Method

Now that we can `<push()>` items into an array, let's pop one off, using `<pop()>`.

`<pop()>` is similar to `<push()>`, except that it deletes the last item of an array. Here's an example:

```javascript
var bucketList = ['item 0', 'item 1', 'item 2'];

bucketList.pop();

console.log(bucketList);
// Output: [ 'item 0', 'item 1' ]
```

Notice that `<'item 2'>` was deleted from the end.

# Review Arrays

Nice work! In this lesson, we learned these concepts regarding arrays:

1. Arrays are lists and are a way to store data in JavaScript. Each item inside of an array is at a numbered position. Arrays are created with brackets `<[]>`.
2. We can access one item in an array using it's numbered position, with syntax like: `<myArray[0]>`.
3. Arrays have a `<length>` property, which allows you to see how many items are in an array.
4. Arrays also have their own methods, including `<push>` and `<pop>`, which add and subtract items from an array, respectively.

In the next lesson we'll learn how to loop over our arrays, which can bring our lists to life!

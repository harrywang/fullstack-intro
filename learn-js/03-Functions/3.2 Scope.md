# Global Scope

Scope is a big idea in programming, so let's start at a high level.

Scope refers to where in a program a variable can be accessed. The idea is that some variables are unable to be accessed everywhere within a program.

Think of it like a an apartment building. Everyone who lives in the apartment building is under the global scope of the building and its manager. So, if there are rats in the shared laundry room, everyone has access to the laundry machines, and the rats.

If you write a variable outside of a function in JavaScript, it's in the global scope and can be used by any other part of the program, just like the laundry room can be used by everyone in an apartment.

Let's practice this by making some global variables.

# Functional Scope
In our theoretical apartment building, you have your own apartment. It has stuff in it that is yours. Other people in the building can't access it. This is like functional scope. You have access to your stuff inside your apartment, and in the building – but not anyone else's apartment.

When we write variables inside a function, only that function has access to its own variables. Therefore, they are in the functional scope.

In addition to a function having access to its own variables, it also has access to variables in the global scope.

In the last exercise we created both variables in the global scope. That is, `<laundryRoom>` `<and mailRoom>` are accessible from anywhere in our program.

Now, let's make two variables within a functional scope.

# Scoping
Nice work! Now that we know how global and functional scope contain variables, let's organize some code to practice.

To the right, we provided you with incorrect sample code. If you try to run it as is, you will get an error because the `<console.log>` on line 20 references variables that are within the functional scope of `<myApartment>`.

Let's fix our scoping issues.

# Review Scope
This unit introduced you to scope.

1. Scope is the idea in programming that some variables are acessible/inaccessible from other parts of the program.
2. Global Scope refers to variables that are accessible to every part of the program.
3. Functional Scope refers to variables created inside functions, which are not accessible outside of its block.

Keep up the awesome job in the next lesson where we'll learn how to make lists and how to program JavaScript to do repetitive tasks for us with loops!

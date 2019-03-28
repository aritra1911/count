# Count
This is a class which is capable of counting forward in any base starting from zero. It keeps every digit as a separate entry in a list. This allows you to specify an integer base to count in. You may use your own glyphs and display them as you count in base n. This class was primarily written for the ease of programming the following.

> Note that counting backwards was also added as a feature recently, but programming sign alterations are still remaining. Basically I'm trying to make it possible to perform basic arithmetic using instances of this class.

## Order
This class forms the base of the following two classes with a sort algorithm implemented to sort the string supplied alphabetically.

### Enrep
Stands for `n-repetitions` which takes a string of characters and and repeats them in every permutation possible and returns a series of them all. You are free to change the length of the output and interestingly you can set the list to grow up to a specified length or use a fixed length instead. This class is specially useful for making word lists for cracking hashes.

### Permutation
Takes a string and outputs a series of the string (as a list) in every order possible using the characters in the string.

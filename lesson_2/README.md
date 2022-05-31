# Lesson 2 - Python Basics
## Built-in types and operations with them

1. Create a list and fill it with elements of various data types. Implement a test script for checking the type of list elements. Use the ```type()``` function to check the element type. The list of elements can be specified explicitly in the program without user request.

2. Implement the swapping the values of neighboring list items. Values are exchanged between elements with indexes ```0``` and ```1```, ```2``` and ```3```, etc. If there are an odd number of elements keep the last one in its place. Use the ```input()``` function to fill in the list of elements.

3. The User enters the month number as an integer from 1 to 12. Program must return the time of year according to month number (winter, spring, summer, autumn). Implement the solution using ```list``` and ```dict```.

4. The User enters a string of several words separated by spaces. Print each word from a new line. All lines need to be numbered. If the word is long print only the first 10 letters in the word.

5. Implement the "Rating" structure which is a list of decreasing natural numbers. Program must request a new rating value from the User. If there are elements with the same values in the rating, then a new element with the same value should be placed after them.
<br>_Example:_ 
<br>Initial list of raiting (natural numbers): ```7, 5, 3, 3, 2```
<br>User entered ```3```. Result: ```7, 5, 3, 3, 3, 2```.
<br>User entered ```8```. Result: ```8, 7, 5, 3, 3, 2```.
<br>User entered ```1```. Result: ```7, 5, 3, 3, 2, 1```.
<br>An initial list of natural numbers can be set in the code: ```my_list = [7, 5, 3, 3, 2]```

6. _(Optional)_ Implement the "Products" data structure. It should be a list of tuples. Each tuple stores information about a separate product. There should be two elements in the tuple — the product id number and a dictionary with product parameters: ```name```, ```price```, ```quantity```, ``unit``. The structure must be formed in program code by requesting all the data from the User.
<br>_Example:_
```
[
(1, {“name": “computer", “price": 20000, “quantity": 5, “units": “pcs.”}),
(2, {“name”: “printer", “price": 6000, “quantity": 2, “units": “pcs.”}),
(3, {“name": “scanner", “price": 2000, “quantity": 7, “units": “pcs"})
]
```
Implement product analytics. Initialize a dictionary in which each ```key``` is a characteristic of the product. The ```value``` is a list of characteristic values.

<br>_Example:_
```
{
“name": [“computer", “printer", “scanner"],
“price": [20000, 6000, 2000],
“quantity": [5, 2, 7],
“ed": [“pcs"]
}
```
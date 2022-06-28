# Python Basics
## Useful tools in Python

```
My goal in completing these tasks was not to demonstrate my knowledge of the basics of Python, but to use tasks to improve the practice of writing structured applications that satisfy some minimum requirements for code readability and lack of redundancy relative to the source task.
```

1. Implement a script that uses the employee's payroll formula in function. The formula is: ```(output in hours * rate per hour) + premium```. The script must be run with the parameters of the values used.

2. There is a list of numbers. The program must output the elements of the source list whose values are greater than the previous element.
_Hint:_ the elements should be arranged in the list. Use a generator to generate it.
_Example_
Source list: ```[300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]```
Result: ```[12, 44, 4, 10, 78, 123]```

3. Find numbers that are multiples of ```20``` or ```21``` for numbers ranging from ```20``` to ```240```. Solve the task in one line.
_Hint:_ use the ```range()``` function and the generator.

4. There is a list of numbers. Identify the list items that do not have repetitions. Form an array of numbers conforming to the requirement. Output the elements in the order of their sequence in the original list. Use the generator to complete the task.
_Example_
Source list: ```[2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]```
Result: ```[23, 1, 3, 10, 4, 11]```

5. Implement the formation of a list using the ```range()``` function and the capabilities of the generator. The list should include even numbers from ```100``` to ```1000``` (including the extreme elements). You need to get the result of calculating the product of all the elements of the list.
_Hint:_ use the ```reduce()``` function.

6. Implement two small scripts:
1) an iterator generating integers starting from the specified;
2) an iterator that repeats the elements of some list defined in advance. _Hint:_ use the ```count()``` and ```cycle()``` functions of the ```itertools``` module. Note that the created loop does not have to be infinite. Provide a condition for its completion.
_Example_
1) output integers starting from ```3```. When the number ```10``` is reached, we complete the cycle.
2) provide a condition under which the repetition of the list items will stop.

7. Implement the generator using a function with the ```yield``` keyword that creates the ```next``` value. When calling a function, a generator object must be created. The function is called as follows: ```for el in fact(n)```. It is responsible for obtaining the factorial of the number. In the loop, you need to output only the first ```n``` numbers, starting from ```1!``` and up to ```n!```.
_Hint:_ the factorial of the number ```n``` is the product of numbers from ```1``` to ```n```. 
_Example_
```4! = 1 * 2 * 3 * 4 = 24```

#### **Completed by**
Evgeny Nemykin | nonwander@gmail.com | _@nonwander_
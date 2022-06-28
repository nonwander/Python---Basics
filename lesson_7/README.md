# Python Basics
## Object-oriented programming - Advanced level
<div style="text-align: right; text-decoration: underline"> Practice, practice, more practice!</div>

```
My goal in completing these tasks was not to demonstrate my knowledge of the basics of Python, but to use tasks to improve the practice of writing structured applications that satisfy some minimum requirements for code readability and lack of redundancy relative to the source task.
```

1. Implement the ```Matrix``` class. Provide an overload of the class constructor _(the __init__() method)_, which must accept ```data``` _(a list of lists)_ to form a *matrix*.
</br>_Hint:_ A matrix is a system of some mathematical quantities arranged in a rectangular scheme.
</br>_Example:_ ```3 by 2, 3 by 3, 2 by 4```
```
31 32     3  5 32    3 5 8 3
37 43     2  4  6    8 3 7 1
51 86    -1 64 -8
```
- implement an overload of the ```__str__()``` method to output the matrix in the _usual form_.
- implement an overload of the ```__add__()``` method to implement the operation of adding two objects _(two matrices)_ of the ```Matrix``` class. The result of the addition should be a _new_ matrix.
</br>_Hint:_ the addition of matrix elements should be performed piecemeal:
_the first element of the first row of the first matrix is added with the first element of the first row of the second matrix, etc._

2. Implement a project for calculating the total consumption of fabric for the production of clothing. The main essence _(class)_ of this project is _clothing_, which can have a specific ```name```. The ```types``` of clothing in this project include a ```coat``` and a ```suit```. These types of clothing have parameters: ```size``` _(```V``` is for a coat)_ and ```height``` _( ```H``` is for a suit)_.
Use the formulas to determine the ```consumption``` of fabric for each type of clothing: </br>(V/6.5 + 0.5) - is for a coat </br>(2 *H + 0.3) - is for a suit.
- test the operation of these methods on real data;
- implement a general calculation of fabric consumption;
- implement _abstract classes_ for the _main classes_ of the project;
- use the decorator ```@property```.

3. Implement a program of work with organic cells consisting of elementary particles. You need to create a ```Cell``` class. Initialize the parameter ```corresponding``` to the number of cells of the cell (an integer). The class must implement methods for overloading arithmetic operators:
_addition_ ```__add__()```, _subtraction_ ```__sub__()```, _multiplication_ ```__mul__()```, _division_ ```__truediv__()```.
</br>These methods should be applied only to Cells and perform increase, decrease, multiplication and integer _(rounded to whole)_ Cell division.
 - *Addition.* The union of two Cells. The number of particles of the common Cell should be equal to the sum of the particles of the original two Cells.
 - *Subtraction.* Two Cells are involved. The operation should be performed only if the difference in the number of particles of two Cells is greater than zero, otherwise the corresponding message should be displayed.
 - *Multiplication.* A common Cell of two is created. The number of particles of a common Cell is defined as the product of the number of particles of these two Cells.
 - *Division.* A common Cell of two is created. The number of particles of a common Cell is defined as the integer division of the number of particles of these two Cells.

Iimplement the ```make_order()``` method in the class, which accepts an instance of the class and the number of particles in a row. This method allows you to organize Cells in rows.
The method should return a string of the form ```*****\n*****\n*****```, where the number of particles between ```\n``` is equal to the passed argument. If there are not enough particles to form a row, then all the remaining ones are written to the last row.
</br>_Example:_
 - the number of particles in a Cell is ```12```, the number of particles in a row is ```5```. The ```make_order()``` method will return the string:
</br>```*****\n*****\n**```.
 - the number of particles in a Cell is ```15```, the number of particles in a row is ```5```. The ```make_order()``` method will return the string:
</br>```*****\n*****\n*****```.
</br></br>
#### **Completed by**
Evgeny Nemykin | nonwander@gmail.com | _@nonwander_
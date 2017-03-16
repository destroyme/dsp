# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Python's lists and tuples are similar in that they store data in a structured way, but have differences in the representation and intention of that structure. 

Lists are designed to *typically* store sequential homogenous data, or rather 'things' of the same type. A few examples of homogenous data is a list of grocery items where a banana is a type of grocery, or cereal is a type of grocery, or a list of real numbers where 1.0 is a real number, 1e6 is a real number. Lists are also mutable structures where the values within it can be edited (delete values, replace values, sort them, etc.)  during the lifetime of your program.

Tuples are designed to *typically* store heterogeous data, or rather 'things' of different types. They're different from lists where they're not meant to represent a sequence of the same type, but rather explicitly state the sequence of different types associated with a value. An example of a tuple is a point in time, (YEAR, MONTH, DAY, HOUR, MINUTES) : (2017, 3, 15, 6, 51) where each position of the tuple represents an element of time. Tuples also differ from lists in mutability; tuples are immutable structures. Their immutable property enables them to be a hashable element, giving them the ability to be used as keys in dictionaries.

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Sets and lists are different data structures designed to store data, and have different principles guiding that storage.

Python's sets stem from Set Theory in mathematics, where a set is a collection of *distinct* objects that allow you to perform operations related to the field, such as unions, intersections, and differences.

A set differs from a list in a few key areas. In a set you're unable to have duplicate objects, whereas in a list duplicates are permitted:
```python
>>> [1, 1, 2, 3]
[1, 1, 2, 3]
>>> set([1, 1, 2, 3])
{1, 2, 3}
```

Another key difference between a set and a list, is a set is unordered. Any ordered structure you pass it will inevitably be restructured to python's partial ordering. This also gives way to the question 'how do you find an element of a set?'. Python uses hash lookups to search for an element, so elements that aren't hashable (lists, dictionaries, *SETS*) can not be contained in a set. A similarity of sets and lists are in their mutability. They both have the abilitiy to continuously change state within your program. Here's an example of these concepts:

```python
>>> a = set([1.0,-1.0,0]) # it will not retain the order of the list
>>> a 
{-1.0, 0, 1.0}
>>> a.add([1,2]) # attempting to add a non-hashable element
...
TypeError: unhashable type: 'list'
>>> a.add(-2) # set mutability
>>> a
{-1.0, 0, 1.0, -2}
>>> 0 in x # use the in operator to FIND single elements in the set.
True
>>> b = [1,2,3]
>>> b.append(4) # list mutability & order
>>> b
[1, 2, 3, 4]
```

The performance of finding an element in a set is much faster than it is in a list. A set contains hashable elements, so a hash function is used to quickly search for an item. List items may or may not be hashable, so Python assumes they're not, and uses a computationally slower search method than a set would for an item.

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> The `lambda` in Python stems from lambda calculus, a formal system in mathematical logic expressing computations using functions. `lambda` acts as a anonymous function (a function without a name) that can hold a large set of arguments but only a single expression to evaluate. Its narrow focus provides us with a fantastic tool for defining small functions and passing them to other functions (a higher order function) such as getters and setters, filters, and maps.

A great example of a lambda is the key paramater in the sorted function of an iterable:
```python
>>> sorted(range(1,11), key=lambda x: x%2 != 0) # sorting a list by even then odd integers
```
The key passes through the list evaluating the lambda `x % 2 != 0` for each element. The list is then sorted according to this new evaluation.


---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions are a way of transforming lists into another list.

They provide syntax that is very similar to set-builder notation in mathematics: {x<sup>2</sup> | x ϵ `Z`, 0 < x < 6}, building a set of {1,4,9,16,25}, where in python the same set expressed as list comprehension is:

```python
[x**2 for x in range(10) if 0 < x < 6]
```

It's so close to the notation! 

These list comprehensions provide a friendly syntax to express lists, but are of course only 1 way of expressing them. The same list can be expressed with a `map` and a `filter`, where a `map` provides us a way to map a function to an iterable, and a `filter` allows us to filter out items from an iterable, only keeping the items that satisfy true for a boolean function passed to it. Here's a few examples using both:

```python
>>> # MAP
>>> x_map = map(lambda x: x**2, range(1,6)) # squaring the iterable returned by range
>>> list(x_map)
[1, 4, 9, 16, 25]

>>> # FILTER
>>> x_filt = filter(lambda n: math.sqrt(n) % 1 == 0, range(1,27)) # a simple check if an element is a perfect square
>>> list(x_filt)
[1, 4, 9, 16, 25]

>>> # MAP AND FILTER
>>> x = map(lambda x: x**2, filter(lambda x: 0 < x < 6, range(10)))
>>> list(x)
[1, 4, 9, 16, 25]
```

To decompose this last one a bit, you'll see that I used a map and it follows the same structure as the first example. The first paramater is a lambda that returns the square of the argument passed to it (f(x) = x<sup>2</sup>). The second parameter of map is meant to be an interable, so here we're expecting to see the list [1,2,3,4,5]. To produce that list, we used a `filter`. The filter parsed through a list looking only for the items (0, 6). This is how we produced the list [1,2,3,4,5] for the map function, which then uses that list to return that list squared.

You'll notice that I converted the return value of map into a list. This is because maps return an iterator and in order to retrieve these values, you need to use something to iterate over them. The same functionality can be produced using the comprehension syntax by using generator comprehension:

```python
>>> x = (x**2 for x in range(10) if 0 < x < 6)
>>> list(x)
[1, 4, 9, 16, 25]
```

The capabilities of map and filter are incredibly similar to list comprehension, and can do this within a more condensed syntax.

The comprehension syntax can also be applied to dictionaries and sets too! Sets are pretty straight forward and function a lot like list comprehension, except they of course have set properties:

```python
>>> {x**2 for x in range(10) if 0 < x < 6}
{1, 4, 9, 16, 25}
>>>
>>> words = ['gustav', 'germany', 'berlin', 'hamburg']
>>> {w[0] for w in words} # set of first letter of all words
{'b', 'h', 'g'}
```

Dictionary comprehension has syntax similar to sets, but the values returned to the dictionary have the syntax *key : value*. Let's have a look at it:

```python
>>> # My friend's favorite sports
>>> d = {'Jess' : 'Football', 'Joe' : 'Football', 'Erica' : 'Basketball', 'Rob' : 'Basketball'};

>>> # Let's make a new dict of my friends who just like Basketball
>>> basketball_fans = {key : value for key, value in d.items() if value == 'Basketball'}
>>> basketball_fans
{'Erica': 'Basketball', 'Rob': 'Basketball'}
```

To break this down a bit:
1. We see in the beginning we have the key : value syntax we're used to with dictionaries, and in comprehensions where those are the new values to be returned.
2. The `for` indicates we're about to begin a loop that will iterate over a structure that returned an iterable of `(key, value)`. We'll store those as their respective names.
3. We're filtering `d.items()` for all values that equal `'Basketball'`.
4. A new dictionary is returned upon completion!



---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)






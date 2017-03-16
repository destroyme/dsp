# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

Python's lists and tuples are similar in that they store data in a structured way, but have differences in the representation and intention of that structure. 

Lists are designed to *typically* store sequential homogenous data, or rather 'things' of the same type. A few examples of homogenous data is a list of grocery items where a banana is a type of grocery, or cereal is a type of grocery, or a list of real numbers where 1.0 is a real number, 1e6 is a real number. Lists are also mutable structures where the values within it can be edited (delete values, replace values, sort them, etc.)  during the lifetime of your program.

Tuples are designed to *typically* store heterogeous data, or rather 'things' of different types. They're different from lists where they're not meant to represent a sequence of the same type, but rather explicitly state the sequence of different types associated with a value. An example of a tuple is a point in time, (YEAR, MONTH, DAY, HOUR, MINUTES) : (2017, 3, 15, 6, 51) where each position of the tuple represents an element of time. Tuples also differ from lists in mutability; tuples are immutable structures. Their immutable property enables them to be a hashable element, giving them the ability to be used as keys in dictionaries.

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

Sets and lists are different data structures designed to store data, and have different principles guiding that storage.

Python's sets stem from Set Theory in mathematics, where a set is a collection of *distinct* objects that allow you to perform operations related to the field, such as unions, intersections, and differences.

A set differs from a list in a few key areas. In a set you're unable to have duplicate objects, whereas in a list duplicates are permitted:
```python
>> [1, 1, 2, 3]
[1, 1, 2, 3]
>> set([1, 1, 2, 3])
{1, 2, 3}
```

Another key difference is a set is unordered, giving way to the question 'how do you find an element of a set?'. Python uses hash lookups to search for an element, so elements that aren't hashable (lists, dictionaries, *SETS*) can not be contained in a set.

```python
>>> a = set([1.0,-1.0,0]) # it will not retain the order of the list
>>> a 
{-1.0, 0, 1.0}
>>> a.add([1,2])
...
TypeError: unhashable type: 'list'
>>> 0 in x # you use the in function to search for items in the set.
True
```

A similarity of sets and lists are in their mutability. They both have the abilitiy to continiously change state within your program, and 

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> REPLACE THIS TEXT WITH YOUR RESPONSE

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> REPLACE THIS TEXT WITH YOUR RESPONSE

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






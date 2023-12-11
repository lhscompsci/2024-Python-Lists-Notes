# CSP Python Lists Notes

What is a list?
- a list is a group of items which are accessed through a single identifier
- This of this as a collection of boxes or spots that all store the same type of values
- each spot stores a value of this type
  - essentially, this is a single variable of the specified type

```python
myList = [0,0,0,0,0,0,0,0,0,0]

price = [32.23, 12.25, 56.38, 77.55, 39.0]
```

Lists are an example of data abstraction.  The use of 5 different storage locations to store all of the values is hidden away from the user.

One name or identifier is used to manage multiple variables or containers for values makes the program nuch easier to manage.

Lists allow you to use one identifier to group items together

To create an empty list:
```python
thisList =[]
```

To create a list with 3 strings:
```python
coworkers = ["Sarah", "Matt", "Sophie"]
```

The index indicates which value in the array/list is being accessed. 
- above, "Sarah" is index 0
- "Matt" is index 1
- "Sophie" is index 2

The index allows you to get or change data in a list:
```python
coworkers[1]="Tim"
```


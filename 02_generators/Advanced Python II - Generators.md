
# Generators
## Generator functions (yield... )
## Generator expressions


```python
a = [1,2,3,4]
b = (i*i for i in a)
b
```




    <generator object <genexpr> at 0x10feabee8>



## General Syntax

    (expression for i in s if cond1
                for j in t if cond2
                ...
                if condfinal)

## Meaning

    for i in s:
        if cond1:
            for j in t:
                if cond2:
                    ...
                    if condfinal: 
                        yield expression



```python
l1 = [i*3 for i in range(0,10) if i % 2 == 0]
l2 = (i*3 for i in range(0,10) if i % 2 == 0)
```


```python
len(l1)
```




    5




```python
len(l2)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-5-d6c9a6b1dc53> in <module>()
    ----> 1 len(l2)
    

    TypeError: object of type 'generator' has no len()


## Ex1: sum of all odd numbers under 5000



```python
def odd_numbers(threshold):
    i = 1
    while i < threshold:
        if i % 2 == 1:
            yield i
        i += 1

sum(odd_numbers(5000))







```




    6250000




```python
sum((x for x in range(1,5000) if x % 2 == 1))





```




    6250000




```python
sum(x for x in range(1,5000) if x % 2 == 1)
```




    6250000



## BTW what is range?
function? NO!

"The range type represents an immutable sequence of numbers and is commonly used for looping a specific number of times in for loops."

"The advantage of the range type over a regular list or tuple is that a range object will always take the same (small) amount of memory, no matter the size of the range it represents (as it only stores the start, stop and step values, calculating individual items and subranges as needed)."

[https://docs.python.org/3/library/stdtypes.html#typesseq-range]


```python
r1 = range(0,10)
```


```python
dir(r1)
```




    ['__class__',
     '__contains__',
     '__delattr__',
     '__dir__',
     '__doc__',
     '__eq__',
     '__format__',
     '__ge__',
     '__getattribute__',
     '__getitem__',
     '__gt__',
     '__hash__',
     '__init__',
     '__iter__',
     '__le__',
     '__len__',
     '__lt__',
     '__ne__',
     '__new__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__reversed__',
     '__setattr__',
     '__sizeof__',
     '__str__',
     '__subclasshook__',
     'count',
     'index',
     'start',
     'step',
     'stop']




```python
iter(r1)
```




    <range_iterator at 0x10fea6a20>



## Ex2: Count the letters in hungarian towns with zipcode 3XXX

- cat hu_zipcodes.txt|head


        2000	Szentendre
        2009	Pilisszentlászló
        2011	Budakalász
        2013	Pomáz
        2014	Csobánka
        2015	Szigetmonostor
        2016	Leányfalu
        2017	Pócsmegyer
        2021	Tahitótfalu	Tótfalu
        2022	Tahitótfalu	Tahi

- empty or blank lines in file!
- just the second word counts!



```python
def hu_zipcodes1():
    sum_ = 0
    with open("hu_zipcodes.txt", "r") as zfile:
        for line in zfile:
            words = line.split()
            if len(words) > 1:
                if words[0].startswith("3"):
                    sum_ += len(words[1])
    return sum_  # aaaarrrrrr...











```


```python
hu_zipcodes1()
```




    5033




```python
def hu_zipcodes2():
    lines = open("hu_zipcodes.txt", "r")
    splitted_lines = (line.split() for line in lines)
    not_empty_splitted_lines = (words for words in splitted_lines if len(words) > 1)
    z3xxx_town_names = (words[1] for words in not_empty_splitted_lines if words[0].startswith("3"))
    z3xxx_town_lenghts = (len(t) for t in z3xxx_town_names)
    return sum(z3xxx_town_lenghts)

hu_zipcodes2()










```




    5033




```python
def hu_zipcodes3():
    not_empty_splitted_lines = (words
                                for words in (line.split() 
                                              for line in open("hu_zipcodes.txt", "r"))
                                if len(words) > 1)
    z3xxx_town_names = (words[1] for words in not_empty_splitted_lines if words[0].startswith("3"))
    return sum(len(t) for t in z3xxx_town_names)

hu_zipcodes3()








```




    5033




```python
def hu_zipcodes4():
    return sum(
        len(words[1])
        for words in (line.split()
                      for line in open("hu_zipcodes.txt", "r"))
        if len(words) > 1 and words[0].startswith("3"))

hu_zipcodes4()






```




    5033



## Ex3: remove duplicate town names before sum! How?!


```python
def sumlen(strs):
    return sum(len(s) for s in strs)


def hu_zipcodes5():
    return sumlen(words[1]
                  for words in (line.split()
                                for line in open("hu_zipcodes.txt", "r"))
                  if len(words) > 1 and words[0].startswith("3"))

hu_zipcodes5()


```




    5033




```python
def usumlen(strs):
    # keeps order!!!
    _olds = []
    def _s_is_new(s):
        if s not in _olds:
            _olds.append(s)
            return True
        else:
            return False
    return sum(len(s) for s in strs if _s_is_new(s))


def usumlen2(strs):
    # lost order!!!
    return sum(len(s) for s in set(strs))


def hu_zipcodes6():
    return usumlen2(words[1]
                  for words in (line.split()
                                for line in open("hu_zipcodes.txt", "r"))
                  if len(words) > 1 and words[0].startswith("3"))

hu_zipcodes6()









```




    4743




```python

```


```python

```

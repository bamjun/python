    a = set([1, 1, 3])
    a = {1, 3}
    a = {1, 1, 3}
    a = {1, 3}
    
>>> a = set([2, 3, 4, 5, 6, 7])
>>> a
{2, 3, 4, 5, 6, 7}
>>> 10 in a
False
>>> 2 in a
True


>>> for i in {1, 2, 4, 8, 16,32}:
...     print(i)
...
32
1
2
4
8
16
#set은 순서가 없다.

#.... 추가 add update  제거 remove discard
>>> a
{2, 3, 4, 5, 6, 7}
>>> a.add(10)
>>> a
{2, 3, 4, 5, 6, 7, 10}
>>> a.update([12,13,14])
>>> a
{2, 3, 4, 5, 6, 7, 10, 12, 13, 14}
>>> a.remove(4)
>>> a
{2, 3, 5, 6, 7, 10, 12, 13, 14}
>>> a.remove(4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 4
  
>>> a.discard(2)
>>> a
{3, 5, 6, 7, 10, 12, 13, 14}
>>> a.discard(2)
>>> a
{3, 5, 6, 7, 10, 12, 13, 14}


python 알고리즘 연습
=================


code snippet
------------

#### 빠른 입출력
```python
import sys
input = sys.stdin.readline()
```

#### 유클리드 호제법
```python
def gcd(a,b):
    return a if b == 0 else gcd(b, a%b)

def lcm(a,b):
    return a*b/gcd(a,b)
```


#### python 스타일 array filter
```python
scores = [70, 60, 80, 90, 50]
filtered = [s for s in scores if s >= 70 ]
#=> [70, 80, 90] 
```



알고리즘 정리
----------
[알고리즘 정리](./algorithm/README.md)
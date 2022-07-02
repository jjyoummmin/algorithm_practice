string formatting
-----------------

실수 자릿수
```python
result = 1.68
f'{result:.1f} MB'   
```

hex
```python
f'{n:X}*{x:X}={y:X}'
```

유클리드 호제법
-----------
```python
def gcd(a,b):
    return a if b == 0 else gcd(b, a%b)

def lcm(a,b):
    return a*b/gcd(a,b)
```

2d-array
--------
```python
arr = [[0] * w for _ in range(h)]
```
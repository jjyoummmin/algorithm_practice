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

walrus operator
---------------
python 3.8 부터 지원
`:=` 대입 표현식

```python
if (n := len(a)) > 10:
    print(f"List is too long ({n} elements, expected <= 10)")
```

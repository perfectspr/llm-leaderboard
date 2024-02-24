***
Generate a bash script to create 10 files, with the names A1.txt through A10.txt
### Answer
```bash
for i in {1..10}
do
  touch A$i.txt
done
```
***
Write a Oracle SQL query to find the nth number in the Fibonacci Sequence.
### Answer
```sql
WITH fibonacci (n, a, b) AS (
  SELECT 1, 0, 1 FROM dual
  UNION ALL
  SELECT n+1, b, a+b FROM fibonacci WHERE n < :n
)
SELECT a AS fibonacci_number FROM fibonacci WHERE n = :n;
```
***
How can I install the Pandas package in Python?
### Answer
python -m pip install pandas
or
pip install pandas
***
Edit the following code to print out all even numbers from 1 to 10.
```python
for i in range(1,11):
    print(i)
```
### Answer
```python
for i in range(1,11):
    if i % 2 == 0:
        print(i)
```

***
Create a function to calculate the area of a given circle.
### Answer
```python
def area_circle(radius):
    return 3.14 * (radius**2)
```

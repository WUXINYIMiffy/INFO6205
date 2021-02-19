**XINYI WU (001529267)**

# Program Structures & Algorithms

**Spring 2021** **Assignment No. 2**

### Task:

Determine the relationship between the number of objects(n) and the number of pairs(m) generated to accomplish this(i.e. to reduce the number of components from n to 1).

### Output:

- Data points
  - `/INFO6205/Python/src/union_find/stats.csv`

### Relationship Conclusion:

When the number of objects(n) gets larger, the number of pairs(m)  gets larger. In general, the relationship between the number of objects(n) and  the number of pairs(m) is roughly like **m = 6E-05n^2 + 4.3525n - 620.83** 

### Evidence to support the conclusion:

According to the output, if we just calculate the number of pairs which are getting connected through union, **m=n-1**. If we count all the list of pairs generated, when n = 10000, **m≈4.3525n**. It is a linear relationship. 

### Graphical representation:

![relationship between n and m.png](/Users/mac/Documents/GitHub/INFO6205/Reports/assignment 3/relationship between n and m.png)

### Unit tests result:
![tests_passed.png](/Users/mac/Documents/GitHub/INFO6205/Reports/assignment 3/tests_passed.png)






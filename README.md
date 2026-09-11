# Logic Box - Pattern Generator and Number Analyzer
 
Python program for my PR.2 assignment. It's menu based - you pick an option, it does its thing, then shows the menu again until you exit.
 
Two things it can do:
1. Generate a Pattern
2. Analyze a Range of Numbers
3. Exit
## Pattern Generator
 
5 pattern options - increasing stars, increasing numbers, decreasing stars, decreasing numbers, and decreasing start numbers. You choose the type, then how many rows, and it prints it.
 
Sample run (option 1, increasing stars, 5 rows):
 
```
Select an option:
1. Generate a Pattern
2. Analyze a Range of Numbers
3. Exit
Enter your choice: 1
 
Select a pattern type:
1. Increasing Stars
2. Increasing Numbers
3. Decreasing Stars
4. Decreasing Numbers
5. Decreasing Start Numbers

Enter your choice (1-5): 1

Enter the number of rows for the pattern: 5
 
Pattern:
*
**
***
****
*****
```
 
![Pattern Genrator](Screenshots/img1.png)


## Number Analyzer
 
Give it a start and end number, it prints odd/even for every number in between.

 
```
Enter the start of the range: 1
Enter the end of the range: 5
1 is odd.
2 is even.
3 is odd.
4 is even.
5 is odd.
```

![Number Analyzer](Screenshots/img2.png)

## Exit

```
Exiting the program. Goodbye!
```
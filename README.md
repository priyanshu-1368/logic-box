# Logic Box - Pattern Generator and Number Analyzer
 
Python program for my PR.2 assignment. It's menu based - you pick an option, it does its thing, then shows the menu again until you exit.
 
Two things it can do:
1. Generate a Pattern
2. Analyze a Range of Numbers
3. Exit

## Pattern Generator
 
10 pattern options - increasing stars, increasing numbers, decreasing stars, decreasing numbers, decreasing start numbers, hollow square, diamond pattern, butterfly pattern, number pyramid, and star pyramid. You choose the type, then how many n, and it prints it.
 
Sample run (option 1, increasing stars, 5 n):
 
```
══════════════════════════════════════════════════════════
  ╔══════════════════════════════════════════════════════╗
  ║    PATTERN GENERATOR & NUMBER ANALYZER CLI APP       ║
  ╚══════════════════════════════════════════════════════╝
══════════════════════════════════════════════════════════

┌── [ MAIN MENU ] ───────────────────────────────────────┐
│  [1] Generate a Pattern                                │
│  [2] Analyze a Range of Numbers                        │
│  [3] Exit                                              │
└────────────────────────────────────────────────────────┘
 ➤ Enter your choice: 1

──────────────────────────────────────────────────────────

  ┌── [ SELECT PATTERN TYPE ] ───────────────────────────┐
  │  [1] Increasing Stars      [6] Hollow Square         │
  │  [2] Increasing Numbers    [7] Diamond Pattern       │
  │  [3] Decreasing Stars      [8] Butterfly Pattern     │
  │  [4] Decreasing Numbers    [9] Number Pyramid        │
  │  [5] Decreasing Start Num  [10] Star Pyramid         │
  └──────────────────────────────────────────────────────┘
  ➤ Enter pattern choice (1-10): 1
  ➤ Enter the value: 5

  ┌── [ PATTERN RESULT ] ─────────────────────────────────
  │ *
  │ **
  │ ***
  │ ****
  │ *****
  └──────────────────────────────────────────────────────
```


## Number Analyzer
 
Give it a start and end number, it prints odd/even for every number in between.

 
```
┌── [ MAIN MENU ] ───────────────────────────────────────┐
│  [1] Generate a Pattern                                │
│  [2] Analyze a Range of Numbers                        │
│  [3] Exit                                              │
└────────────────────────────────────────────────────────┘
 ➤ Enter your choice: 2

──────────────────────────────────────────────────────────
  ┌── [ NUMBER RANGE ANALYZER ] ─────────────────────────┐
  ➤ Enter the start of the range: 1
  ➤ Enter the end of the range: 5
  └──────────────────────────────────────────────────────┘

  ┌── [ ANALYSIS RESULT ] ────────────────────────────────
  │  1 is odd.
  │  2 is even.
  │  3 is odd.
  │  4 is even.
  │  5 is odd.
  └──────────────────────────────────────────────────────
```

## Exit

```
══════════════════════════════════════════════════════════
  [✓] Exiting the program. Goodbye!
══════════════════════════════════════════════════════════
```
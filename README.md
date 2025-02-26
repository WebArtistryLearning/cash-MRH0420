[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=18413331)
# Cash

## Instructions

Suppose you work at a store and a customer gives you $1.00 (100 cents) for candy that costs $0.50 (50 cents). You’ll need to pay them their “change,” the amount leftover after paying for the cost of the candy. When making change, odds are you want to minimize the number of coins you’re dispensing for each customer, lest you run out (or annoy the customer!).

In a file called `cash.py`, implement a program in Python that prints the minimum coins needed to make the given amount of change, in cents. **You have coins of denominations of 25 cents, 10 cents, 5 cents, and 1 cent.**

## Sample Checkpoints

### Sample Checkpoint 1

**Sample Input**

```
25
```

**Sample Output**

```
1
```

**Comment**

You can give the customer one coin of 25 cents.

### Sample Checkpoint 2

**Sample Input**

```
70
```

**Sample Output**

```
4
```

**Comment**

You can give the customer two coins of 25 cents and two coins of 10 cents, for a total of 25 + 25 + 10 + 10 = 70 cents.

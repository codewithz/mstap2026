# Algorithms in Java — Part 1: Big O & Sorting Concepts

This guide covers the theory before any Java-specific tooling: how we
measure efficiency, and how the three classic "simple" sorts actually
work under the hood. Part 2 (`06-sorting-in-java-and-primes-challenge.md`)
picks up with Java's built-in sorting tools, custom ordering, and the
primes challenge.

---

## The Concept

### Big O notation

Big O notation describes how an algorithm's **running time** grows as
the input size `n` gets larger. It focuses on the **worst case** and
ignores constants and hardware, so we can compare algorithms fairly —
independent of which machine they run on.

The key idea: we care about what happens when `n` gets big. An
algorithm that's slower on 10 items but scales better will always win
on 10,000,000 items.

**Common complexities, fastest to slowest:**

| Notation | Name | What it means | Example in Java |
|---|---|---|---|
| `O(1)` | Constant | Execution time doesn't change as the volume of data grows | `myArray[i]` |
| `O(log n)` | Logarithmic | Grows very slowly — doubling the data adds just one more step | binary search in a sorted list |
| `O(n)` | Linear | Grows in step with the data — twice the data, twice the time | loop once over a list |
| `O(n log n)` | Linearithmic | A little slower than linear, but the realistic best for sorting | efficient sorts (merge / quick) |
| `O(n²)` | Quadratic | Grows dramatically — twice the data means **four times** the time | nested loops (e.g. bubble sort) |

### Real-life analogies (use these to build intuition before any code)

Two stories per complexity — the first is the one to lead with, the
second is a quick backup if a different picture lands better with a
particular group.

**`O(1)` — Constant**
- *Pressing a floor button in a lift.* Press "9" and you go to floor
  9. It makes no difference whether the building has 9 floors or 90 —
  one press, one action, done. The size of the building never enters
  into it.
- *Backup: grabbing your front door key from your pocket.* You know
  exactly which key it is by feel. Doesn't matter how many other keys
  are on the ring.

**`O(log n)` — Logarithmic**
- *Finding an author in an alphabetised bookshop.* Looking for a
  Terry Pratchett novel? Walk to roughly the "P" section — you don't
  start at "A" and check every shelf. Once you're near "P," you don't
  scan every author either: is it before or after "Pratchett"?
  Narrow again. Each glance eliminates a huge chunk of the shop, not
  just one book at a time.
- *Backup: the "higher or lower" number-guessing game.* Someone picks
  a number between 1 and 1,000; you guess, they say "higher" or
  "lower." Guess 500, then 250 or 750, then halve again. 1,000
  numbers take at most **10 guesses**; a million numbers take at most
  **20**. This is precisely what binary search does to a sorted list.

**`O(n)` — Linear**
- *Counting how many sweets are left in a jar by counting them one by
  one.* No shortcuts — you touch every single sweet once. Twice as
  many sweets, twice as long to count them.
- *Backup: reading every name tag at a conference to find one person.*
  Same idea, more people. If there's no seating plan or alphabetical
  order to exploit, you check attendees one at a time.

**`O(n log n)` — Linearithmic**
- *Sorting a stack of exam papers by splitting into piles.* Split the
  stack in half, then those halves in half again, until each pile has
  one paper (trivially "sorted"). Merge pairs of piles back together
  *in order*. The repeated halving is the `log n` part; re-merging
  every paper back in at every level is the `n` part. This is
  literally how merge sort works.
- *Backup: a big pile of laundry sorted by handing socks to two
  helpers, who each hand half to two more helpers, and so on — then
  everyone merges their small sorted piles back together going back
  up the chain.*

**`O(n²)` — Quadratic**
- *Everyone in a room shaking hands with everyone else.* 10 people
  make 45 handshakes. 20 people make 190 — not double, **more than
  four times as many**. Every item having to compare against every
  other item is exactly what the nested loops in bubble/selection
  sort are doing, and it's why they collapse on large lists.
- *Backup: finding the tallest person in a crowd by comparing every
  single person against every other single person,* instead of just
  tracking the tallest-so-far as you go once through the crowd (which
  would only be `O(n)` — a nice bridge into "there's usually a
  smarter way").

**A useful gut-check to leave the room with:** whenever an algorithm
has **one loop**, think `O(n)`. Whenever it has **a loop nested inside
another loop** covering the same data, think `O(n²)`. Whenever it
**halves the problem each step**, think `O(log n)`. That single
pattern-recognition habit gets candidates most of the way to reading
Big O off real code without memorising formulas.

### Seeing the growth for real numbers

Talking about "n" is abstract — plugging in actual numbers makes the
gap concrete. Here's roughly how many operations each complexity
does for a few input sizes (rounded):

| n | O(1) | O(log n) | O(n) | O(n log n) | O(n²) |
|---|---|---|---|---|---|
| 10 | 1 | 3 | 10 | 33 | 100 |
| 100 | 1 | 7 | 100 | 664 | 10,000 |
| 1,000 | 1 | 10 | 1,000 | 9,966 | 1,000,000 |
| 10,000 | 1 | 13 | 10,000 | 132,877 | 100,000,000 |

At `n = 10` the difference between `O(n)` and `O(n²)` looks trivial
(10 vs. 100). By `n = 10,000` it's the difference between "instant"
and "100 million operations" — the gap doesn't grow steadily, it
explodes. That's the entire point of Big O: it tells you *which side
of that explosion* an algorithm is going to land on before you ever
run it on real-sized data.

### Watch it happen live

This is worth actually running in front of the room rather than just
describing — it makes the gap between complexity classes visceral
rather than theoretical. This version times all five complexities
side by side, each using a genuine Java example of that complexity
class: a single array access for `O(1)`, `Arrays.binarySearch` for
`O(log n)`, a single pass for `O(n)`, `Arrays.sort` for `O(n log n)`,
and nested loops for `O(n²)`.

```java
import java.util.Arrays;

public class BigODemo {
    static long sink = 0; // accumulates real work so the JIT can't optimise the loops away

    public static void main(String[] args) {
        int[] sizes = {5000, 10000, 20000, 40000, 80000};

        System.out.println("n\tO(1)\tO(log n)\tO(n)\tO(n log n)\tO(n^2)");
        for (int n : sizes) {
            long constantTime = timeConstant(n);
            long logTime = timeLogarithmic(n);
            long linearTime = timeLinear(n);
            long nLogNTime = timeNLogN(n);
            long quadraticTime = timeQuadratic(n);
            System.out.println(n + "\t" + constantTime + "\t" + logTime
                    + "\t\t" + linearTime + "\t" + nLogNTime + "\t\t" + quadraticTime);
        }
        System.out.println("(sink=" + sink + ", ignore this - it just stops the JIT cheating)");
    }

    // O(1): a single array access, regardless of n
    static long timeConstant(int n) {
        int[] data = new int[n];
        long start = System.nanoTime();
        sink += data[n / 2]; // one access, no matter how big the array is
        long end = System.nanoTime();
        return (end - start) / 1_000_000;
    }

    // O(log n): binary search on a sorted array
    static long timeLogarithmic(int n) {
        int[] data = new int[n];
        for (int i = 0; i < n; i++) data[i] = i; // already sorted
        long start = System.nanoTime();
        int index = Arrays.binarySearch(data, n - 1); // worst case: last element
        long end = System.nanoTime();
        sink += index;
        return (end - start) / 1_000_000;
    }

    // O(n): one pass over n items
    static long timeLinear(int n) {
        long start = System.nanoTime();
        for (int i = 0; i < n; i++) {
            sink += i;
        }
        long end = System.nanoTime();
        return (end - start) / 1_000_000;
    }

    // O(n log n): sorting n items (Arrays.sort on a primitive array uses a dual-pivot quicksort)
    static long timeNLogN(int n) {
        int[] data = new int[n];
        java.util.Random rnd = new java.util.Random(42);
        for (int i = 0; i < n; i++) data[i] = rnd.nextInt();
        long start = System.nanoTime();
        Arrays.sort(data);
        long end = System.nanoTime();
        sink += data[0];
        return (end - start) / 1_000_000;
    }

    // O(n^2): every item compared against every other item
    static long timeQuadratic(int n) {
        long start = System.nanoTime();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                sink += 1;
            }
        }
        long end = System.nanoTime();
        return (end - start) / 1_000_000;
    }
}
```

```
# Output (timings will vary slightly by machine, but the shape holds):
n	O(1)	O(log n)	O(n)	O(n log n)	O(n^2)
5000	0	0		0	4		7
10000	0	0		0	4		3
20000	0	0		0	5		14
40000	0	0		2	5		57
80000	0	0		0	10		146
(sink=2053185745, ignore this - it just stops the JIT cheating)
```

**Quick IDE tip while typing this out live:** in IntelliJ (and most
Java-aware editors with live templates), typing `sout` and hitting Tab
expands to `System.out.println();` with the cursor already inside the
parentheses — worth showing candidates once, since this file has
several `System.out.println` calls and it saves a lot of typing for
the rest of the course.

Walk the room through what each column is saying:

- **`O(1)` and `O(log n)` stay at 0ms the entire way down**, even at
  80,000 items. That's the point, not a bug — a single array lookup
  and a binary search are so fast that even 16x more data doesn't
  register on the stopwatch. This is exactly why "does it scale?" is
  a non-question for these two: for all practical purposes, it
  already scales to any size you'll ever throw at it.
- **`O(n)` stays close to 0ms too**, only occasionally ticking up to
  1–2ms even at the largest size. A single pass over data is cheap.
- **`O(n log n)` grows, but gently** — roughly 4ms at 5,000 items,
  roughly 10ms at 80,000. Note it's *not* proportional: the input grew
  16x but the time grew roughly 2–3x. That's the "slightly worse than
  linear" behaviour the name promises.
- **`O(n²)` is the one that visibly explodes** — from single-digit
  milliseconds up to 146ms, and look specifically at the last two
  rows: `n` doubles from 40,000 to 80,000, and the time roughly
  **doubles again on top of that** (57ms → 146ms, closer to 3x, and
  would trend towards a clean 4x with less JIT/GC noise at these
  sizes) — exactly the "double the data, four times the time" rule
  from the table above, now showing up as a real, measured number
  instead of a theoretical claim.

The `sink` field is a small but important detail worth mentioning if
anyone asks about it: modern JVMs are aggressive about deleting loops
whose results are never used, so without accumulating into a field
that gets printed at the end, the compiler would happily optimise the
whole loop away and you'd see 0ms everywhere for every column — a
nice small lesson in why benchmarking code needs care, not just a
`System.nanoTime()` wrapped around it.

### Sorting algorithms: how the simple ones work

All three of the following are `O(n²)` — easy to understand, but slow
on large lists. We'll trace each one sorting `[5, 1, 4, 2]`.

**Bubble sort** — repeatedly swap neighbouring items that are out of
order; the largest unsorted value "bubbles" to the end on each pass.

```
[5, 1, 4, 2]   compare 5 & 1 → swap (5 > 1)
[1, 5, 4, 2]   compare 5 & 4 → swap
[1, 4, 5, 2]   compare 5 & 2 → swap
[1, 4, 2, 5]   5 has bubbled to the end ✓
```
Then repeat the pass on the remaining unsorted items until a full pass
makes no swaps — that's the signal the list is sorted.

**Selection sort** — scan the rest of the list for the smallest item
and place it next; repeat for each position.

```
[5, 1, 4, 2]   scan for the smallest value: 1
[1, 5, 4, 2]   place 1 at the front; next smallest is 2
[1, 2, 4, 5]   place 2 next; the remaining values are already in order
[1, 2, 4, 5]   sorted ✓
```

**Insertion sort** — take each item and slot it into its correct place
among the items already sorted (like ordering a hand of cards).

```
[5, 1, 4, 2]   "5" is the sorted start; take 1 and insert it on the left
[1, 5, 4, 2]   take 4 and slide it between 1 and 5
[1, 4, 5, 2]   take 2 and slide it between 1 and 4
[1, 2, 4, 5]   sorted ✓
```

### Faster sorts (for context — covered from the Java side in Part 2)

| Algorithm | Average | Worst case | Notes |
|---|---|---|---|
| Bubble | `O(n²)` | `O(n²)` | Simple but slow |
| Insertion | `O(n²)` | `O(n²)` | Fast on nearly-sorted data |
| Merge | `O(n log n)` | `O(n log n)` | Stable; uses extra memory |
| Quick | `O(n log n)` | `O(n²)` | Fast in practice; sorts in place |
| Tim | `O(n log n)` | `O(n log n)` | Adaptive hybrid; **the default in Java** — a hybrid of Merge and Insertion sort, optimised for real-world (partly-sorted) data |

---

## 🔧 Hands-On Practice

Small, quick, verified snippets — type and run each one before moving
to the full lab.

**1. Trace bubble sort with printouts after every pass**

```java
import java.util.Arrays;

public class BubbleSortDemo {
    public static void main(String[] args) {
        int[] values = {5, 1, 4, 2};
        System.out.println("Before: " + Arrays.toString(values));

        for (int pass = 0; pass < values.length - 1; pass++) {
            boolean swapped = false;
            for (int i = 0; i < values.length - 1 - pass; i++) {
                if (values[i] > values[i + 1]) {
                    int temp = values[i];
                    values[i] = values[i + 1];
                    values[i + 1] = temp;
                    swapped = true;
                }
            }
            System.out.println("After pass " + (pass + 1) + ": " + Arrays.toString(values));
            if (!swapped) break;
        }
        System.out.println("After: " + Arrays.toString(values));
    }
}
```

```
# Output:
Before: [5, 1, 4, 2]
After pass 1: [1, 4, 2, 5]
After pass 2: [1, 2, 4, 5]
After pass 3: [1, 2, 4, 5]
After: [1, 2, 4, 5]
```

Notice pass 3 makes no swaps — that's `swapped == false`, so a smarter
bubble sort would stop early there instead of grinding through a
pass it doesn't need.

**2. The `swapped` flag matters — try removing it**

Delete the `if (!swapped) break;` line and re-run. The output is
identical, but the algorithm now always runs the full `n - 1` passes
regardless of whether the list is already sorted. This is the
difference between bubble sort's **best case** (`O(n)`, already sorted,
with the early-exit flag) and its **worst case** (`O(n²)`, without it).

---

## 🧪 Lab: Implement Selection Sort and Insertion Sort

Using the bubble sort demo above as a model, write your own
`SelectionSortDemo.java` and `InsertionSortDemo.java`, each sorting
`{5, 1, 4, 2}` and printing the array state after each meaningful step
(after each item is placed / inserted), matching the traces above.

**Guided steps:**

1. Start from the `BubbleSortDemo` structure — same `Arrays.toString`
   printouts, same starting array.
2. For selection sort: outer loop picks the position to fill; inner
   loop finds the index of the smallest remaining value; swap it into
   place; print after each position is filled.
3. For insertion sort: outer loop starts at index `1` (index `0` is
   trivially "sorted" on its own); use a `while` loop to shift larger
   values one place to the right until you find the correct slot for
   the current value; print after each insertion.
4. Run both and confirm your output matches the traces in the Concept
   section above.

**Expected output (selection sort):**
```
Before: [5, 1, 4, 2]
After placing position 0: [1, 5, 4, 2]
After placing position 1: [1, 2, 4, 5]
After placing position 2: [1, 2, 4, 5]
After: [1, 2, 4, 5]
```

**Expected output (insertion sort):**
```
Before: [5, 1, 4, 2]
After inserting 1: [1, 5, 4, 2]
After inserting 4: [1, 4, 5, 2]
After inserting 2: [1, 2, 4, 5]
After: [1, 2, 4, 5]
```

---

## 🚀 Challenge Task

Extend **all three** of your sorts (bubble, selection, insertion) to
**count comparisons** instead of just sorting — increment a counter
every time two values are compared, and print the total at the end.

Then:

1. Generate a random array of 1,000 integers (use a fixed `Random`
   seed so your results are reproducible between runs).
2. Run all three sorts on **identical copies** of that array (use
   `.clone()` so sorting one doesn't affect the others).
3. Print the comparison count for each algorithm side by side.

**Think about before you run it:** which algorithm do you expect to
make the fewest comparisons on random data, and why? Does the result
match what the `O(n²)` worst-case table predicted, or does one
algorithm's real-world behaviour surprise you?

No solution is provided here — this is designed as an unguided
stretch exercise. If your numbers all land somewhere close to
`n² / 2` for bubble and selection sort, and noticeably lower for
insertion sort, you're on the right track.
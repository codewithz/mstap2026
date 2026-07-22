/*
 * CHALLENGE — Array Problem Set
 *
 * 3 classic array problems. No TODOs holding your hand, no hints inside
 * main() - just the data and the requirement. Work out your own
 * approach for each one before checking it against the expected output
 * at the bottom of each section.
 *
 * Uses only what you already know: declare/construct/initialize, .length
 * (a field, not a method - don't forget), for/while loops, if/else.
 */
public class ArrayChallenges {

    public static void main(String[] args) {

        // ============================================================
        // PROBLEM 1: Find the Missing Number
        // ============================================================
        // This array holds 99 of the 100 numbers from 1 to 100 - exactly
        // ONE number in that range is missing, and the array is NOT in
        // order. Find it.
        //
        // Requirement: print the missing number, on its own, clearly
        // labelled.
        //
        // ⚠️ Do NOT solve this by looping through 1..100 and checking
        // "is this number in the array?" for each one - that works, but
        // it's slow and misses the elegant trick this problem is
        // actually testing. Think about what you know is TRUE about the
        // numbers 1 to 100 as a group, that you could compare against
        // what's actually IN this array.

        int[] numbers = {74, 62, 92, 10, 34, 27, 2, 76, 16, 64, 81, 11, 53, 91, 52, 93, 50, 42, 68, 31,
                58, 75, 46, 33, 84, 70, 95, 9, 38, 80, 65, 48, 45, 43, 99, 51, 86, 13, 37, 24,
                40, 41, 19, 67, 60, 78, 8, 35, 82, 47, 3, 17, 39, 56, 69, 23, 61, 25, 6, 7,
                22, 49, 63, 100, 20, 72, 44, 87, 21, 1, 97, 59, 94, 54, 90, 26, 73, 85, 79, 66,
                30, 28, 89, 98, 5, 55, 77, 12, 71, 88, 14, 18, 29, 32, 36, 96, 4, 15, 83};

        // Your code here.


        // ============================================================
        // PROBLEM 2: Filter Even Numbers
        // ============================================================
        // Requirement: from the array below, build a NEW array that
        // contains only the even numbers, in the same order they
        // appeared. Print the new array's contents, and print how many
        // even numbers were found out of the total.
        //
        // ⚠️ You can't know the size of your "evens" array until you've
        // actually counted how many there are - which means you'll need
        // to look through the data more than once. That's fine, and
        // expected.

        int[] mixed = {12, 7, 33, 4, 19, 22, 5, 40, 1, 8, 15, 6};

        // Your code here.


        // ============================================================
        // PROBLEM 3: Reverse an Array In-Place
        // ============================================================
        // Requirement: reverse the order of the array below WITHOUT
        // constructing a second array to hold the result. When you're
        // done, toReverse itself should hold its own elements back to
        // front.
        //
        // Print the array before and after, so the reversal is visible.
        //
        // 🔁 Think about two positions moving toward each other from
        // opposite ends of the array at the same time, rather than one
        // position moving from start to finish.

        int[] toReverse = {10, 20, 30, 40, 50, 60, 70};

        // Your code here.

    }
}

/*
 * ============================================================
 * SELF-CHECK — exact expected output
 * ============================================================
 *
 * Problem 1:
 *   Missing number: 57
 *
 * Problem 2:
 *   Even numbers: 12, 4, 22, 40, 8, 6
 *   Even count: 6 out of 12
 *
 * Problem 3:
 *   Before reverse: 10, 20, 30, 40, 50, 60, 70
 *   After reverse:  70, 60, 50, 40, 30, 20, 10
 *
 * ============================================================
 * STRETCH GOALS (optional)
 * ============================================================
 * A. Problem 1 assumed exactly ONE number was missing. What would you
 *    need to change about your approach if TWO numbers could be
 *    missing instead of one? (You don't need to code this - just be
 *    able to explain why the sum trick alone stops being enough.)
 *
 * B. Problem 2 built a brand new array for the evens. Now do the
 *    opposite without a second array at all: loop through "mixed" and
 *    just PRINT each even number as you find it, with no array
 *    involved - notice how much simpler this is when you don't need to
 *    hand back a result, only report one.
 *
 * C. Problem 3 reversed the array in-place. Now find the LARGEST value
 *    left in "toReverse" after the reversal, using a single loop and
 *    without sorting anything. (The answer should be 70, wherever it
 *    now sits in the reversed array.)
 */
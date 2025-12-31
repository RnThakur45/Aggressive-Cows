# Aggressive-Cows-
Aggressive Cows - Binary Search

📝 Problem Statement

You are given an array arr[] representing positions of stalls on a line and an integer c representing the number of cows.
The task is to place all cows in stalls such that:

    Each stall can hold only one cow

    Cows are placed in different stalls

    The minimum distance between any two cows is maximized

Return the largest possible minimum distance.

💡 Approach: Binary Search on Answer

This problem is efficiently solved using Binary Search, because:

    The minimum possible distance is 1

    The maximum possible distance is max(arr) - min(arr)

We binary search on distance and check feasibility.

🔍 Feasibility Check

For a given distance m:

    Place the first cow in the first stall

    Place remaining cows in the next stall that is at least m units away

    If all cows can be placed, the distance is valid

⚙️ Algorithm Steps

Sort the stall positions

Set:

    low = 1

    high = max(arr) - min(arr)

Perform binary search:

    If cows can be placed with distance mid, try a larger distance

    Otherwise, reduce the distance

Return the maximum valid distance
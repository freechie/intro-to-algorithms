# 6.006 Spring 2020 — OA study plan

Course on disk: `study/6.006-spring-2020/` (Demaine, Ku, Solomon).
C++ work on disk: `cpp/DSA-Project/` (Abdul Bari course, already through arrays and strings).
Open a lecture from the local page. The player loads from YouTube, so you need a network connection. Notes and problem-set PDFs are already local.

Python is the daily assessment language. C++ is one structure per week in `cpp/DSA-Project/`, continuing the Udemy course from the next unfinished section. Coding the same problem in both languages every day doubles the time and stalls both.

If a posting says the assessment is in C++, switch that week's LeetCode solves to C++ and keep the lecture in Python.

If an online assessment is inside 7 days, skip new lectures and new C++ structures. Repeat Python problems from Weeks 1 and 3.

## C++ catch-up (about 45 minutes, once)

Sections already done, from `study/tasks/todo.md`: Udemy intro, recursion, arrays, strings, plus `Array<T>` in `cpp/DSA-Project/ds/array.h` (resize, iterators, search, duplicates). Leave diagonal, upper, and symmetric matrices parked. They are the in-progress Udemy section and they rarely show up on assessments.

1. Compile and run the existing demo. About 10 minutes.

```bash
cd /Users/what/Sites/intro-to-algorithms/cpp/DSA-Project
g++ -std=gnu++20 -Wall -Wextra main.cpp algo/strings.cpp -o advanced_array_demo
./advanced_array_demo
```

2. In `cpp/DSA-Project/ds/array.h`, find `Append`, `Insert`, and `BinarySearchLoop`. Read those three only. About 20 minutes.
3. Check the "C++ revival" box at the bottom. Next new C++ code is the singly linked list in Week 2.

## Each study day (about 4 hours)

1. Open the lecture page below and watch at 1.5×. Write four lines: pattern name, when it applies, time, space. About 50 minutes.
2. Code that structure once from memory in Python. About 40 minutes.
3. Solve 2 mediums from the NeetCode section for that day, in Python. First one untimed. Second one with a 30-minute cap. About 90 minutes.
4. If time is left, do the one course problem named for that day, in Python. Stop at 45 minutes and read the solution PDF. About 45 minutes.
5. Log one sentence in the progress list at the bottom: what you would try first next time. About 10 minutes.

The week's C++ block is separate. Do it on one day that has no interview, in place of step 4.

Interview day: one 20-minute Python easy in the morning. No new lecture.

## Week 1 — arrays, sorting, hashing (about 16 hours)

Lectures:

1. `study/6.006-spring-2020/resources/lecture-1-algorithms-and-computation/index.html`
2. `study/6.006-spring-2020/resources/lecture-2-data-structures-and-dynamic-arrays/index.html`
3. `study/6.006-spring-2020/resources/lecture-3-sets-and-sorting/index.html`
4. `study/6.006-spring-2020/resources/lecture-4-hashing/index.html`

NeetCode 150, in Python: Arrays & Hashing, Two Pointers, Sliding Window, Binary Search.
Two pointers, sliding window, and binary search are not separate lectures here. Drill them from NeetCode after Lecture 4.

C++ this week: the 45-minute revival only. `Array<T>` already covers this week's structures.

Course problem if time is left: Problem Set 2-4, MixBookTube.tv Chat.
Questions: `study/6.006-spring-2020/resources/mit6_006s20_ps2-questions/index.html`

## Week 2 — trees and heaps (about 16 hours)

Lectures:

1. `study/6.006-spring-2020/resources/lecture-6-binary-trees-part-1/index.html`
2. `study/6.006-spring-2020/resources/lecture-8-binary-heaps/index.html`
3. Skim only: `study/6.006-spring-2020/resources/lecture-7-binary-trees-part-2-avl/index.html` — know that AVL keeps the tree balanced. Stop before memorizing rotations.

NeetCode 150, in Python: Stack, Linked List, Binary Tree, Heap / Priority Queue, Binary Search Tree.
Stacks and linked lists are thin in this course. Drill them from NeetCode.

C++ this week (about 3 hours, one sitting): Abdul Bari singly linked list (`udemy-s7-1` in `study/tasks/todo.md`). Add `cpp/DSA-Project/ds/linked_list.h` with insert at head, insert at tail, delete, and reverse. That is the next unfinished Udemy section.

Course problem if time is left: Problem Set 4-1 (binary tree practice) and 4-2 (heap practice).
Questions: `study/6.006-spring-2020/resources/mit6_006s20_ps4-questions/index.html`

## Week 3 — graphs (about 16 hours)

Lectures:

1. `study/6.006-spring-2020/resources/lecture-9-breadth-first-search/index.html`
2. `study/6.006-spring-2020/resources/lecture-10-depth-first-search/index.html`
3. `study/6.006-spring-2020/resources/lecture-13-dijkstra/index.html`
4. Skim only: `study/6.006-spring-2020/resources/lecture-11-weighted-shortest-paths/index.html`

NeetCode 150, in Python: Graphs, then Union-Find and Backtracking.
Union-find and backtracking are not in this course. Drill them from NeetCode after Lecture 10.

C++ this week (about 3 hours, one sitting): stack and queue on the linked list from Week 2 (`udemy-s9-1`, `udemy-s10-1`). BFS needs a queue. Leave a C++ graph class for later.

Course problem if time is left: Problem Set 5-1, Graph Practice.
Questions: `study/6.006-spring-2020/resources/mit6_006s20_ps5_questions/index.html`

## Week 4 — dynamic programming (about 16 hours)

Lectures:

1. `study/6.006-spring-2020/resources/lecture-15-dynamic-programming-part-1-srtbot-fib-dags-bowling/index.html`
2. `study/6.006-spring-2020/resources/lecture-16-dynamic-programming-part-2-lcs-lis-coins/index.html`
3. If the week is clear: `study/6.006-spring-2020/resources/lecture-17-dynamic-programming-part-3-apsp-parens-piano/index.html`

Use the lecture’s SRTBOT steps on every DP problem: subproblems, relation, topological order, base cases, original problem, time.

NeetCode 150, in Python: 1-D DP, 2-D DP, Greedy.

C++ this week: re-solve one Python DP medium in C++, same recurrence. About 60 minutes. No new Udemy section.

Course problem if time is left: Problem Set 7-1, Effective Campaigning. Write the recurrence, then code it.
Questions: `study/6.006-spring-2020/resources/mit6_006s20_ps7_questions/index.html`

## After week 4

Two timed sets a week: 2 mediums in 45 minutes. Re-drill any pattern you cannot name in the first 5 minutes.

## Later

Save these until interviews are steady:

- Lecture 5, linear sorting
- Lecture 7 in full (AVL rotations)
- Lectures 12 and 14 (Bellman-Ford, Johnson / all-pairs)
- Lectures 18 and 19 (pseudopolynomial DP, complexity)
- Lectures 20 and 21 (review, next steps)
- Problem Sets 0, 1, 3, 6, and 8
- Quiz reviews under `study/6.006-spring-2020/resources/quiz-1-review/`, `quiz-2-review/`, `quiz-3-review/`
- Remaining matrix types in `cpp/MatricesCPP/` (diagonal, upper, symmetric)
- C++ merge sort and quick sort on `Array<T>`
- C++ hash table, BST, and graph classes (Udemy sections 11–14)

## Progress

Check an item when the lecture notes and the 2 LeetCode problems for that day are done.

- [ ] C++ revival: compile `cpp/DSA-Project` and reread `Append`, `Insert`, `BinarySearchLoop`
- [ ] L1 Algorithms and computation
- [ ] L2 Dynamic arrays
- [ ] L3 Sets and sorting
- [ ] L4 Hashing
- [ ] NeetCode: two pointers, sliding window, binary search
- [ ] L6 Binary trees
- [ ] L8 Binary heaps
- [ ] L7 AVL skim
- [ ] C++ singly linked list (`cpp/DSA-Project/ds/linked_list.h`)
- [ ] NeetCode: stack, linked list
- [ ] L9 BFS
- [ ] L10 DFS
- [ ] L13 Dijkstra
- [ ] C++ stack and queue on the linked list
- [ ] NeetCode: union-find, backtracking
- [ ] L15 DP part 1
- [ ] L16 DP part 2
- [ ] L17 DP part 3
- [ ] Timed set 1 (2 mediums / 45 min)
- [ ] Timed set 2 (2 mediums / 45 min)

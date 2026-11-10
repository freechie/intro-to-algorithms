# 6.006 Spring 2020 — OA study plan

The session is [`TODAY.md`](../TODAY.md). Do that one task and stop. Open a lecture from this file when a problem is stuck.

Course: [MIT 6.006 Spring 2020](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) (Demaine, Ku, Solomon).
C++ work on disk: `cpp/DSA-Project/` (Abdul Bari course, already through arrays and strings).
Lecture videos stay on OCW. Notes, recitations, problem sessions, quizzes, and problem sets are on disk at `study/6.006-spring-2020/` (gitignored), in resource-index week folders. Week 13 has no files. Lecture 21 and recitation 20 have no notes.

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
4. If time is left, do the one course problem named for that day, in Python. Stop at 45 minutes and read the solutions PDF in that week’s `problem-sets/` folder. About 45 minutes.
5. Log one sentence in the progress list at the bottom: what you would try first next time. About 10 minutes.

The week's C++ block is separate. Do it on one day that has no interview, in place of step 4.

Interview day: one 20-minute Python easy in the morning. No new lecture.

## Week 1 — arrays, sorting, hashing (about 16 hours)

Lectures. Video on OCW, notes on disk:

1. [Algorithms and computation](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/resources/lecture-1-algorithms-and-computation/). Notes: `study/6.006-spring-2020/week-01/lectures/lecture-1-introduction.pdf`
2. [Data structures and dynamic arrays](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/resources/lecture-2-data-structures-and-dynamic-arrays/). Notes: `study/6.006-spring-2020/week-01/lectures/lecture-2-data-structures.pdf`
3. [Sets and sorting](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/resources/lecture-3-sets-and-sorting/). Notes: `study/6.006-spring-2020/week-02/lectures/lecture-3-sorting.pdf`
4. [Hashing](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/resources/lecture-4-hashing/). Notes: `study/6.006-spring-2020/week-02/lectures/lecture-4-hashing.pdf`

Recitations 1–4, problem sessions 1–2, and problem sets 0–1 are in `study/6.006-spring-2020/week-01/` and `week-02/`.

NeetCode 150, in Python: Arrays & Hashing, Two Pointers, Sliding Window, Binary Search.
Two pointers, sliding window, and binary search are not separate lectures here. Drill them from NeetCode after Lecture 4.

C++ this week: the 45-minute revival only. `Array<T>` already covers this week's structures.

Course problem if time is left: Problem Set 2-4, MixBookTube.tv Chat.
Questions: `study/6.006-spring-2020/week-03/problem-sets/problem-set-2-questions.pdf`. Solutions: `study/6.006-spring-2020/week-03/problem-sets/problem-set-2-solutions.pdf`.

## Week 2 — trees and heaps (about 16 hours)

Lectures. Video on OCW, notes on disk:

1. [Binary trees, part 1](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/resources/lecture-6-binary-trees-part-1/). Notes: `study/6.006-spring-2020/week-04/lectures/lecture-6-binary-trees-part-1.pdf`
2. [Binary heaps](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/resources/lecture-8-binary-heaps/). Notes: `study/6.006-spring-2020/week-05/lectures/lecture-8-binary-heaps.pdf`
3. Skim only: [Binary trees, part 2 (AVL)](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/resources/lecture-7-binary-trees-part-2-avl/). Notes: `study/6.006-spring-2020/week-04/lectures/lecture-7-binary-trees-part-2-avl.pdf`. Know that AVL keeps the tree balanced. Stop before memorizing rotations.

NeetCode 150, in Python: Stack, Linked List, Binary Tree, Heap / Priority Queue, Binary Search Tree.
Stacks and linked lists are thin in this course. Drill them from NeetCode.

C++ this week (about 3 hours, one sitting): Abdul Bari singly linked list (`udemy-s7-1` in `study/tasks/todo.md`). Add `cpp/DSA-Project/ds/linked_list.h` with insert at head, insert at tail, delete, and reverse. That is the next unfinished Udemy section.

Course problem if time is left: Problem Set 4-1 (binary tree practice) and 4-2 (heap practice).
Questions: `study/6.006-spring-2020/week-05/problem-sets/problem-set-4-questions.pdf`. Solutions: `study/6.006-spring-2020/week-05/problem-sets/problem-set-4-solutions.pdf`.

## Week 3 — graphs (about 16 hours)

Lectures. Video on OCW, notes on disk:

1. [Breadth-first search](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/resources/lecture-9-breadth-first-search/). Notes: `study/6.006-spring-2020/week-05/lectures/lecture-9-breadth-first-search.pdf`
2. [Depth-first search](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/resources/lecture-10-depth-first-search/). Notes: `study/6.006-spring-2020/week-06/lectures/lecture-10-depth-first-search.pdf`
3. [Dijkstra](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/resources/lecture-13-dijkstra/). Notes: `study/6.006-spring-2020/week-08/lectures/lecture-13-dijkstra.pdf`
4. Skim only: [Weighted shortest paths](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/resources/lecture-11-weighted-shortest-paths/). Notes: `study/6.006-spring-2020/week-06/lectures/lecture-11-weighted-shortest-paths.pdf`

NeetCode 150, in Python: Graphs, then Union-Find and Backtracking.
Union-find and backtracking are not in this course. Drill them from NeetCode after Lecture 10.

C++ this week (about 3 hours, one sitting): stack and queue on the linked list from Week 2 (`udemy-s9-1`, `udemy-s10-1`). BFS needs a queue. Leave a C++ graph class for later.

Course problem if time is left: Problem Set 5-1, Graph Practice.
Questions: `study/6.006-spring-2020/week-07/problem-sets/problem-set-5-questions.pdf`. Solutions: `study/6.006-spring-2020/week-07/problem-sets/problem-set-5-solutions.pdf`.

## Week 4 — dynamic programming (about 16 hours)

Lectures. Video on OCW, notes on disk:

1. [Dynamic programming, part 1](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/resources/lecture-15-dynamic-programming-part-1-srtbot-fib-dags-bowling/). Notes: `study/6.006-spring-2020/week-09/lectures/lecture-15-dynamic-programming-part-1.pdf`
2. [Dynamic programming, part 2](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/resources/lecture-16-dynamic-programming-part-2-lcs-lis-coins/). Notes: `study/6.006-spring-2020/week-09/lectures/lecture-16-dynamic-programming-part-2.pdf`
3. If the week is clear: [Dynamic programming, part 3](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/resources/lecture-17-dynamic-programming-part-3-apsp-parens-piano/). Notes: `study/6.006-spring-2020/week-10/lectures/lecture-17-dynamic-programming-part-3.pdf`

Use the lecture’s SRTBOT steps on every DP problem: subproblems, relation, topological order, base cases, original problem, time.

NeetCode 150, in Python: 1-D DP, 2-D DP, Greedy.

C++ this week: re-solve one Python DP medium in C++, same recurrence. About 60 minutes. No new Udemy section.

Course problem if time is left: Problem Set 7-1, Effective Campaigning. Write the recurrence, then code it.
Questions: `study/6.006-spring-2020/week-10/problem-sets/problem-set-7-questions.pdf`. Solutions: `study/6.006-spring-2020/week-10/problem-sets/problem-set-7-solutions.pdf`.

## After week 4

Two timed sets a week: 2 mediums in 45 minutes. Re-drill any pattern you cannot name in the first 5 minutes.

## Later

Save these until interviews are steady:

- Lecture 5, linear sorting: `study/6.006-spring-2020/week-03/lectures/lecture-5-linear-sorting.pdf`
- Lecture 7 in full (AVL rotations): `study/6.006-spring-2020/week-04/lectures/lecture-7-binary-trees-part-2-avl.pdf`
- Lecture 12, Bellman-Ford: `study/6.006-spring-2020/week-07/lectures/lecture-12-bellman-ford.pdf`
- Lecture 14, Johnson / all-pairs: `study/6.006-spring-2020/week-08/lectures/lecture-14-apsp-johnson.pdf`
- Lecture 18, pseudopolynomial DP: `study/6.006-spring-2020/week-11/lectures/lecture-18-dynamic-programming-part-4.pdf`
- Lecture 19, complexity: `study/6.006-spring-2020/week-11/lectures/lecture-19-complexity.pdf`
- Lecture 20, review: `study/6.006-spring-2020/week-12/lectures/lecture-20-course-review.pdf`. Lecture 21 has no notes.
- Problem sets 0, 1, 3, 6, and 8, under `week-01`, `week-02`, `week-04`, `week-08`, and `week-11` `problem-sets/`
- Quiz reviews: `study/6.006-spring-2020/week-05/quizzes/quiz-1-review.pdf`, `study/6.006-spring-2020/week-08/quizzes/quiz-2-review.pdf`, `study/6.006-spring-2020/week-11/quizzes/quiz-3-review.pdf`
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

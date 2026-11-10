# Study plan for MIT 6.006, spring 2020

Open [TODAY.md](../TODAY.md), do that one task, and stop. When you get stuck, open a lecture from this file.

The course is [MIT 6.006, spring 2020](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/), taught by Demaine, Ku, and Solomon. The [syllabus](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/pages/syllabus/) names Introduction to Algorithms, third edition, by Cormen, Leiserson, Rivest, and Stein. That book is CLRS. Read the sections named with the lecture you watch. About 25 minutes. The lecture notes stay the session. Beyond Cracking the Coding Interview replaces Cracking the Coding Interview. Its reading order is in [STUDY.org](STUDY.org). C++ work is in [DSA-Project](../cpp/DSA-Project/). You are already through arrays and strings in Abdul Bari's course.

Lecture videos stay on OCW. Notes, recitations, problem sessions, quizzes, and problem sets are on disk under `study/6.006-spring-2020/`, in week folders. That folder is gitignored. Week 13 has no files. Lecture 21 and recitation 20 have no notes.

Use Python for the daily assessment. Add one C++ structure per week in [DSA-Project](../cpp/DSA-Project/), starting at the next unfinished Udemy section. Coding the same problem in both languages every day doubles the time and stalls both.

If a posting says the assessment is in C++, solve that week's LeetCode problems in C++ and keep the lecture in Python.

If an online assessment is inside 7 days, skip new lectures and new C++ structures. Repeat Python problems from weeks 1 and 3.

## C++ catch-up, about 45 minutes, once

These are already done, from the [task list](tasks/todo.md). Udemy intro, recursion, arrays, and strings are done. So is `Array<T>` in [array.h](../cpp/DSA-Project/ds/array.h), including resize, iterators, search, and duplicates. Diagonal, upper, and symmetric matrices can wait. They are the Udemy section in progress, and they rarely show up on assessments.

1. Compile and run the existing demo. About 10 minutes.

```bash
cd /Users/what/Sites/intro-to-algorithms/cpp/DSA-Project
g++ -std=gnu++20 -Wall -Wextra main.cpp algo/strings.cpp -o advanced_array_demo
./advanced_array_demo
```

The same steps are in the [DSA-Project readme](../cpp/DSA-Project/README.md).

2. In [array.h](../cpp/DSA-Project/ds/array.h), read [Append](../cpp/DSA-Project/ds/array.h#L49), [Insert](../cpp/DSA-Project/ds/array.h#L50), and [BinarySearchLoop](../cpp/DSA-Project/ds/array.h#L57). Read those three only. About 20 minutes.
3. Check C++ revival in the progress list at the bottom. The next new C++ code is the singly linked list in week 2.

## Each study day, about 4.5 hours

1. Open the lecture below and watch at 1.5x. About 50 minutes. Then read the CLRS sections named for that lecture. About 25 minutes. Write four lines. Name the pattern, when it applies, the time, and the space.
2. Code that structure once from memory in Python. About 40 minutes.
3. Solve 2 mediums from the NeetCode section for that day, in Python. Leave the first one untimed. Cap the second at 30 minutes. About 90 minutes.
4. If time is left, do the one course problem named for that day, in Python. Stop at 45 minutes and read the solutions PDF in that week's `problem-sets/` folder. About 45 minutes.
5. Log one sentence in the progress list at the bottom. Say what you would try first next time. About 10 minutes.

Do the week's C++ block on one day with no interview, in place of step 4.

On an interview day, do one 20-minute Python easy in the morning. Do not start a new lecture.

## Week 1, arrays, sorting, and hashing, about 16 hours

Watch the video on OCW. The notes are on disk.

1. [Algorithms and computation](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/resources/lecture-1-algorithms-and-computation/). Notes are in [lecture 1](6.006-spring-2020/week-01/lectures/lecture-1-introduction.pdf).
2. [Data structures and dynamic arrays](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/resources/lecture-2-data-structures-and-dynamic-arrays/). Notes are in [lecture 2](6.006-spring-2020/week-01/lectures/lecture-2-data-structures.pdf).
3. [Sets and sorting](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/resources/lecture-3-sets-and-sorting/). Notes are in [lecture 3](6.006-spring-2020/week-02/lectures/lecture-3-sorting.pdf).
4. [Hashing](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/resources/lecture-4-hashing/). Notes are in [lecture 4](6.006-spring-2020/week-02/lectures/lecture-4-hashing.pdf).

CLRS for these lectures. L1 is chapters 1 and 3. L2 is sections 10.1, 10.2, and 17.4. Section 17.4 is the resize analysis. L3 is chapters 2 and 7. L4 is chapter 11.

Recitations 1 to 4, problem sessions 1 and 2, and problem sets 0 and 1 are in [week 1](6.006-spring-2020/week-01/) and [week 2](6.006-spring-2020/week-02/).

NeetCode 150 for this week, in Python, is arrays and hashing, two pointers, sliding window, and binary search. Two pointers, sliding window, and binary search are not separate lectures here. Drill them from NeetCode after lecture 4.

C++ this week is the 45-minute revival only. `Array<T>` already covers this week's structures.

If time is left, do problem set 2-4, MixBookTube.tv Chat. Questions are in [problem set 2](6.006-spring-2020/week-03/problem-sets/problem-set-2-questions.pdf). Solutions are in [the solutions PDF](6.006-spring-2020/week-03/problem-sets/problem-set-2-solutions.pdf).

## Week 2, trees and heaps, about 16 hours

Watch the video on OCW. The notes are on disk.

1. [Binary trees, part 1](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/resources/lecture-6-binary-trees-part-1/). Notes are in [lecture 6](6.006-spring-2020/week-04/lectures/lecture-6-binary-trees-part-1.pdf).
2. [Binary heaps](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/resources/lecture-8-binary-heaps/). Notes are in [lecture 8](6.006-spring-2020/week-05/lectures/lecture-8-binary-heaps.pdf).
3. Skim only [binary trees, part 2, AVL](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/resources/lecture-7-binary-trees-part-2-avl/). Notes are in [lecture 7](6.006-spring-2020/week-04/lectures/lecture-7-binary-trees-part-2-avl.pdf). Know that AVL keeps the tree balanced. Stop before you memorize rotations.

CLRS for these lectures. L6 is chapter 12 and section 10.4. L8 is chapter 6. L7 has no AVL chapter. Chapter 13 is red-black trees. Skim the idea that balance keeps the height logarithmic, and stop before the rotations.

NeetCode 150 for this week, in Python, is stack, linked list, binary tree, heap or priority queue, and binary search tree. Stacks and linked lists are thin in this course. Drill them from NeetCode.

C++ this week takes about 3 hours in one sitting. Do the Abdul Bari singly linked list, `udemy-s7-1` on the [task list](tasks/todo.md). Add `cpp/DSA-Project/ds/linked_list.h` with insert at the head, insert at the tail, delete, and reverse. That is the next unfinished Udemy section.

If time is left, do problem set 4-1, binary tree practice, and 4-2, heap practice. Questions are in [problem set 4](6.006-spring-2020/week-05/problem-sets/problem-set-4-questions.pdf). Solutions are in [the solutions PDF](6.006-spring-2020/week-05/problem-sets/problem-set-4-solutions.pdf).

## Week 3, graphs, about 16 hours

Watch the video on OCW. The notes are on disk.

1. [Breadth-first search](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/resources/lecture-9-breadth-first-search/). Notes are in [lecture 9](6.006-spring-2020/week-05/lectures/lecture-9-breadth-first-search.pdf).
2. [Depth-first search](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/resources/lecture-10-depth-first-search/). Notes are in [lecture 10](6.006-spring-2020/week-06/lectures/lecture-10-depth-first-search.pdf).
3. [Dijkstra](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/resources/lecture-13-dijkstra/). Notes are in [lecture 13](6.006-spring-2020/week-08/lectures/lecture-13-dijkstra.pdf).
4. Skim only [weighted shortest paths](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/resources/lecture-11-weighted-shortest-paths/). Notes are in [lecture 11](6.006-spring-2020/week-06/lectures/lecture-11-weighted-shortest-paths.pdf).

CLRS for these lectures. L9 is sections 22.1 and 22.2. L10 is sections 22.3 and 22.4. The weighted-shortest-paths skim is the opening of chapter 24. L13 is section 24.3.

NeetCode 150 for this week, in Python, is graphs, then union-find and backtracking. Union-find and backtracking are not in this course. Drill them from NeetCode after lecture 10.

C++ this week takes about 3 hours in one sitting. Add a stack and a queue on the linked list from week 2, `udemy-s9-1` and `udemy-s10-1`. Read CLRS sections 10.1 and 10.2 with that code. Breadth-first search needs a queue. Leave a C++ graph class for later.

If time is left, do problem set 5-1, graph practice. Questions are in [problem set 5](6.006-spring-2020/week-07/problem-sets/problem-set-5-questions.pdf). Solutions are in [the solutions PDF](6.006-spring-2020/week-07/problem-sets/problem-set-5-solutions.pdf).

## Week 4, dynamic programming, about 16 hours

Watch the video on OCW. The notes are on disk.

1. [Dynamic programming, part 1](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/resources/lecture-15-dynamic-programming-part-1-srtbot-fib-dags-bowling/). Notes are in [lecture 15](6.006-spring-2020/week-09/lectures/lecture-15-dynamic-programming-part-1.pdf).
2. [Dynamic programming, part 2](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/resources/lecture-16-dynamic-programming-part-2-lcs-lis-coins/). Notes are in [lecture 16](6.006-spring-2020/week-09/lectures/lecture-16-dynamic-programming-part-2.pdf).
3. If the week is clear, watch [dynamic programming, part 3](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/resources/lecture-17-dynamic-programming-part-3-apsp-parens-piano/). Notes are in [lecture 17](6.006-spring-2020/week-10/lectures/lecture-17-dynamic-programming-part-3.pdf).

CLRS for these lectures. L15 is sections 15.1 and 15.3. L16 is section 15.4. L17 is section 15.2 and section 25.2.

On every dynamic programming problem, use the lecture's SRTBOT steps. Those steps are subproblems, relation, topological order, base cases, original problem, and time.

NeetCode 150 for this week, in Python, is 1D dynamic programming, 2D dynamic programming, and greedy.

For C++ this week, solve one Python dynamic programming medium again in C++, with the same recurrence. About 60 minutes. Do not start a new Udemy section.

If time is left, do problem set 7-1, Effective Campaigning. Write the recurrence, then code it. Questions are in [problem set 7](6.006-spring-2020/week-10/problem-sets/problem-set-7-questions.pdf). Solutions are in [the solutions PDF](6.006-spring-2020/week-10/problem-sets/problem-set-7-solutions.pdf).

## After week 4

Do two timed sets a week. Each set is 2 mediums in 45 minutes. Repeat any pattern you cannot name in the first 5 minutes.

## Later

Save these until interviews are steady.

- Lecture 5, linear sorting. CLRS chapter 8. Notes are in [lecture 5](6.006-spring-2020/week-03/lectures/lecture-5-linear-sorting.pdf).
- Lecture 7 in full, including AVL rotations. CLRS chapter 13 is the balanced-tree chapter. Notes are in [lecture 7](6.006-spring-2020/week-04/lectures/lecture-7-binary-trees-part-2-avl.pdf).
- Lecture 12, Bellman-Ford. CLRS section 24.1. Notes are in [lecture 12](6.006-spring-2020/week-07/lectures/lecture-12-bellman-ford.pdf).
- Lecture 14, Johnson and all-pairs. CLRS section 25.3. Notes are in [lecture 14](6.006-spring-2020/week-08/lectures/lecture-14-apsp-johnson.pdf).
- Lecture 18, pseudopolynomial dynamic programming. Stay with CLRS chapter 15. Notes are in [lecture 18](6.006-spring-2020/week-11/lectures/lecture-18-dynamic-programming-part-4.pdf).
- Lecture 19, complexity. CLRS chapter 34. Notes are in [lecture 19](6.006-spring-2020/week-11/lectures/lecture-19-complexity.pdf).
- Lecture 20, review. No new CLRS chapter. Notes are in [lecture 20](6.006-spring-2020/week-12/lectures/lecture-20-course-review.pdf). Lecture 21 has no notes.
- Problem sets 0, 1, 3, 6, and 8 are under `problem-sets/` in [week 1](6.006-spring-2020/week-01/), [week 2](6.006-spring-2020/week-02/), [week 4](6.006-spring-2020/week-04/), [week 8](6.006-spring-2020/week-08/), and [week 11](6.006-spring-2020/week-11/).
- Quiz reviews are [quiz 1](6.006-spring-2020/week-05/quizzes/quiz-1-review.pdf), [quiz 2](6.006-spring-2020/week-08/quizzes/quiz-2-review.pdf), and [quiz 3](6.006-spring-2020/week-11/quizzes/quiz-3-review.pdf).
- Diagonal, upper, and symmetric matrices in `cpp/MatricesCPP/` can wait.
- C++ merge sort and quick sort on `Array<T>` can wait.
- C++ hash table, BST, and graph classes can wait. Those are Udemy sections 11 to 14.

## Progress

Check an item when the lecture notes, the CLRS sections named for that lecture, and the 2 LeetCode problems for that day are done.

- [ ] C++ revival. Compile [DSA-Project](../cpp/DSA-Project/) and reread `Append`, `Insert`, and `BinarySearchLoop`.
- [ ] L1 Algorithms and computation
- [ ] L2 Dynamic arrays
- [ ] L3 Sets and sorting
- [ ] L4 Hashing
- [ ] NeetCode two pointers, sliding window, and binary search
- [ ] L6 Binary trees
- [ ] L8 Binary heaps
- [ ] L7 AVL skim
- [ ] C++ singly linked list in `cpp/DSA-Project/ds/linked_list.h`
- [ ] NeetCode stack and linked list
- [ ] L9 BFS
- [ ] L10 DFS
- [ ] L13 Dijkstra
- [ ] C++ stack and queue on the linked list
- [ ] NeetCode union-find and backtracking
- [ ] L15 dynamic programming, part 1
- [ ] L16 dynamic programming, part 2
- [ ] L17 dynamic programming, part 3
- [ ] Timed set 1, 2 mediums in 45 minutes
- [ ] Timed set 2, 2 mediums in 45 minutes

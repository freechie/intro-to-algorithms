# DSA-Project

C++ data structures and algorithms. The code you use now is `Array<T>` in [array.h](ds/array.h), plus the string functions in [strings.h](algo/strings.h).

`Array<T>` is a header-only template, which is how C++ templates are usually written. [main.cpp](main.cpp) is a small menu you can run for `Array<int>`. It also runs the string functions first.

## What Array can do

`Array<T>` can hold any type that you can copy and compare, including `int`, `double`, and `std::string`.

`begin` and `end` work with range-based `for` and with many standard algorithms.

```cpp
Array<std::string> arr;
arr.Append("Hello");
arr.Append("World");

for (const auto& value : arr) {
    std::cout << value << " ";
}
```

That loop prints `Hello World`.

The class follows the rule of five. The destructor frees the buffer. Copy construction and copy assignment copy the elements. Move construction and move assignment take the buffer from a temporary.

The array grows when it runs out of room. `std::out_of_range` and `std::logic_error` report a bad operation. Search and `Get` return `std::optional`, so a miss is not the number `-1`.

Operations:

- Core operations are `Append`, `Insert`, `Delete`, `Get`, and `Set`.
- Search is `LinearSearch`, which can move a hit to the front, and `BinarySearchLoop`.
- Summaries are `Max`, `Min`, `Sum`, `Avg`, and `isSorted`.
- Rearrangement is `Reverse`, `ReverseInPlace`, `InsertSort`, and `Rearrange`. `Reverse` allocates a new array. `Rearrange` partitions numbers.
- Set operations on sorted arrays are `Merge`, `Union`, `Intersection`, and `Difference`.
- Missing-element helpers cover one miss or many, in sorted and unsorted number arrays.
- Duplicate helpers cover sorted and unsorted arrays.

## String functions

The declarations are in [strings.h](algo/strings.h). The code is in [strings.cpp](algo/strings.cpp).

- `reverse_string` reverses a string in place.
- `is_palindrome` checks whether a string is a palindrome.
- `find_duplicates_hashing` finds duplicate characters with a hash map.
- `find_duplicates_bitwise` finds duplicate characters with bits.
- `are_anagrams_hash` checks an anagram with a hash map.
- `are_anagrams_bitwise` checks an anagram with bits.

## Compile and run

There is no Makefile yet. From this directory, compile `main.cpp` with a C++20 compiler. You do not compile `array.h`. The template implementation is already in that header.

```bash
g++ -std=gnu++20 -Wall -Wextra main.cpp algo/strings.cpp -o advanced_array_demo
./advanced_array_demo
```

The program prints the string demos, then opens a menu for `Array<int>`.

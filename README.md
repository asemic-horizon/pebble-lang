## PEBBLE: Parenthetical Expressions in a Browserlike Environment
(**Status: dormant. No progress expected in the near-term**)
Immediate goals:

* Parse a simple s-expression syntax (Python, Lark). Example:
 ```
 (fold + 1 2 (fold * 3 4))
```
* Convert simple folds to WebAssembly Text (wast) stack functions
* Creation of variables in wast (runtime) rather than Python ("compile-time")
* Make a test HTML/JS environment

Near-term goals:

* Define a very small list-oriented language
* Write a tree-walking compiler to WebAssembly Text


Long-term goals:

* Expand the language to the point where it's able to represent the original tree walking compiler.

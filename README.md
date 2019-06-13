## PEBBLE: Parenthetical Expressions in a Browserlike Environment

Immediate goals:

* Parse a simple s-expression syntax (Python, Lark). Example:
 ```
 (fold + 1 2 (fold * 3 4));comment
(another symbolic expression)
;(this expression won't run)
```

Near-term goals:

* Define a very small list-oriented language
* Write a tree-walking compiler to WebAssembly Text (stack format)


Long-term goals:

* Expand the language to the point where it's able to represent the original tree walking compiler.
"""Last
https://www.codewars.com/kata/last

Find the last element of a list.

Example:

```python
last([1,2,3,4]) # => 4
last("xyz") # => z
last(1,2,3,4) # => 4
```
```ruby
last( [1,2,3,4] ) # => 4
last( "xyz" ) # => z
last( 1,2,3,4 ) # => 4
```
```haskell
last [1,2,3,4] -- => 4
last ['x','y','z'] -- => z
```
```clojure
(last [1,2,3,4]) ; => 4
(last "xyz") ; => z
```
```javascript
last( [1,2,3,4] ) // => 4
last( "xyz" )     // => z
last( 1,2,3,4 )   // => 4
```
```java
last(Arrays.asList(1,2,3,4)); // => 4
last("xyz");                  // => z
last(1,2,3,4);                // => 4
last(new int[]{1,2,3,4});     // => 4
```
```coffeescript
last [1,2,3,4] # => 4
last "xyz"     # => z
last 1,2,3,4   # => 4
```
```rust
last(&[1,2,3,4]) // => 4
last(&['x','y','z']) // => z
```
In **javascript** and **CoffeeScript** a **list** will be an `array`, a `string` or the list of `arguments`.

(courtesy of [haskell.org](http://www.haskell.org/haskellwiki/99_questions/1_to_10))


"""


def last(*args):
    return args[-1] if not hasattr(args[-1], "__getitem__") else args[-1][-1]

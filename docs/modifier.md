Modifier
========
The modifier block adds attributes to existing signals as specified. If the `exclude` flag is set, the block instantiates new (generic) signals and passes them along with *only* the specified `fields`.

Both the key and value of an attribute can evaluate using the [nio expressions](https://docs.n.io/blocks/expressions.html?h=expressions). Several common Python libraries are imported for ease of access, such as `datetime`, `json`, `math`, `random`, `regex`, all of which are documented under the [Python Standard Library](https://docs.python.org/3/library/index.html).

Properties
----------
- **exclude**: If checked (true), the attributes of the incoming signal will be excluded from the outgoing signal. If unchecked (false), the attributes of the incoming signal will be included in the outgoing signal.
- **fields**: List of attribute names and corresponding values to add to the incoming signals.

Example
-------
This block configuration will add a random number to every signal:
```json
{
  "exclude": false,
  "fields": [
    {
      "title": "random_number",
      "formula": "{{ random.random() }}"
    }
  ]
}
```
Input signals:
```json
[
  {
    "foo": "bar"
  }
]
```
Output signals:
```json
[
  {
    "foo": "bar",
    "random_number": 0.123...
  }
]
```
By selecting `Exclude Existing Fields` the original contents of the incoming signals will be lost and outgoing signals will contain only the configured fields:
```json
{
  "exclude": true,
  "fields": [
    {
      "title": "area",
      "formula": "{{ math.pi * $radius**2 }}"
    }
  ]
}
```
```
Input signals:
```json
[
  {
    "radius": 2
  }
]
```
Output signals:
```json
[
  {
    "area": 12.566...
  }
]
```

Commands
--------
None


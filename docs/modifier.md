Modifier
========
The modifier block can add or modify fields to incoming signals as key-value pairs. Both the key and value of an attribute (field) can evaluate using [nio expressions](https://docs.n.io/blocks/expressions.html). Several standard Python libraries are imported for ease of access: [datetime](https://docs.python.org/3/library/datetime.html), [json](https://docs.python.org/3/library/json.html), [math](https://docs.python.org/3/library/math.html), [random](https://docs.python.org/3/library/random.html), and [re](https://docs.python.org/3/library/re.html). If the value of a field depends on some condition, consider using the [Conditional Modifier](https://blocks.n.io/ConditionalModifier).

Properties
----------
- **Fields**: List of attributes to add to the incoming signals.
  - *Title*: The key of this attribute.
  - *Formula*: The value of this attribute.
- **Exclude Existing Fields**: If checked (True) incoming signals will be discarded, and new signals created with only the fields specified. If False, the incoming signals will have the specified fields added to them, or updated if present.

Examples
-------
This block configuration will add a random number to every signal while preserving the original signal contents:
```
Exclude Existing Fields: False
Fields:
  Title: random_number
  Formula: {{ random.random() }}
```
<table width=100%>
<tr>
<th align="left">Incoming Signals</th>
<th align="left">Outgoing Signals</th>
</tr>
<tr>
<td>
<pre>
[
  {"foo": "bar"}
]
</pre>
</td>
<td>
<pre>
[
  {"foo": "bar", "random_number": 0.123...}
]
</pre>
</td>
</tr>
</table>

By selecting `Exclude Existing Fields` the incoming signals will be discarded and outgoing signals will contain only the configured fields:
```
Exclude Existing Fields: True
Fields:
  Title: area
  Formula: {{ math.pi * $radius ** 2 }}
```
<table width=100%>
<tr>
<th align="left">Incoming Signals</th>
<th align="left">Outgoing Signals</th>
</tr>
<tr>
<td>
<pre>
[
  {"radius": 2},
  {"radius": 3}
]
</pre>
</td>
<td>
<pre>
[
  {"area": 12.566...},
  {"area": 28.274...}
]
</pre>
</td>
</tr>
</table>

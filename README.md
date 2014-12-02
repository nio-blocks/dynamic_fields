DynamicFields
===========

A NIO block for enriching signals dynamically.

By default, the dynamic fields block adds attributes to existing signals as specified. If the *exclude* flag is set, the block instantiates new (generic) signals and passes them along with *only* the specified fields.

Properties
--------------

-   **fields**: List of attribute names and corresponding values to add to the incoming signals.
-   **exclude**: If True, output signals only contain the attributes specified by *fields*.


Dependencies
----------------
None

Commands
----------------
None

Input
-------
Any list of signals.

Output
---------
One signal for every incoming signal, modified according to *fields* and *exclude*.

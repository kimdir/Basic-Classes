Michael Stebbins' basic classes and hierarchy.

Class hierarchy is generally split into levels:

1. Managers: Objects that serve as the interface for aspects of a program.
Generally have a collection of direct report objects that perform the requested
functions and interface to the rest of the program (or the user) through their
respective manager.

2. Handlers: Objects specifically oriented around data management and handling,
specifically with applications related to external sources from the program.
Often used for reporting and IO operations.

3. Agents: Objects that perform specific collections of actions, generally
closely related. Do no interface with external data sources or programs.

This structure serves several purposes. Reducing the number of interactions (via
the utilization of Managers) with disparate components reduces the potential for
mistakes and confusion, and isolation of internal versus external interactions
allows for easier debugging and functional decomposition.

--Functional Decomposition--

Choosing a set of terms to explain the architecture in a commonly understood
way, the following terms will be used in further discussions.

1. Objective: The primary focus and overall function that a program fulfills.
Objectives are multi-part processes that utilize multiple Functions to complete
its process.

2. Function: A large framework component that makes up a portion of an
Objective. Functions can also contain Sub-Functions, usually denoted with an
additional versioning-style number (x.x or x.x.x for example). Functions capture
the larger aspects of a program's Objective and allow for more discretization of
the work that is needed to be completed. Functions can be composed of other
Functions or Tasks

3. Tasks: The singular steps required to fulfill a Function's requirements. This
can be an internal task (handled by Agents) or an external

A typical architecture would look something like this:

-Program Manager
--

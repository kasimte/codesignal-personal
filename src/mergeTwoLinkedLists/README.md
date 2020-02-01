# mergeTwoLinkedLists

I had trouble with this one at first.

The key parts of the algorithm for me were:

* creating a dummy node for the start
* creating a tracking node that traverses through the new list and moving it forward

Some recursive solutions on StackOverflow did not pass all the tests
on CodeSignal, as there was some sort of infinite loop created without
the start dummy node.

Also useful was searching for examples on GitHub (making sure to
select all of GitHub and "Code").

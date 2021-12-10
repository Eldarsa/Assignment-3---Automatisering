## Purpose

Only containing the data model for the node graph. Everything related to displaying it should indeed be handled in QT. Developing this seperately is however a great way of ensuring full detachment between the model and the view. 

Could this be implemented as a library we can just import into our app? That would be very nice indeed. 

### Why is this important? 

Just imagine if we want to develop a web app in the future for displaying the node graphs online. It would be extremely convenient if we can reuse this code without having to do any modifications at all, but just create a new front end. 

Following the principle of "not assuming how it is going to be used" the node graph will be fully accessible through a well defined interface. A developer working on the node graph and a developer working on the front end should be able to work completely seperately as long as they agree on the interface. That is at least the ideal I believe we should strive to achieve. 

## A beautiful point about weak pointers

In this library we have put a lot of effort into using proper pointer practice. This is very important as we want different entities (active nodes) within our graph network to be able to efficiently access variables, change and read values, without having to go through the graph hierarchy all the time. If the front-end application instead has the ability to **retrieve a weak or shared pointer to whatever node / variable / attribute it wants**, it is easier for the front end developer to efficiently organize and work with the values as most fit in a particular situation. Fetching weak pointers through the interface makes this **mostly safe**. I think the main rule of thumb should be casting to weak pointers from the shared pointers and only use shared if absolutely necessary.

Another great thing about weak pointers is that they are easy to check if are still valid or not, which will be *extremely* powerful in our case. Here's an example why:

Imagine you have ten nodes. A node Q has a variable X that all other nodes use in some way. Then you decide to delete node Q. How does every other node know that X is gone? Notifying subscribers could be an option, but let's say that turns out to not be benificial in some case. Then the subscriber can simply check if X is available using the .lock() function before performing any operation on it. If it is expired, it can simply remove it. 

# Technical questions:

### What is the best data structure for storing nodes and connections? 

We have to consider some important factors in order to determine this:

1. How often do we need to locate a node?
2. How often do we need to create or delete a node?
3. How often do we have to iterate through a set of nodes?

There may be even more factors that we discover will be relevant to consider, but these are the ones I was able to come up with on the spot. 

There is probably no "one size fits all" solution for this. It does however seem apparent that the most important consideration for us is accessing nodes (mainly because we want to extract data every time we select a node in the graph). I would think the fastest way to do this is to give every node an index and sort them based on this. In that case, using an algorithm like binary search or similar will find the node in no time. 

**Initial conclusion:** An id-based dictionary structure seems to be the best bet for now.  


## Sources for inspiration

- Python NodeGraphQt: https://github.com/jchanvfx/NodeGraphQt/tree/master/NodeGraphQt

- Paceholder C++: https://github.com/paceholder/nodeeditor 
    - This is nice and all, but I do find the node models way to coupled with the model. I see where they are coming from and how it can simplify their application for their purpose, but our approach has to be stricter to avoid long term complications.

- Hazel engine: https://github.com/TheCherno/Hazel
    - Great wway of observing good C++ practice
# Static and Dynamic engine - The motivation

As I am writing this it is 10.12.2021, friday and very late. I just need to clear out some thoughts on where the idea of dividing into a static and a dynamic engine comes from. The terms may be up for later debate, but I'll avoid dwelling on that too much as is a bad habit of mine. Instead I'll just clear out some thought surrounding the concepts. 

## Part 1 - The engine concept

The concept of an engine is that it is supposed to be what simulates the economy once the parameters have all been adjusted. This means it has to take in every node and every flow between the nodes in a graph and calculate how the system unfolds mathematically step by step. This is not really an easy task as we want to optimize for speed as much as possible. At the same time we have a lot of other concerns. For instance:

- We may want to look at how the system unfolds slowly on the screen, be able to affect it as it is unfolding and directly interact with the live system. 
- We may want to just set it up and perform millions of computations on it with different parameters in order to create confidence in which parameters yield the best outcome. 
- The may be other unforseen applications with completely different requirements that we have to design this computational engine for

The main point is that we should make engines that optimize the exact usage we want to apply our program to, and that may indeed vary. 

Another important strength of the engine is that it can be attached the moment the user decides to run the simulation. Depending on which type of simulation is chosen to run, the engine can be decided in the last moment. 

## Part 2 - The difference between static and dynamic engine

The two first engine concepts born out of the concerns above are the static and dynamic engines.

- The static one is what I imagine would be designed for computing just tons of iterations of a system and stress testing it with millions upon millions of samples.
- The dynamic one is what I imagine would be shown on a demonstration where you want to visually display how the system evolves over time. 

I think it is beneficial to develop both of these at the same time as some key ideas may occur along the way as I am developing, and I may simultaneously realize it belongs to the other engine and not the one I am currently working on. 

### So what do we need for the dynamic one?

The dynamic one has to be able to calculate each iteration effectively and return the result immediately such that it can be displayed on screen. There are a ton of concerns to consider when designing a system like that. A few of them are

1. **We may not want to flush the values to screen for *every* iteration**: How often do we want to "flush" the values to screen and how many iterations do we want to calculate per second? This should probably be customizable based on what system the user has set up and how fast the user wants to play the simulation. 

2. **We have to ensure that the system remains responsive by threading the back end execution seperately from the front end somehow**

3. **We have to ensure that things that happen on a periodic basis happens within realistic periods**: Say we simulate a person paying monthly bills. These bills are not always paid on the same day but spread across different days of the month. How do we simulate this realistically? Do we predetermine when transactions take place or do we randomize it? 

### And what about the static one?

This one has to be a power horse in the sense that it must take very smart evaluations on how to set up the equations. It has to have systems for dealing with condition checking and quickly switching between different equations to solve based on if the conditions are met. This immediately sounds a lot like a state machine system to me with some global variables to check, but I have not explored the thought that much. 

Some considerations for such a system are:

1. **How do we quickly set up the necessary equations?**
2. **How do we quickly switch between the necessary equations?**


## Initializing the engines

One observation that seems very nice is that both the engines can be initialized right before performing the calculations. This means we have a lot of freedom in how we want to set up our system as the user is not interfering with anything while the process is happening. This is in a sense a luxury. 
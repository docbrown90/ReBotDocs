C# Lambdas & How ReBot Uses Them
================================

A rotation is just a collection of conditions and the spells to cast when those conditions are met.  There are a few different
ways to cast and return, we'll cover two basic ones here.

The simplest way is to use an if statement, like so.  Everyone understands how this works and its very easy to read, however,
it takes up quite a few lines and could lead to very large rotation files.

.. sourcecode:: c#

    if(conditions)
    {
        Cast("Spell Name");
        return;
    }
    
The shortest way is to use an expression lambda.  Expression lambdas are a C# language sugar that allow you to write an
evaulation, inline, with very little extra code.  Expression lambdas might look a little confusing, but they're really quite
simple.  The default rotations use lambdas heavily, so we'll go over those here.

The ReBot cast methods support inline conditions in the form of expression lambdas.  Everything after the `=>` is evaluated and
must be true or false.  This is a very simple way to do evaulation for a spell without the need to wrap it inside an if block or
its own function.

.. sourcecode:: c#

    if(Cast("Spell Name", () => conditions)) return;
    
.. note::
  
  This guide will use expression lambdas whenever possible.

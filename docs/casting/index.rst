Casting Spells
==============

Well, it is how the game works afterall.  ReBot provides many ways to cast a spell, covering pretty much all possible
requirements.

Casting Basics
--------------

.. warning::
    
    All cast methods require the spell name to be in English, it will be converted to the proper localized version by ReBot.

Each cast method will return true or false depending on if the spell can be casted.  If the spell can be casted and it triggers
the GCD, you should return directly after.  This lets the bot know it should wait for the GCD to cast the next spell.

There are a few different ways to cast and return, we'll cover two basic ones here.

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

.. sourcecode:: c#

    if(Cast("Spell Name", () => conditions)) return;

Everything after the `=>` is evaluated and must be true or false.  This is a very simple way to do evaulation for a spell
without the need to wrap it inside an if block or its own function.

.. note::
 
    I'll be using the lamda format for all examples.  You should use it too.


.. toctree::
    :maxdepth: 3

    cast


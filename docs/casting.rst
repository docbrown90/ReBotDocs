Casting
=======

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

Everything after the `=>` is evaluated and must be true or false.  This is a very simple way to do evaulation for a spell
without the need to wrap it inside an if block or its own function.

.. sourcecode:: c#

    if(Cast("Spell Name", () => conditions)) return;
    
**I'll be using Lambdas for examples here on out.**


.. _cast:

Cast
----
.. function:: Cast(name[, onlyCastWhen])
              Cast(name, onlyCastWhen, target)
              Cast(name, target[, onlyCastWhen])

The absolute simplest way to cast a spell is to call the `Cast` method with your spell name as the only argument.  This will cast the spell on cooldown.

.. sourcecode:: c#

    Cast("Spell Name")

With inline conditions.

.. sourcecode:: c#

    Cast("Spell Name", () => HasAura("Some Buff"))


.. _cast-prevent-double:

CastPreventDouble
-----------------
.. function:: CastPreventDouble(name[, onlyCastWhen, preventTime])
              CastPreventDouble(name, onlyCastWhen, target[, preventTime])

This function will cast a spell and prevent it from being cast again for 300ms by default or however long you set.
For example, cast a spell and don't cast it again for 1 second.

.. sourcecode:: c#

    CastPreventDouble("Spell Name", () => conditions, 1000)
    
CastSelf
--------
.. function:: CastSelf(name[, onlyCastWhen])

Exactly the same as :ref:`cast` except the unit is always the player.


CastSelfPreventDouble
---------------------
.. function:: CastSelfPreventDouble(name[, onlyCastWhen, preventTime])
    
----
    
Exactly the same as :ref:`cast-prevent-double` except the unit is always the player.


CastOnTerrain
-------------
.. function::  CastOnTerrain(name, position[, onlyCastWhen])

Cast a spell on the terrain in the game world. See Unit Vectors for more information on this.  The below example would cast a spell directly under the player.

.. sourcecode:: c#

    CastOnTerrain("Spell Name", Me.Position, () => conditions)

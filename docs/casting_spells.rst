Casting Spells
==============

Well, it is how the game works afterall.  ReBot provides many ways to cast a spell, covering pretty much all possible
requirements.

Casting Basics
--------------

**All cast methods require the spell name to be in _English_, it will be converted to the proper localized version by ReBot.**

Each cast method will return true or false depending on if the spell can be casted.  If the spell can be casted and it triggers
the GCD, you should return directly after.  This lets the bot know it should wait for the GCD to cast the next spell.

There are a few different ways to cast and return, we'll cover two basic ones here.

The simplest way is to use an if statement, like so.  Everyone understands how this works and its very easy to read, however,
it takes up quite a few lines and could lead to very large rotation files.

.. sourcecode:: c#

    if(conditions)
    {
        Cast('Spell Name');
        return;
    }
    
The shortest way is to use an expression lambda.  Expression lambdas are a C# language sugar that allow you to write an
evaulation, inline, with very little extra code.  Expression lambdas might look a little confusing, but they're really quite
simple.  The default rotations use lambdas heavily, so we'll go over those here.

Everything after the `=>` is evaluated and must be true or false.  This is a very simple way to do evaulation for a spell
without the need to wrap it inside an if block or its own function.

.. sourcecode:: c#

    if(Cast('Spell Name', () => conditions)) return;



Cast
----

**Definitions**

.. sourcecode:: c#

    Cast(string, [System.Func<bool>])
    Cast(string, System.Func<bool>, ReBot.API.UnitObject)
    Cast(string, ReBot.API.UnitObject, [System.Func<bool>])
    
----------
    
The absolute simplest way to cast a spell, call Cast with your spell name as the only argument.

.. sourcecode:: c#

    Cast('Spell Name')
    
C# supports something called Expression Lamdas.  This is a language sugar that allows you to wrote
a function inline, with very little extra code.  The default rotations use lambdas heavily, so we'll go over those here.

Everything after the => is evaluated and must be true or false.  This is a very simple way to do evaulation for a spell without
the need to wrap it inside an if block.

An Expression Lambda looks like this.

.. sourcecode:: c#

    () => 1 + 1 == 2
    
An Expression Lamda used inside the Cast method, looks like this.

.. sourcecode:: c#

    Cast('Spell Name', () => HasAura('Some Buff') )
    
Without Expression Lamdas, the same code would need to look like this. As you can see, its much cleaner and takes less code.

.. sourcecode:: c#

    if(HasAura('Some Buff'))
    {
        Cast('Spell Name')
    }
    

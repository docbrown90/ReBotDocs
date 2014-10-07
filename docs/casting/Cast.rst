.. _func-cast

Cast
====

.. sourcecode:: c#
  
    Cast(name[, onlyCastWhen])
    Cast(name, onlyCastWhen, target)
    Cast(name, target[, onlyCastWhen])

The absolute simplest way to cast a spell is to call the `Cast` method with your spell name as the only argument.  This will cast the spell on cooldown.

.. sourcecode:: c#

    Cast("Spell Name")

With inline conditions.

.. sourcecode:: c#

    Cast("Spell Name", () => HasAura("Some Buff"))

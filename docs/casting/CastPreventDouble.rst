.. _func-cast-prevent-double:

CastPreventDouble
=================

.. sourcecode:: c#

    CastPreventDouble(name[, onlyCastWhen, preventTime])
    CastPreventDouble(name, onlyCastWhen, target[, preventTime])

This function will cast a spell and prevent it from being cast again for 300ms by default or however long you set.
For example, cast a spell and don't cast it again for 1 second.

.. sourcecode:: c#

    CastPreventDouble("Spell Name", () => conditions, 1000)

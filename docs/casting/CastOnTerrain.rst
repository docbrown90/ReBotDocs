.. _func-CastOnTerrain:

CastOnTerrain
=============

.. sourcecode:: c#

    CastOnTerrain(name, position[, onlyCastWhen])

Cast a spell on the terrain in the game world. See Unit Vectors for more information on this.  The below example would cast a spell directly under the player.

.. sourcecode:: c#

    CastOnTerrain("Spell Name", Me.Position, () => conditions)

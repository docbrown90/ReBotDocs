Combat Rotation Class
=====================
Rotations work by overloading the default empty methods.  Each combat rotation inherits the base class `CombatRotation`.

The Constructor
---------------
The constructor is where you can setup veriables and other settings for the rotation.  This is also where you setup
things like Pull Spells and Group Buffs.

All of these veriables are place inside the constructor.

.. sourcecode:: c#
    
    public class CustomRotation : CombatRotation
    {
        // Initialization happens here.
    }


Pull Spells
^^^^^^^^^^^
Spells the bot will use to initate combat.

.. sourcecode:: c#

    PullSpells = new string[]
    {
        "Pull Spell One",
        "Pull Spell Two",
    }
    
Group Buffs
^^^^^^^^^^^
The bot will try and keep these buffs on all party members.  During a BG for example, the bot will wait for everyone
to join then cast these spells.

.. sourcecode:: c#

    GroupBuffs = new string[]
    {
	    "Group Buff One",
	    "Group Buff Two",
    };
    
Dismount Spell
^^^^^^^^^^^^^^
This is the spell the bot will use to dismount as it moves in for combat.

.. sourcecode:: c#

    DismountSpell = "Dismount Spell Name";

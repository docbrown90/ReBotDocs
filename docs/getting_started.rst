Getting Started
==============

Example rotation that contains In, Out and After combat scenarios.


Base Combat Rotation
--------------------

This is the base for a combat rotation, I'll go over each part below.

.. sourcecode:: c#

    using System;
    using System.Linq;
    using ReBot.API;
    
    namespace ReBot
    {
        [Rotation("Custom Rotation", "docbrown", WoWClass.Class, Specialization.ClassSpec)]
        public class CustomRotation : CombatRotation
        {
            public CustomRotation()
            {
                
            }
            public override bool OutOfCombat()
            {
                return false;
            }
            public override void Combat()
            {
		    
            }
        }
    }
    
    
Sections Explained
------------------

This will import some core System APIs and the ReBot API.  To have Visual Studio give you intellisense feedback,
you will need to create a reference to the ReBot.exe in your project, you can also download the ReBVot Combat
Profile template from the `ReBot forums here`_.

.. sourcecode:: c#

    using System;
    using System.Linq;
    using ReBot.API;
    
This allows direct access to the ReBot API without the need to prefix all API calls with ReBot.
    
.. sourcecode:: c#

    namespace ReBot
    {


This defines the rotations name, author, class, spec, combat distance and dismount distance.
The Rotation function has two overrides, one includes a description while one does not.
The last two arguments showed in these examples refer to Combat Range and Dismount Range respectively.

.. sourcecode:: c#

    [Rotation("Custom Rotation", "docbrown", WoWClass.Class, Specialization.ClassSpec), 5, 25]
    [Rotation("Custom Rotation", "docbrown", "Rotation Description", WoWClass.Class, Specialization.ClassSpec), 5, 25]
    
This creates the class for your rotation and inherits the ReBot.CombatRotation class.
This class name *must* be unique and will cause ReBot to crash if it is not.
    
.. sourcecode:: c#

    public class CustomRotation : CombatRotation
    {


This is the class constructor and will be called once, this *must* have the same name as the class.
This is where you can setup buffs and other constant values that you might need.
    
.. sourcecode:: c#

    public CustomRotation()
    {
            
    }


This is the out of combat rotation, this will run only while out of combat. It's `bool` so you must
return a bool value, I'm not sure what that means, the default implentation returns false, so thats what we'll do here.
    
    
.. sourcecode:: c#

    public override bool OutOfCombat()
    {
        return false;
    }

This is where your main combat rotation is defined.  It's a `void` so must must return nothing.  A return assumes
you've done something that has triggerd a GCD and it will wait for the next combat pulse to run again, if you do
not return, the bot will continue and attempt to cast the next spell defined (which is fine as long as the spell
doesn't trigger the GCD).	
	
.. sourcecode:: c#

    public override void Combat()
    {
        
    }


Finishing Up
------------

Thats all for the base rotation, continue to the next steps to learn how to cast spells.

.. ReBot forums here: http://www.rebot.to/showthread.php?t=847

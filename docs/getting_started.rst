Getting Started
==============

Example rotation that contains In, Out and After combat scenarios.

.. sourcecode:: csharp
  using System;
  using System.Linq;
  using ReBot.API;
  
  namespace ReBot
  {
      [Rotation("Custom Rotation Name", "Rotation Author", "Rotation Description", WoWClass.Warrior, Specialization.WarriorArms, 5, 25)]
      public class Feral : CombatRotation
      {
          public Feral()
          {
  
          }
  
          public override bool OutOfCombat()
          {
              return false;
          }
  
          public override void Combat()
          {
  
          }
  
          public override bool AfterCombat()
          {
              return false;
          }
  
      }
  }

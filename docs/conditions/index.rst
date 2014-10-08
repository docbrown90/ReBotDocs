Conditions
==========

Conditions are the core of any rotation, they decided if you should cast a spell or not.  Even the simplest rotations require
conditions.

    public int AuraStackCount(string auraName)
    public double AuraTimeRemaining(string auraName)
    public bool HasAura(string auraName, bool checkOnlySelf, int minStackCount)
    public bool HasAura(string auraName, bool checkOnlySelf)
    public bool HasAura(int id)
    public bool HasAura(string auraName)
    public bool HasGlobalCooldown()
    public bool HasSpell(string spellName)
    public bool IsInShapeshiftForm(string spellName)
    public double SpellCooldown(string spellName)
    public int SpellCost(string spellName)
    public double SpellMaxRangeSq(string spellName)
    public double SpellMinRangeSq(string spellName)

.. toctree::
    :maxdepth:
    
    

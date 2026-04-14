from alchemy.grimoire.dark_spellbook import dark_spell_record
print("=== Kaboom 1 ===")
print("Access to alchemy/grimoire/dark_spellbook.py directly")
print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
try:
    dark_spell_record("none", "NONE")
except ImportError as e:
    print(e)
print()

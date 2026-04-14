def validate_ingredients(ingredients: str) -> str:
    from .dark_spellbook import dark_spell_allowed_ingredients
    allowed: list = dark_spell_allowed_ingredients()
    test = [i.lower().strip() for i in ingredients.split(",")]
    done = False
    for i in test:
        if i in allowed:
            done = True
            break
    if done:
        return f"{ingredients} - VALID"
    else:
        return f"{ingredients} - INVALID"

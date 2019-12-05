# Genius-Plaza-Django-Test
Python Django Restful assessment for genius plaza

## /recipes/<int:user_id>
### POST
    {
        "id": 1,
        "name": "Meatballs",
        "user": 1,
        "ingredients": [{"text": "Bread Crumbs"},{"text":"Ground Beef"}],
        "steps": [{"step_text":"Mix in Bowl"},{"step_text":"Cook"}]
    }
### PUT
    {
        "id": 1,
        "name": "Norwegian Meatballs",
        "user": 1,
        "ingredients": [{"text": "Bread Crumbs"},{"text":"Ground Beef"},{"text": "Milk"},{"text":"Paprika"}],
        "steps": [{"step_text":"Mix all ingredients in Bowl"},{"step_text":"Heat Pan"}, {"step_text": "Cook Meatballs"}]
    }
### GET
will return users recipe
### DELETE
will delete users recipe

## /recipes
### GET
will return all recipes

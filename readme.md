# Seasons App

This is a basic app to demonstrate using Jinja2 syntax with Flask.

## Running

- Set up a Python virtual environment
  - `python -m venv venv`
  - `venv\scripts\activate`
- Install project dependencies
  - `pip install flask python-dotenv`
- Create your `.env` file
- Run the app with `flask run`

## Developing Your Own Version

To develop your own version of this project, you can `clone` or `fork` this repo.

- `git clone <repo url>` makes a copy of the repo, but still considers the upstream (parent) repo to be this repo. This is fine for development and testing, but the remote repo still belongs to me.
- Forking the repo makes a copy of the repo on _your_ GitHub account, meaning that you have full control of it from that point forward. This is the better approach when you want to make your own version of an existing project, as opposed to contributing to the existing one.

## Branches

There are a few branches of the project that represent different stages of development, which you may find helpful:

- `main` is the most current and up to date branch at the final stage of development, including all features present in other branches.
- `BaseAppNoInheritance` is the basic Seasons app, just a page displaying the current season, with no template inheritance, additional pages, Bootstrap, headers, or extra features.
  - This is the starting point to practice adding those extra features from.
- `TemplateInheritance` refactors the app to use template inheritance for the `index.html` page.
  - This is the starting point for adding your own custom page.
- `addCardPage` is my personal development branch where I add some new features and try things out.

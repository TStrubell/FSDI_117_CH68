# FSDI-117 – Assignment 1  
## The models for the Projects section of my portfolio  
Author: Tim Strubell  

## Overview
This assignment implements the data layer for a simple portfolio using Django.  
It focuses on two core entities:

- `Skill` – represents technical or professional skills.
- `Project` – represents portfolio projects that use one or more skills.

The models are registered in the Django admin, populated via the admin interface,  
and displayed in the browser using function-based views and templates.

---

## Project Structure

fsdi117_ch68_cl1_asgmt1_strubell/
- `manage.py`
- `config/`
  - `__init__.py`
  - `settings.py`
  - `urls.py`
  - `wsgi.py`
  - `asgi.py`
- `portfolio/`
  - `__init__.py`
  - `admin.py`
  - `apps.py`
  - `models.py`
  - `views.py`
  - `urls.py`
  - `migrations/`
    - `__init__.py`
  - `templates/portfolio/`
    - `projects.html`
    - `skills.html`
- `static/css/`
  - `styles.css`

---

## Models

### `Skill`
- `name` (`CharField`, max_length=100)  
- `proficiency` (`IntegerField`, 0–100, validated with `MinValueValidator` and `MaxValueValidator`)  

Includes:
- `Meta.ordering = ['name']`
- `verbose_name = "Skill"`
- `verbose_name_plural = "Skills"`
- `__str__` returns `"Skill: <name>"`

### `Project`
- `title` (`CharField`, max_length=200)  
- `description` (`TextField`)  
- `link` (`URLField`, optional)  
- `skills` (`ManyToManyField` to `Skill`)  
- `image` (`ImageField`, optional, `upload_to='projects/'`)  

Includes:
- `Meta.ordering = ['title']`
- `verbose_name = "Project"`
- `verbose_name_plural = "Projects"`
- `__str__` returns `"Project: <title>"`

---

## Admin Configuration

`portfolio/admin.py`:

- `SkillAdmin`
  - `list_display = ('name', 'proficiency')`
  - `ordering = ('name',)`

- `ProjectAdmin`
  - `list_display = ('title', 'link')`
  - `ordering = ('title',)`
  - `filter_horizontal = ('skills',)`

This makes the admin interface clear and easy to use when populating data.

---

## Views and URLs

### Views (`portfolio/views.py`)
- `projects_view(request)`  
  - Retrieves all `Project` objects and renders `projects.html`.
- `skills_view(request)`  
  - Retrieves all `Skill` objects and renders `skills.html`.

### URLs
- `portfolio/urls.py`
  - `/projects/` → `projects_view` (name: `projects`)
  - `/skills/` → `skills_view` (name: `skills`)

- `config/urls.py`
  - `/admin/` → Django admin
  - `/` → includes `portfolio.urls`

---

## Templates

### `projects.html`
- Lists all projects with:
  - Title
  - Description
  - Optional image
  - Skills used (name + proficiency)
  - Optional external link

### `skills.html`
- Lists all skills with:
  - Name
  - Proficiency percentage

Both templates use the shared stylesheet at `/static/css/styles.css`.

---

## Styles

`static/css/styles.css`:

- Global:
  - `font-family: Cambria, serif;`
  - Generous padding and line-height for readability.
- `.project-card`:
  - Border, padding, margin, rounded corners, light background.
- Project images:
  - Max width, block display, rounded corners.

---

## How to Run

1. Create and activate a virtual environment.
2. Install Django (`pip install django`).
3. Run migrations:
   - `python manage.py makemigrations`
   - `python manage.py migrate`
4. Create a superuser:
   - `python manage.py createsuperuser`
5. Start the server:
   - `python manage.py runserver`
6. Visit:
   - `/admin/` to add Skills and Projects.
   - `/projects/` and `/skills/` to view them in the browser.

---

## Professional Enhancements

- Docstrings added to models and views for clarity.
- Validation on `proficiency` to enforce 0–100 range.
- `Meta` ordering for predictable display.
- Admin classes for better data management.
- Typography and spacing tuned for readability with Cambria.

This combination demonstrates strong technical understanding, clear structure,  
and attention to professional presentation.

---

## Skill Badge Icons 

1. Agile Project Management & Estimation
2. Content Strategy & Publishing Workflow
3. Full-Stack Network Professional (FSNP) Operations
4. Full-Stack Web Development (Django)
5. Leadership & Mission-Focused Execution
6. Mobile Development Foundations (MDI-1 & MDI-2)
7. Network Design & FSNP Practices
8. Systems Architecture & Workflow Design
9. Technical Documentation & System Thinking
10. Woodworking & Structural Planning
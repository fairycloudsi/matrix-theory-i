# Matrix Theory and Applications I — course website

Course site for **M571011S03 · Matrix Theory and Applications I**, a 16-week (32 contact hour)
graduate course built on Golub & Van Loan, *Matrix Computations*, 4th edition.

Live site: `https://<your-username>.github.io/matrix-theory-i/`

---

## Publishing this on GitHub Pages

Three steps, no build system and no CI required — GitHub Pages builds Jekyll natively.

1. **Create the repository** and push this directory to it:

   ```bash
   git init
   git add .
   git commit -m "Course website"
   git branch -M main
   git remote add origin https://github.com/<your-username>/matrix-theory-i.git
   git push -u origin main
   ```

2. **Turn on Pages.** Repository → *Settings* → *Pages* → **Source: Deploy from a branch**,
   branch `main`, folder `/ (root)`. The first build takes a minute or two.

3. **Set `baseurl`.** In `_config.yml`, `baseurl` must match the repository name:

   | Repository | `baseurl` |
   |---|---|
   | `matrix-theory-i` | `"/matrix-theory-i"` (the default here) |
   | any other name | `"/that-name"` |
   | `<username>.github.io` | `""` |

   Getting this wrong is the usual cause of a site that loads with no CSS.

Then fill in the placeholders in `_config.yml`: instructor name, email, meeting time, location,
and office hours. They appear on the home page and in the footer.

---

## Editing the course content

**The schedule lives in exactly one place: `_data/schedule.yml`.**

Both the schedule table and all sixteen week pages are generated from it, so they cannot drift
apart. To change a topic, a reading, or a learning objective, edit that file — nothing else.

### Posting slides and notes

Drop the file under `assets/` and add the path to the relevant week in `_data/schedule.yml`:

```yaml
- week: 3
  slug: "03"
  topic: "The singular value decomposition"
  slides: "/assets/slides/week03.pdf"    # add this
  notes:  "/assets/notes/week03.pdf"     # and this
```

The week page picks them up automatically and the "posted before class" placeholder disappears.
The same applies to `code:` (any URL) and `due:`.

### Adding announcements to a week

Each file in `_weeks/` holds only a `week:` number in its front matter. Anything you write in the
body appears *below* the materials block — the right place for announcements, worked examples, or
extra links.

### Adding a page

Create a markdown file in the root with front matter:

```yaml
---
layout: page
title: Office Hours
permalink: /office-hours/
---
```

To add it to the navigation bar, edit the `nav` line in `_layouts/default.html`.

---

## Building locally (optional)

Not required — you can edit on GitHub and let Pages build. If you want a local preview:

```bash
gem install jekyll bundler
jekyll serve
# http://localhost:4000/matrix-theory-i/
```

---

## Repository layout

```
_config.yml            site and course settings; baseurl lives here
_data/schedule.yml     ← the single source of truth for all 16 weeks
_layouts/
  default.html         page shell, header, navigation, footer
  page.html            ordinary content pages
  week.html            week pages, generated from schedule.yml
_weeks/                one near-empty stub per week (week-01.md … week-16.md)
assets/css/style.css   the entire stylesheet; light and dark
index.md               home
schedule.md            the 16-week table
assignments.md         grading, five assignments, quizzes, project
resources.md           textbooks, Van Loan's companion material, software
```

No plugins, no theme dependency, no JavaScript. The site is four pages plus sixteen generated
week pages, and the whole design is one stylesheet.

---

## Credits

Course structure follows the chapter and section order of Golub & Van Loan, *Matrix Computations*,
4th edition (Johns Hopkins University Press, 2013). Van Loan's freely available companion
material — M-files, errata, and the master bibliography — is linked from the Resources page.

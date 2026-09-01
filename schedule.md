---
layout: page
title: Schedule
permalink: /schedule/
---

Sixteen weeks, two hours each, {{ site.course.hours }} contact hours in total. Section and page
numbers refer to **Golub & Van Loan, _Matrix Computations_, 4th edition**. Reading load is
roughly 30 pages per week.

Click any week for objectives, algorithms, and materials.

<div class="table-scroll" markdown="0">
<table>
  <thead>
    <tr>
      <th class="num">Wk</th>
      <th>Topic</th>
      <th>Reading</th>
      <th>Theme</th>
      <th>Due</th>
    </tr>
  </thead>
  <tbody>
  {% assign current_part = "" %}
  {% for wk in site.data.schedule %}
    {% if wk.part != current_part %}
    <tr class="part-row"><td colspan="5">{{ wk.part }}</td></tr>
    {% assign current_part = wk.part %}
    {% endif %}
    <tr>
      <td class="num">{{ wk.week }}</td>
      <td>
        <a href="{{ '/weeks/week-' | append: wk.slug | append: '/' | relative_url }}">{{ wk.topic }}</a>
        {% if wk.flag %}<br><span class="badge badge--mark">{{ wk.flag }}</span>{% endif %}
      </td>
      <td>{{ wk.gvl }}<br><small>pp. {{ wk.pages }}</small></td>
      <td>{{ wk.theme }}</td>
      <td>{% if wk.due %}{{ wk.due }}{% else %}&mdash;{% endif %}</td>
    </tr>
  {% endfor %}
  </tbody>
</table>
</div>

## What is deliberately left out

A 32-hour course cannot cover a 747-page book. These are named in lecture but not examined, and
each makes a good project topic:

- **Chapter 9, Functions of Matrices** — the matrix exponential, sign, square root and logarithm.
- **Most of Chapter 10** — beyond the symmetric Lanczos process in Week 15.
- **§11.6, The Multigrid Framework** — a natural follow-on to Week 15.
- **§12.1–12.2, 12.4–12.5** — displacement structure, structured-rank problems, and tensor
  decompositions.
- **Parallel sections** (§1.6, §3.6) and the more specialised eigenvalue material (§7.6–7.9,
  §8.4–8.5, §8.7).

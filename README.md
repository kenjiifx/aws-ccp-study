# AWS CLF-C02 Cloud Practitioner Prep

A free, offline study app for the **AWS Certified Cloud Practitioner (CLF-C02)** exam. Open one HTML file in your browser — no install, no account, no backend.

## Quick start

1. Open [`clf_c02_study_app.html`](./clf_c02_study_app.html) in any modern browser.
2. Work through **Learn** → practice with **Quiz** / **Flashcards** → skim the **Cheat Sheet** before test day.

That’s it. Progress is saved in your browser’s `localStorage`.

## What’s inside

| Feature | Details |
| --- | --- |
| **Learn** | 19 lessons covering all four CLF-C02 domains, with key points, service comparisons, exam traps, and per-lesson quizzes (70%+ marks a lesson done) |
| **Quiz** | 218 practice questions — custom length, by domain, timed modes, multi-select support, explanations after each answer |
| **Flashcards** | 103 term/definition cards filtered by domain |
| **Cheat Sheet** | Condensed service & concept reference for last-minute review |

### Exam domains covered

| Domain | Weight |
| --- | --- |
| Cloud Concepts | 24% |
| Security & Compliance | 30% |
| Cloud Technology & Services | 34% |
| Billing, Pricing & Support | 12% |

## Suggested study path

1. Complete every lesson in **Learn** (1.1 → 4.3) at **70%+**.
2. Drill weak domains in **Quiz** and **Flashcards**.
3. Run an exam-style / readiness check in **Quiz**.
4. Skim the **Cheat Sheet** the day before.

## Project layout

```
clf_c02_study_app.html   # Ready-to-use study app (open this)
build_study_app.py       # Rebuilds the HTML from content modules
exam_content.py          # Base lessons + questions
extra_questions.py       # Extra practice questions
lesson_enrichment.py     # Comparisons & exam traps
flashcards_data.py       # Flashcard bank
```

## Rebuilding the app

If you edit the Python content modules, regenerate the HTML:

```bash
python build_study_app.py
```

Requires Python 3. No third-party packages.

## Notes

- This is an unofficial study aid — not affiliated with AWS.
- Exam blueprints and service names change; always cross-check with the [official CLF-C02 exam guide](https://aws.amazon.com/certification/certified-cloud-practitioner/).
- Best used as practice + recall, not as a dump of memorized answers.

## License

Use freely for personal study. Attribution appreciated if you fork or share.

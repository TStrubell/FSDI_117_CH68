# Effort Estimation – Planning Poker

## Scale Used

Modified Fibonacci scale for story points:

- 0, 0.5, 1, 2, 3, 5, 8, 13, 20, 40, 100

Story points represent **relative complexity**, **effort**, and **risk**,  
not exact hours.

---

## Story 1 – View Projects

**Story Points:** 3 (Small–Medium)

**Rationale:**  
- Requires connecting the `Project` model to a view and template.  
- Involves basic layout and styling.  
- Low risk, moderate complexity, mostly straightforward CRUD display.  
- No advanced interactivity or external integrations.

---

## Story 2 – View Skills

**Story Points:** 2 (Small)

**Rationale:**  
- Similar to the Projects list but simpler.  
- Only displays name and proficiency.  
- Ordering by name adds a small amount of complexity.  
- Very low risk and minimal uncertainty.

---

## Story 3 – Contact Tim

**Story Points:** 5 (Medium–Large)

**Rationale:**  
- Requires form design, validation, and email configuration.  
- Involves integration with an email backend (SMTP, credentials, environment).  
- Higher risk due to configuration issues and potential deployment differences.  
- More moving parts: form, view, messages, and error handling.

---

## How This Supports Project Management

- **Capacity Planning:**  
  - If the team’s velocity is, for example, 8 story points per sprint,  
    these three stories (3 + 2 + 5 = 10) might span more than one sprint  
    or require prioritization.

- **Risk Management:**  
  - The Contact story has more integration risk, so it may be scheduled earlier  
    to surface issues sooner.

- **Communication:**  
  - Story points and rationale help the Product Owner and Scrum Master  
    understand trade-offs and make informed decisions about scope and timelines.

This estimation session shows how developers contribute to planning,  
not just coding, by providing structured effort estimates and clear reasoning.

---

## Definition of Done (DoD) for Portfolio Stories

For any user story in this portfolio:

1. Code is written, reviewed, and passes tests.
2. The feature is visible and usable in the browser.
3. Styling is consistent with the Cambria-based theme.
4. Documentation (README or comments) explains how it works.
5. The story can be demonstrated end-to-end to a stakeholder.

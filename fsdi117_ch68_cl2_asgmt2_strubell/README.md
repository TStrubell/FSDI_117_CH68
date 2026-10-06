# FSDI-117 – ASSIGNMENT 2  

---

## USER STORY CREATION AND EFFORT ESTIMATION

- **STUDENT:** Tim Strubell  
- **COURSE #:** FSDI 117 – Agile Architecture and Software Project Management  
- **COHORT #:** 68  
- **CLASS #:** 2  
- **ASSIGNMENT #:** #2 – User Story and Effort Estimation (SGnG)  
- **FOLDER NAME:** `fsdi117_ch68_cl2_asgmt2_strubell`  
- **GITHUB REPO LINK:** `https://github.com/TStrubell/FSDI_117_Ch68.git`  

---

## OVERVIEW

This repository contains my work for **FSDI 117 – Agile Architecture and Software Project Management, Cohort 68, Class 2, Assignment 2: User Story and Effort Estimation** for the **Strubell Goods & Gear (SGnG)** portfolio project.

The assignment focuses on defining Agile user stories and acceptance criteria for key SGnG features, then applying **Planning Poker** with a **Fibonacci-based story point deck** to estimate relative effort and complexity for each story.

---

## FILES

- `user_stories.md` – User stories, acceptance criteria, and tasks.
- `estimation_session.md` – Effort estimation using Planning Poker and story points.

---

## METHODOLOGY

1. I identified core features of my portfolio (viewing projects, contacting me, and browsing skills).
2. I wrote user stories using the standard format:
   - As a `<role>`, I want `<goal>`, so that `<benefit>`.
3. I defined acceptance criteria using clear, testable conditions.
4. I assigned story points using the modified Fibonacci scale:
   - 0, 0.5, 1, 2, 3, 5, 8, 13, 20, 40, 100.
5. I documented the rationale behind each estimate to show how complexity, risk,  
   and uncertainty influence effort.

This demonstrates how developers contribute to project management through  
structured estimation and communication.

--- 

### 3. SGnG USER STORIES AND ACCEPTANCE CRITERIA

The assignment defines five core user stories for the SGnG Django portfolio:

1. **SGnG Projects Page (Visitor)**  
   - View a list of SGnG projects to understand Tim’s experience and domains.  
   - Acceptance criteria:  
     - `/projects/` page loads successfully.  
     - Each project card shows title, category, description, and skills.  
     - Data is pulled dynamically from the Django database.  
     - At least two projects appear on the page.

2. **SGnG Skills Page (Visitor)**  
   - View Tim’s skills to quickly understand technical strengths and expertise.  
   - Acceptance criteria:  
     - `/skills/` page loads successfully.  
     - Each skill card shows name, level, and description.  
     - Skills are retrieved from the Django database.  
     - Page uses SGnG-branded styling.

3. **SGnG Contact Form (Visitor)**  
   - Send a message through the contact page without leaving the portfolio site.  
   - Acceptance criteria:  
     - `/contact/` page displays a functional contact form.  
     - Fields: name, email, message.  
     - Submitting the form triggers Django’s `send_mail()` function.  
     - Email is successfully delivered to Tim’s inbox.  
     - A confirmation message appears after submission.

4. **SGnG Homepage (Visitor)**  
   - See a branded SGnG homepage that clearly communicates identity and purpose.  
   - Acceptance criteria:  
     - Homepage loads at `/`.  
     - Hero section shows SGnG branding, tagline, and mission.  
     - “View Portfolio” button links to `/projects/`.  
     - Layout uses SGnG colors and typography.

5. **Django Admin Management (Admin)**  
   - Manage projects and skills through Django admin without modifying code.  
   - Acceptance criteria:  
     - Django admin displays `Project` and `Skill` models under the Portfolio app.  
     - Admin pages allow adding, editing, and deleting entries.  
     - Slugs auto-populate based on project titles.  
     - Skills can be assigned to projects via a ManyToMany relationship.

---

### 4. PLANNING POKER DECK AND ESTIMATION APPROACH

The Planning Poker deck uses the **Fibonacci sequence**:

- **Cards:** 1, 2, 3, 5, 8, 13  
- **Meanings:**  
  - 1 – Trivial  
  - 2 – Very small  
  - 3 – Small  
  - 5 – Medium  
  - 8 – Large  
  - 13 – Very large / complex

For each user story, I asked:

1. How many files will this touch?  
2. How many Django concepts are involved (models, views, templates, forms, email, etc.)?  
3. How much unknown or risk is there?

A simulated team voting round was performed for the **Projects Page** story, resulting in a final estimate of **8 story points** after reconciling different votes and discussing complexity.

---

### 5. STORY POINT ESTIMATES

Final story point assignments (Planning Poker):

| USER STORY                 | STORY POINTS | REASONING SUMMARY                                                                  |
|----------------------------|--------------|------------------------------------------------------------------------------------|
| SGnG Projects Page         |     8        | Multiple components: models, admin, templates, CSS, dynamic data, ManyToMany.      |
| SGnG Skills Page           |     5        | Similar to projects but simpler; fewer relationships and less template complexity. |
| SGnG Contact Form + Email  |     13       | Highest complexity: forms, views, email backend, testing, error handling.          |
| SGnG Homepage              |     5        | Template + CSS work; moderate complexity, no backend logic.                        |
| Django Admin Management    |     3        | Straightforward admin registration and configuration.                              |

These estimates represent **relative effort**, not exact hours, and follow Agile best practices for story point estimation.

---

### 6. HOW PLANNING POKER APPLIES TO SGNG

Planning Poker supports the SGnG project by:

- **Prioritization:**  
  - High-point stories (8–13) are larger and riskier.  
  - Low-point stories (1–3) are quick wins.

- **Time Management:**  
  - With limited time, it is more practical to tackle a 3-point story (e.g., admin configuration) than a 13-point story (contact form + email).

- **Scope Communication:**  
  - The 13-point contact form/email story touches forms, views, email backend, and testing.  
  - The 5-point homepage story is mostly template and CSS work.

Overall, Planning Poker provides a structured, collaborative way to communicate scope and complexity and to plan development tasks for the SGnG portfolio.

---

### 7. BACKEND / LOGIC

For Assignment 2, **no backend code screenshots** are required. The focus is on Agile planning artifacts (user stories, acceptance criteria, and estimation).

---

### 8. AI DISCLOSURE

I used **Microsoft Copilot** to help organize and draft the written content for this assignment. Copilot did **not** generate any source code. All ideas, interpretations, and final responses represent my own understanding and were reviewed and finalized by me, **Tim Strubell**, in accordance with SDGKU’s AI-assisted learning guidelines.

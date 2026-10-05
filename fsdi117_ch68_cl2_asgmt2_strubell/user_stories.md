# User Stories for Developer Portfolio

## Story 1 – View Projects

**User Story**  
As a visitor, I want to view a list of projects with descriptions and links,  
so that I can understand the kind of work Tim has done.

**Acceptance Criteria (Gherkin-style)**  
Scenario: Viewing the projects list  
- Given I am on the Projects page  
- When I load the page  
- Then I should see a list of projects  
- And each project should display a title and description  
- And projects with links should show a clickable link  
- And projects with images should show a project image

**Tasks**  
- Design the Projects page layout.  
- Implement the Projects view in Django.  
- Connect the Projects page to the `Project` model.  
- Style the page using Cambria and consistent spacing.  
- Test that all projects appear correctly from the database.

---

## Story 2 – View Skills

**User Story**  
As a visitor, I want to see a list of Tim’s skills with proficiency levels,  
so that I can quickly understand his technical strengths.

**Acceptance Criteria**  
Scenario: Viewing the skills list  
- Given I am on the Skills page  
- When I load the page  
- Then I should see a list of skills  
- And each skill should display a name and proficiency percentage  
- And the list should be ordered alphabetically by skill name

**Tasks**  
- Design the Skills page layout.  
- Implement the Skills view in Django.  
- Connect the Skills page to the `Skill` model.  
- Ensure skills are ordered by name.  
- Test that all skills appear correctly from the database.

---

## Story 3 – Contact Tim

**User Story**  
As a visitor, I want to send a message to Tim through a contact form,  
so that I can reach out for collaboration or questions.

**Acceptance Criteria**  
Scenario: Sending a message via the contact form  
- Given I am on the Contact page  
- When I fill in my name, email, subject, and message  
- And I click the "Send" button  
- Then the system should validate that all fields are filled  
- And the system should send the message to Tim’s email address  
- And I should see a confirmation message if the email is sent  
- And I should see an error message if validation fails

**Tasks**  
- Design the Contact page layout and form.  
- Implement the contact view in Django.  
- Configure email settings for sending messages.  
- Add validation for required fields.  
- Test that emails are sent and error messages appear when needed.

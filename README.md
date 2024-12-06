# Run Wild

![Am I responsive image](assets/README_images/amiresponsive.png)

## Overview

### Purpose
Run Wild is a web-based platform designed to gamify the running experience and foster a community of active runners through a token-based reward system. The platform transforms everyday runs into rewarding achievements by allowing runners to earn tokens based on their performance, creating an engaging and motivating environment for consistent physical activity.

<details>
<summary>Objectives</summary>

1. **Motivate Regular Exercise**: By implementing a token reward system, the platform encourages users to maintain consistent running haibits.
2. **Foster Competition**: Create healthy competition through a global leaderboard system that recognises both dedication and performance.
3. **Build Community**: Develop a space where runners can compete and compare their achievements with others, creating a sense of belonging and mutual motivation.

</details>

<details>
<summary>Value Proposition</summary>

- Transforms routine running activities into rewarding experiences
- Provides immediate feedback and recognition for running achievements
- Creates a structured system for tracking progress and improvement
- Offers a competitive element that maintains long-term engagement
- Delivers a simple, streamlined experience focused on running metrics that matter

</details>

### Target Audience

<details>
<summary>Recreational Runners</summary>

- Age Range: 18+ years old
- Running Experience: Beginner to intermediate runners
- Motivation: Seeking additional motivation and structure in their running routine

</details>

<details>
<summary>Beginner Runners</summary>

- Looking for motivation to establish consistent running habits
- Interested in tracking progress and improvement
- Need positive reinforcement to maintain commitment
- Value clear metrics and achievable goals
  
</details>

<details>
<summary>Regular Runners</summary>

- Seeking new ways to stay motivated
- Interested in competing with others
- Want to track their performance metrics
- Looking for recognition of their efforts

</details>

<details>
<summary>Challenge-Driven Individuals</summary>

- Motivated by competition and achievements
- Enjoy collecting rewards and tracking statistics
- Like to compare their performance with others
- Appreciate structured goal systems

</details>

### Why They Will Benefit?

<details>
<summary>Motivation Through Rewards</summary>

- Immediate gratification through token earnings
- Visual representation of progress
- Clear connection between effort and rewards

</details>

<details>
<summary>Progress Tracking</summary>

- Detailed run history
- Performance metrics tracking
- Clear visibility of improvement over time

</details>

<details>
<summary>Community Engagement</summary>

- Global leaderboard participation
- Competitive element
- Sense of belonging to a running community

</details>

<details>
<summary>Accessibility</summary>

- Simple, user-friendly interface
- Clear token earning structure
- Easy submission process for runs

</details>

### User Needs Addressed:

- Need for motivation to maintain regular running habits
- Desire for recognition of running achievements
- Want for structured progress tracking
- Interest in competing with other runners
- Requirement for simple, straightforward run logging

The aim of this web app is to specifically addresses the growing trend of gamification in fitness applications whilst maintaining a focus on simplicity and user engagement. By combining traditional run tracking with a reward system, Run Wild creates a unique value proposition for runners who are looking for additional motivation and structure in their running routine.

## UX Design Process

### Strategy Plane
<hr>

<details>
<summary>User Stories</summary>

### Must Have Features

#### <u>Quest Management</u>

**User Story:** As a site user, I can view a paginated list of quests so that I can select which run I want to view. 

<details>
<summary>Acceptance Criteria:</summary>

- Given more than one quest in the database, these multiple quests are listed
- When a user opens the main page a list of quests is seen
- The user sees all quests titles with pagination to choose what to complete

</details>

#### <u>Run Tracking</u>

**User Story:** As a user I can submit my run details so that I can earn tokens

<details>
<summary>Acceptance Criteria:</summary>
  
- User can input completion time
- Submission process:
  - Confirms submission success
  - Displays tokens earned
- User can update and delete runs

</details>

#### <u>User Authentication</u>

**User Story:** As a registered user I can log into my account so that I can access my running history and tokens

<details>
<summary>Acceptance Criteria:</summary>
  
- User can log in using email/username and password

</details>

**User Story:** As a new user I want to register for an account so that I can track my runs and earn tokens

<details>
<summary>Acceptance Criteria:</summary>
  
- User can create account using email and password
- Profile is automatically created upon registration
- Initial token balance is set to 0
- Password must meet minimum security requirements:
  - At least 8 characters
  - Contains at least one number
  - Contains at least one special character

</details>

#### <u>Responsive Design</u>

**User Story:** As a user I want the site to be responsive so that I can use on any device

<details>
<summary>Acceptance Criteria:</summary>
  
- Site is usable on desktop, tablet, and mobile devices
- Layout adjusts appropriately to different screen sizes

</details>

#### <u>Accessibility</u>

**User Story:** As a User I require the site to be accessible so that I can utilise the website fully, regardless of potential visual impairments

<details>
<summary>Acceptance Criteria:</summary>
  
- Colour contrast, fonts, images and screen reading capabilities adhered to
- Good use of semantic elements

</details>

#### <u>Token System</u>

**User Story:** As a user I want to earn tokens so that can feel rewarded for my run

<details>
<summary>Acceptance Criteria:</summary>
  
- Token calculation:
  - Base rate: 10 tokens per km

- System must:
  - Calculate tokens instantly
  - Display calculation breakdown
  - Update user's total balance

- Transaction details include:
  - Date and time
  - Amount earned
  - Running total

- Notifications:
  - Immediate token earning notification

</details>

### Should Have Features

#### <u>Leaderboard</u>

**User Story:** As a user I want a leaderboard so that I can see how I rank against others

<details>
<summary>Acceptance Criteria:</summary>
  
- Leaderboard shows:
  - Total tokens earned
  - Total distance

- Privacy:
  - Only shows display user names

</details>

#### <u>Enhanced Token System</u>

**User Story:** As a user I want to have more token bonus so that I can gain more tokens

<details>
<summary>Acceptance Criteria:</summary>
  
- Pace bonuses:
  - Sub 4:00 min/km: +15 tokens/km
  - Sub 5:00 min/km: +10 tokens/km
  - Sub 6:00 min/km: +5 tokens/km


- Personal best bonus:
  - +5 tokens if personal best for route is achieved

- Difficulty bonus:
  - No bonus for easy
  - +5 for medium
  - +10 for hard

</details>

</details>

### Scope Plane
<hr>

<details>
<summary>Core Features:</summary>

- User authentication and profile management
- Running activity tracking and logging
- Token achievement system
- Leaderboards

</details>

### Structure Plane
<hr>

<details>
<summary>Logical structure</summary>

The application follows a logical structure where users can:

- Register/Login to access their personal dashboard
- Log and track running activities
- Earn tokens based on activity completion
- View their ranking on various leaderboards

</details>

### Skeleton Plane
<hr>

#### Wireframes

<details>
<summary>Desktop</summary>

![desktop wireframes](assets/README_images/WF_desktop_home.png)
![desktop wireframes](assets/README_images/WF_desktop_quest_about_leader.png)
![desktop wireframes](assets/README_images/WF_desktop_quest_page.png)

</details>
<br>
<details>
<summary>Mobile</summary> 

![mobile wireframes](assets/README_images/WF_mobile_index.png)
![mobile wireframes](assets/README_images/WF_mobile_quest_post.png)
![mobile wireframes](assets/README_images/WF_mobile_quest_page.png)
![mobile wireframes](assets/README_images/WF_mobile_about_leader.png)

</details>
<br>
<details>
<summary>Tablet</summary> 

![tablet wireframes](assets/README_images/WF_tablet_home.png)
![tablet wireframes](assets/README_images/WF_tablet_quest_post.png)
![tablet wireframes](assets/README_images/WF_tablet_about_quest_leader.png)

</details>
<br>
<details>
<summary>Database Schema</summary> 

![Database Schema](assets/README_images/ERD_Final.png)

</details>

### Surface Plane
<hr>

#### Design Chocies

<details>
<summary>Color Scheme</summary> 

My color palette was chosen to reflect Run Wild's gamified running experience and token-based achievements, aiming to create a clean, modern and sporty user interface,
To acheive only one accent colour has been chosen. 

![Colour Pallet](assets/README_images/colour-pallet.png)

Off White (#fafdfb) - Primary Background

- Creates a soft, clean canvas that reduces eye strain
- Provides excellent contrast for text and interactive elements
- Maintains readability across different screen sizes and lighting conditions

Dark Gray (#212121) - Text Color

- Ensures optimal readability against the light background
- Softer than pure black, creating a more comfortable reading experience
- Meets WCAG accessibility standards for contrast

Vibrant Red (#ff1744) - Accent Color

- Creates visual excitement and energy
- Draws attention to important actions and achievements
- Represents passion and motivation in fitness

Pure White (#fff)

- Used for contrast on Dark Gray elements

</details>
<br>
<details>
<summary>Typography:</summary> 
The typography combines two distinctive fonts to create a modern and energetic aesthetic while maintaining readability

![Bebas Font](assets/README_images/bebas_font.png)

Used for:

- Headlines
- Section titles
- Important numbers (statistics, achievements)

Characteristics:

- All-caps display font
- Strong visual impact
- Creates a bold, athletic feel
- Excellent for hierarchy and emphasis


![lato Font](assets/README_images/lato_font.png)

Used for:

- Body text
- Navigation items
- Form elements
- Secondary headings

Characteristics:

- High readability at all sizes
- Clean and modern sans-serif
- Excellent for long-form content
- Various weights for flexibility

##### Font Awesome

Icons: Font Awesome for intuitive navigation

</details>

#### Design Principles

##### 1. Clarity

- Clean layouts with ample white space
- Clear visual hierarchy
- Intuitive navigation


##### 2. Consistency

- Consistent colour usage across all pages
- Standardised spacing and alignment
- Uniform interactive elements


##### 2. Accessibility

- High contrast text-to-background ratios
- Clear focus states for navigation
- Readable font sizes and line heights


##### 2. Responsiveness

- Fluid typography scaling
- Flexible grid system
- Mobile-first approach to layout


This design system creates an energetic, modern interface that motivates users while maintaining excellent usability and accessibility standards.


## Technologies/Languages/Frameworks Used 


**HTML5** - Structuring of the website<br>
**CSS3** - Design, layout and visual aesthetics<br>
**JavaScript** - For interactivity and DOM manipulation on the frontend<br>
**Python (Django)** - Backend web framework for server-side logic and management<br>
**PostgreSQL** - Database management system<br>
**Cloudinary** - Cloud-based image storage<br>
**Whitenoise** - For serving static files directly from Django<br>
**Django** - Backend framework<br>
**Django Crispy Forms** - Form rendering<br>
**Whitenoise** - For serving static files<br>
**GitHub Projects** - Project management and tracking<br>
**Heroku** - Deployment and hosting<br>
**Balsamiq** - Wireframes and design prototypes<br>


## Testing and Validation

### Testing Results
Summarize the results of testing across different devices and screen sizes.  
Mention any issues found and how they were resolved.  
**Guidance:** Summarize the results of your testing across various devices using tools like Chrome DevTools, as outlined in Phase 2. Mention any issues found and how they were resolved.

### Validation
Discuss the validation process for HTML and CSS using W3C and Jigsaw validators.  
Include the results of the validation process.  
**Guidance:** Document your use of W3C and Jigsaw validators to ensure your HTML and CSS meet web standards. Include any errors or warnings encountered and how they were resolved.

## AI Tools Usage

### GitHub Copilot
Brief reflection on the effectiveness of using AI tools for debugging and validation.  
**Guidance:** Reflect on how GitHub Copilot assisted with debugging and validation, particularly any issues it helped resolve.

## Deployment

### Deployment Process
Briefly describe the deployment process to GitHub Pages or another cloud platform.  
Mention any specific challenges encountered during deployment.  
**Guidance:** Describe the steps you took to deploy your website during Phase 4: Final Testing, Debugging & Deployment, including any challenges encountered.

## AI Tools Usage

### Reflection
Describe the role AI tools played in the deployment process, including any benefits or challenges.  
**Guidance:** Reflect on how AI tools assisted with the deployment process, particularly how they streamlined any tasks or presented challenges.

## Reflection on Development Process

### Successes
Effective use of AI tools, including GitHub Copilot and DALL-E, and how they contributed to the development process.

### Challenges
Describe any challenges faced when integrating AI-generated content and how they were addressed.

### Final Thoughts
Provide any additional insights gained during the project and thoughts on the overall process.  
**Guidance:** Begin drafting reflections during Phase 1 and update throughout the project. Finalize this section after Phase 4. Highlight successes and challenges, particularly regarding the use of AI tools, and provide overall insights into the project.

## Code Attribution
Properly attribute any external code sources used in the project (excluding GitHub Copilot-generated code).  
**Guidance:** Document any external code sources used throughout the entire project, especially during Phase 2 and Phase 3. Exclude GitHub Copilot-generated code from attribution.

## Future Improvements
Briefly discuss potential future improvements or features that could be added to the project.  
**Guidance:** Reflect on potential enhancements that could be made to the project after Phase 4: Final Testing, Debugging & Deployment. These could be Could user story features you didn’t have time to implement or improvements based on testing feedback.
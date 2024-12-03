# Run Wild

## Overview

### Purpose
Run Wild is a web-based platform designed to gamify the running experience and foster a community of active runners through a token-based reward system. The platform transforms everyday runs into rewarding achievements by allowing runners to earn tokens based on their performance, creating an engaging and motivating environment for consistent physical activity.

#### Objectives:

1. **Motivate Regular Exercise**: By implementing a token reward system, the platform encourages users to maintain consistent running haibits.
2. **Foster Competition**: Create healthy competition through a global leaderboard system that recognises both dedication and performance.
3. **Build Community**: Develop a space where runners can compete and compare their achievements with others, creating a sense of belonging and mutual motivation.

#### Value Proposition:

- Transforms routine running activities into rewarding experiences
- Provides immediate feedback and recognition for running achievements
- Creates a structured system for tracking progress and improvement
- Offers a competitive element that maintains long-term engagement
- Delivers a simple, streamlined experience focused on running metrics that matter

### Target Audience

#### Primary Audience: Recreational Runners

- Age Range: 18+ years old
- Running Experience: Beginner to intermediate runners
- Motivation: Seeking additional motivation and structure in their running routine

#### 1. Beginner Runners
- Looking for motivation to establish consistent running habits
- Interested in tracking progress and improvement
- Need positive reinforcement to maintain commitment
- Value clear metrics and achievable goals
  
#### 2. Regular Runners
- Seeking new ways to stay motivated
- Interested in competing with others
- Want to track their performance metrics
- Looking for recognition of their efforts

#### 3. Challenge-Driven Individuals
- Motivated by competition and achievements
- Enjoy collecting rewards and tracking statistics
- Like to compare their performance with others
- Appreciate structured goal systems

### Why They Will Benefit:

#### Motivation Through Rewards

- Immediate gratification through token earnings
- Visual representation of progress
- Clear connection between effort and rewards

#### Progress Tracking

- Detailed run history
- Performance metrics tracking
- Clear visibility of improvement over time

#### Community Engagement

- Global leaderboard participation
- Competitive element
- Sense of belonging to a running community

#### Accessibility

- Simple, user-friendly interface
- Clear token earning structure
- Easy submission process for runs

### User Needs Addressed:

- Need for motivation to maintain regular running habits
- Desire for recognition of running achievements
- Want for structured progress tracking
- Interest in competing with other runners
- Requirement for simple, straightforward run logging

The aim of this web app is to specifically addresses the growing trend of gamification in fitness applications whilst maintaining a focus on simplicity and user engagement. By combining traditional run tracking with a reward system, Run Wild creates a unique value proposition for runners who are looking for additional motivation and structure in their running routine.

## UX Design Process

### Strategy Plane

## User Stories

### Must Have Features

### <u>Quest Management</u>
**User Story:** As a site user, I can view a paginated list of quests so that I can select which run I want to view. 

**Acceptance Criteria:** 
- Given more than one quest in the database, these multiple quests are listed
- When a user opens the main page a list of quests is seen
- The user sees all quests titles with pagination to choose what to complete

### <u>Run Tracking</u>

**User Story:** As a user I can submit my run details so that I can earn tokens

**Acceptance Criteria:** 
  
- User can input completion time
- Submission process:
  - Confirms submission success
  - Displays tokens earned
- User can update and delete runs

### <u>User Authentication</u>

**User Story:** As a registered user I can log into my account so that I can access my running history and tokens

**Acceptance Criteria:** 
  
- User can log in using email/username and password

**User Story:** As a new user I want to register for an account so that I can track my runs and earn tokens

**Acceptance Criteria:** 
  
- User can create account using email and password
- Profile is automatically created upon registration
- Initial token balance is set to 0
- Password must meet minimum security requirements:
  - At least 8 characters
  - Contains at least one number
  - Contains at least one special character

### <u>Responsive Design</u>

**User Story:** As a user I want the site to be responsive so that I can use on any device

**Acceptance Criteria:** 
  
- Site is usable on desktop, tablet, and mobile devices
- Layout adjusts appropriately to different screen sizes

### <u>Accessibility</u>

**User Story:** As a User I require the site to be accessible so that I can utilise the website fully, regardless of potential visual impairments

**Acceptance Criteria:** 
  
- Colour contrast, fonts, images and screen reading capabilities adhered to
- Good use of semantic elements

### <u>Token System</u>

**User Story:** As a user I want to earn tokens so that can feel rewarded for my run

**Acceptance Criteria:** 
  
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

### Should Have Features

### <u>Leaderboard</u>

**User Story:** As a user I want a leaderboard so that I can see how I rank against others

**Acceptance Criteria:** 
  
- Leaderboard shows:
  - Total tokens earned

- Privacy:
  - Only shows display names

### <u>Enhanced Token System</u>

**User Story:** As a user I want to have more token bonus so that I can gain more tokens

**Acceptance Criteria:** 
  
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

### Scope Plane

#### Core Features:

- User authentication and profile management
- Running activity tracking and logging
- Token achievement system
- Leaderboards

### Structure Plane

The application follows a logical structure where users can:

- Register/Login to access their personal dashboard
- Log and track running activities
- Earn tokens based on activity completion
- View their ranking on various leaderboards

### Skeleton Plane

#### Wireframes

##### Desktop
![desktop wireframes](assets/README_images/WF_desktop_home.png)
![desktop wireframes](assets/README_images/WF_desktop_quest_about_leader.png)
![desktop wireframes](assets/README_images/WF_desktop_quest_page.png)

##### Mobile
![mobile wireframes](assets/README_images/WF_mobile_index.png)
![mobile wireframes](assets/README_images/WF_mobile_quest_post.png)
![mobile wireframes](assets/README_images/WF_mobile_quest_page.png)
![mobile wireframes](assets/README_images/WF_mobile_about_leader.png)

##### Tablet
![tablet wireframes](assets/README_images/WF_tablet_home.png)
![tablet wireframes](assets/README_images/WF_tablet_quest_post.png)
![tablet wireframes](assets/README_images/WF_tablet_about_quest_leader.png)


#### Database Schema

![Database Schema](assets/README_images/ERD_Final.png)


(Include any could-have features that were implemented or considered)  
**Guidance:** If any could-have features were implemented, describe them here. This is an opportunity to showcase extra work done beyond the initial scope. But remember - keep it simple! Focus on the Must stories first. Could user story features are commonly earmarked for future project iterations.



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
# Run Wild

![Am I responsive image](assets/README_images/amiresponsive.png)

## Overview

[Live Project](https://run-wild-67c9460e78b3.herokuapp.com/)

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
<details>
<summary>Mobile</summary> 

![mobile wireframes](assets/README_images/WF_mobile_index.png)
![mobile wireframes](assets/README_images/WF_mobile_quest_post.png)
![mobile wireframes](assets/README_images/WF_mobile_quest_page.png)
![mobile wireframes](assets/README_images/WF_mobile_about_leader.png)

</details>
<details>
<summary>Tablet</summary> 

![tablet wireframes](assets/README_images/WF_tablet_home.png)
![tablet wireframes](assets/README_images/WF_tablet_quest_post.png)
![tablet wireframes](assets/README_images/WF_tablet_about_quest_leader.png)

</details>
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

<details>
<summary>Typography</summary> 
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

## Features

<details>
<summary>Home Page</summary>

1. Welcome Section
   - Introduces the platform, emphasising gamified running and exploring Cornwall's scenic routes.
2. Call-to-Action
    - Encourages visitors to sign up or log in to start their running journey.
2. Number counters
    - provding a overview of all the completed quests so far.
3. About Us
    - Highlights the mission of turning running into an engaging and rewarding adventure.
4. Featured Routes
    - Bootstrap carosuaul used to showcases avaliable quests.
5. Key Benefits
    - Explains tokens, challenges, and leaderboards for motivation and fun.

![Home Page](assets/README_images/home_page.png)
![Current Quests and About](assets/README_images/current_quests_about.png)
![Token Caculation](assets/README_images/run_upload_caculation.png)

</details>

<hr>
<details>
<summary>User Authentication</summary>

1. Sign-Up Functionality
    - Users can create accounts to access features like their dashboard, and Run Tracking functionality.
2. Login System
    - Secure login allows users to resume their progress and view completed quests.
3. Login in Status
    - In the top right, the status of user is displayed.
4. Role Based functionality
    - Admin pannel link only availible when you are signed in as a superuser.
5. User Messages
    - Message pop ups giving user further claification on action completed for all user Authentication actions

![Sign Up](assets/README_images/sign_up.png)
![Sign In](assets/README_images/sign_in.png)
![Sign Out](assets/README_images/sign_out.png)
![User Dashboard](assets/README_images/dashboard.png)
![Message](assets/README_images/user_message.png)

</details>
<hr>
<details>
<summary>Quest Management</summary>

1. Avalibale Quest
    - Pagination for avalible quests for the user to select, reachable in the navigation.
2. Quest Details
    - Quest overview - breif descirption of route and image showing markers for route.
    - Difficulity, Distance, Elevation gain and Max displayed so user can assess if they are able to acheive.
    - Total Quests complete and Top 5 uploads displayed on each Quest Post.
    - Details of Completed runs shown, authenticated users can also access CRUD functionality here.
     

![Pagination of Quests](assets/README_images/quest_post_pagination.png)
![Quest View and Details](assets/README_images/quest_view_and_details.png)
![Completed Quests](assets/README_images/completed_runs.png)


</details>
<hr>
<details>
<summary>Run Tracking</summary>

CRUD functionality - The user is able to upload, edit and delete their uploads on the quest page.

![Upload Run](assets/README_images/run_upload.png)
![Delete Run](assets/README_images/run_delete.png)
![Update Run](assets/README_images/run_update.png)

</details>
<hr>

<details>
<summary>Leaderboards</summary>
Pagination for avalible quests for the user to select, reachable in the navigation.

![Global Leaderboard](assets/README_images/global_leaderboard.png)
![Top 5](assets/README_images/top-5.png)

</details>
<hr>

<details>
<summary>Token Stystem</summary>

The token system is designed to reward runners based on multiple factors:
- Base distance completed
- Running pace
- Personal best achievements
- Quest difficult

**Token caculation Components**
1. Base Tokens

    ```base_tokens = round(quest.distance * 10)```

- 10 Tokens awarded per kilometer
    - Example: 5km run = 50 base tokens

2. Pace Bonus System
Rewards faster runners with additional tokens based on pace (minutes per kilometer):

    | Pace (min/km) | Bonus Tokens per km | Example for 5km |
    |---------------|---------------|---------------|
    | Under 4:00 | +15 tokens | +75 tokens |
    | Under 5:00 | +10 tokens | +50 tokens |
    | Under 6:00 | +5 tokens | +25 tokens |
    | Under 7:00 | +2 tokens | +10 tokens |

3. Personal Best Bonus
- +5 tokens for achieving a personal best time on a quest
- System automatically tracks and updates personal best status
- Only one run per quest can hold personal best status

4. Difficulty Multiplier 
Final token amounts is mulitplied based on quest difficulty:
- Easy: 1.0x (no change)
- Medium: 1.1x (10% bonus)
- Hard: 1.2x (20% bonus)

5. Caculation examples
The user inputs their completion time as:
    - Hours
    - Minutes
    - Seconds

    Example 1: Casual 5km Run
    ```
    Distance: 5km
    Time Input: 0:32:30 (32 minutes, 30 seconds)

    Time Conversion:
    - Total seconds: (0 * 3600) + (32 * 60) + 30 = 1,950 seconds
    - Minutes: 1,950 / 60 = 32.5 minutes
    - Pace: 32.5 / 5 = 6.5 min/km

    Calculations:
    Base tokens: 5km × 10 = 50 tokens
    Pace bonus: 5km × 2 = 10 tokens (under 7:00 pace)
    Personal best bonus: 0 tokens
    Subtotal: 60 tokens
    Difficulty: Easy (1.0×)
    Final tokens: 60 tokens
    ```
    Example 2: Fast 5km Run with Personal Best
    ```
    Distance: 5km
    Time Input: 0:19:30 (19 minutes, 30 seconds)

    Time Conversion:
    - Total seconds: (0 * 3600) + (19 * 60) + 30 = 1,170 seconds
    - Minutes: 1,170 / 60 = 19.5 minutes
    - Pace: 19.5 / 5 = 3.9 min/km

    Calculations:
    Base tokens: 5km × 10 = 50 tokens
    Pace bonus: 5km × 15 = 75 tokens (under 4:00 pace)
    Personal best bonus: 5 tokens
    Subtotal: 130 tokens
    Difficulty: Hard (1.2×)
    Final tokens: 156 tokens
    ```
    Example 3: Long Distance Run
    ```
    Distance: 10km
    Time Input: 1:05:00 (1 hour, 5 minutes)

    Time Conversion:
    - Total seconds: (1 * 3600) + (5 * 60) + 0 = 3,900 seconds
    - Minutes: 3,900 / 60 = 65 minutes
    - Pace: 65 / 10 = 6.5 min/km

    Calculations:
    Base tokens: 10km × 10 = 100 tokens
    Pace bonus: 10km × 2 = 20 tokens (under 7:00 pace)
    Personal best bonus: 0 tokens
    Subtotal: 120 tokens
    Difficulty: Medium (1.1×)
    Final tokens: 132 tokens
    ```

![User Completed Run Message](assets/README_images/upload_message.png)

</details>
<hr>


## Technologies/Languages/Frameworks Used 


<img src="https://img.shields.io/badge/html5%20-%23E34F26.svg?&style=for-the-badge&logo=html5&logoColor=white"/><img src="https://img.shields.io/badge/css3%20-%231572B6.svg?&style=for-the-badge&logo=css3&logoColor=white"/><img src="https://img.shields.io/badge/javascript%20-%23323330.svg?&style=for-the-badge&logo=javascript&logoColor=%23F7DF1E"/><img src="https://img.shields.io/badge/python%20-%2314354C.svg?&style=for-the-badge&logo=python&logoColor=white"/><img src="https://img.shields.io/badge/bootstrap%20-%23563D7C.svg?&style=for-the-badge&logo=bootstrap&logoColor=white"/><img src="https://img.shields.io/badge/django%20-%23092E20.svg?&style=for-the-badge&logo=django&logoColor=white"/><img src="https://img.shields.io/badge/heroku%20-%23430098.svg?&style=for-the-badge&logo=heroku&logoColor=white"/><img src="https://img.shields.io/badge/markdown-%23000000.svg?&style=for-the-badge&logo=markdown&logoColor=white"/><img src="https://img.shields.io/badge/git%20-%23F05033.svg?&style=for-the-badge&logo=git&logoColor=white"/><img src="https://img.shields.io/badge/github%20-%23121011.svg?&style=for-the-badge&logo=github&logoColor=white"/>

### Other:
**PostgreSQL** - Database management system<br>
**Cloudinary** - Cloud-based image storage<br>
**Whitenoise** - For serving static files directly from Django<br>
**Django Crispy Forms** - Form rendering<br>
**Whitenoise** - For serving static files<br>
**GitHub Projects** - Project management and tracking<br>
**Balsamiq** - Wireframes and design prototypes<br>

## Testing and Validation

### Testing Results
Summarize the results of testing across different devices and screen sizes.  
Mention any issues found and how they were resolved.  
**Guidance:** Summarize the results of your testing across various devices using tools like Chrome DevTools, as outlined in Phase 2. Mention any issues found and how they were resolved.

### Validation

<details>
<summary>HTML</summary>

[W3C](https://validator.w3.org/) - Used for HTML Validation - results as follows:

1. index.html/base.html

![Index and base html](assets/README_images/html_index.png)

 - Fixes:
    - Trailing backslash removed from line 14 (base.html)
    - span tags changed to div - fixing errors 2 and 3.
    - Carousel errors fixed by added else statments to ensure no empty attributes.
<hr>

2. about.html

![About page](assets/README_images/about.png)
- No errors
<hr>

3. Sign in, up and out

![Sign up](assets/README_images/signup.png)

- Sign up 
    - The errors flagged are from allauth code and not something I can adjust - to note the opening takes for the span and p are present in the code as shown in the image below.
    ![allauth code](assets/README_images/signup_allauth.png)

![Sign up](assets/README_images/signin.png)
- Sign in
    - No Errors

![Sign out](assets/README_images/signout.png)
- Sign out
    - No Errors
<hr>   

4. dashboard.html

![Dashboard](assets/README_images/dashboard_val.png)
- No errors
<hr>

5. leaderboard.html

![Leaderboard](assets/README_images/leaderboard.png)
- Fixes:
    - Heading elements removed from table header, styling added to style.css to fix.
      ```
      .th-leaderboard {
          background: #f5f5f5;
          font-weight: 500;
          font-family: "Bebas Neue", sans-serif;
          font-size: 1.8em;
      }
      ```
<hr>

6. quests.html

![Quest](assets/README_images/Quests.png)

- Fixes:
    - Remove trailing backlash from hard returns

<hr>

6. quest_post.html

![Quest Post](assets/README_images/Quest_post.png)
- Fixes:
    - Heading elements removed from table header, styling added to style.css to fix.
      ```
      th {
        font-family: "Bebas Neue", sans-serif;
        font-weight: 500;
        font-size: 1.5em;
      }
      ```
<hr>

8. about.html

![About](assets/README_images/about.png)
- No errors

</details>

<details>
<summary>CSS</summary>

[Jigsaw](https://jigsaw.w3.org/css-validator/) - used for testing css, results as follows:

![CSS validator results](assets/README_images/css-validator.png)

- Fixes:
    - Remove border-color as not in use
    - Remove border-radius as not in use
    - Remove pesudo-element

</details>

<details>
<summary>JavaScript</summary>

[JSLint] - used for testing JavaScript files, results as follows:

1. index_scirpt.js

![Index scirpt results]()

</details>


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
# crowdfunding_back_end
# Clean-future ( Cristiane Tanaka)
view deployed site: https://clear-future.fly.dev/
Clean-Future crowdfunding platform links various NGO whose main focus is on Recycling.We aim to raise funds for NGO's whose main focus in on recycling -Textile, whitegoods, furniture, plastics and UHT.
## Intended Audience/User Stories
Clean future is for any NGO or those who cares about reducing waste to go on landfill. 
### Front End Pages/Fuctionality
-TBA
### API Spec
| Endpoint         | Method | Request Body   | Authentication Required?            | Implemented? |
|------------------|--------|----------------|-------------------------------------|--------------|
| /projects/       | GET    |                | No                                  | Yes          |
| /projects/       | POST   | Project Object | Yes                                 | Yes          |
| /projects/1/     | GET    | Project Object | No                                  | Yes          |
| /projects/1/     | PUT    | Project Object | Yes Must be project owner           | Not working  |
| /projects/1/     | DELETE | Project Object | Yes Must be project owner           | Not working  |
| /pledges/        | GET    |                | No                                  | Yes          |
| /pledges/        | POST   | Pledge Object  | Yes                                 | Yes          |
| /users/          | GET    |                | No                                  | Yes          |
| /users/          | POST   | User Object    | No                                  | Yes          |
| /users/1/        | GET    | User Object    | No                                  | Yes          |
| /users/1         | PUT    | User Object    | Yes Request user must equal user id | Not working  |
| /api-token-auth/ | POST   | User           | N/A                                 | Yes          |
### DB Schema
![DB Schema](<Images/DB shema.png>)
### Insomnia- How to create Users and Project in Insomnia

Creating a User
1. From your Insomnia dashboard, create a Collection. 
2. In a Collection, select New Request.
3. In the New Request modal: 
    - Select a POST method from the dropdown. 
    - Enter https://clear-future.fly.dev/users/ in the request URL field.
    - Change the request body to JSON and enter the below block of code:

        '''

            {
            "username": [Enter your information here],
            "password": [Enter password here],
            }

        '''

    - Click Send

Request an Authentication Token
1. Create a new HTTP request
2. Select a POST method from the dropdown. 
    - Enter https://clear-future.fly.dev/api-token-auth/ in the request URL field. 
3. Change the request body to JSON and enter your username and password in this format:

        {
            "username": [Enter your information here],
            "password": [Enter password here]
        }
4. You will receive a token as a response. For any further requests which require authentication, you will need to enter this under the Auth tab. 
5. In the Auth tab, select "Bearer Token". Ensure this is enabled, enter your token in the Token field, and enter "Token" in the Prefix field. 

Creating a Project
1. Ensure you have followed the steps above to be authenticated. 
2. Create a new HTTP request. 
3. Select a POST method from the dropdown. 
    - Enter https://clear-future.fly.dev/projects/ in the request URL field. 
4. Change the request body to JSON and enter the information below: 

    '''

        {
        "title":"Project 22",
        "description": "The 22 project.",
        "goal":500,
        "image":"https://via.placeholder.com/300.jpg",
        "is_open":true,
        "date_created":"2020-03-20T14:28:23.382748Z",
        "owner":"Real Creator"
        }

    '''



### Insomnia Screenshots
![GET Request]![alt text](<Images/Get method projects.png>)
![POST Request]![alt text](<Images/Post method projects.png>)
![Token Request]![alt text](<Images/Token return projects.png>)


[TBC] Be separated into two distinct projects: an API built using the Django RestFramework and a website built using React.
    
    [X] Have a cool name, bonus points if it includes a pun and/or missing vowels. See https://namelix.com/ for inspiration. (Bonus Points are meaningless)
    [X] Have a clear target audience.
    [X] Have user accounts. A user should have at least the following attributes:
        [X] Username
        [X] Email address
        [X] Password
    [X] Ability to create a “project” to be crowdfunded which will include at least thefollowing attributes:
        [X] Title
        [X] Owner (a user)
        [X] Description
        [X] Image
        [X] Target amount to fundraise
        [X] Whether it is currently open to accepting new supporters or not
        [X] When the project was created
    [X] Ability to “pledge” to a project. A pledge should include at least the followingattributes:
        [X] An amount
        [X] The project the pledge is for
        [X] The supporter/user (i.e. who created the pledge)
        [X] Whether the pledge is anonymous or not
        [X] A comment to go along with the pledge
    [ ] Implement suitable update/delete functionality, e.g. should a project owner beallowed to update a project description?
    [X] Implement suitable permissions, e.g. who is allowed to delete a pledge? - 
    [X] Return the relevant status codes for both successful and unsuccessful requeststo the API.
    [X] Handle failed requests gracefully (e.g. you should have a custom 404 pagerather than the default error page).
    [X] Use Token Authentication.
    [TBC] Implement responsive design.
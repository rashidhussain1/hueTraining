# hueTraining

API

GET APIs 

1.	Getting list of all projects
a.	/project/
2.	Getting list of issues
a.	/issues/
3.	Getting list of users
a.	/user/
4.	Getting all comments
a.	/comment/


POST API

1.	Adding a project
a.	/project/ 
2.	Adding user
a.	/user/ 
3.	Adding a new issue
a.	/issues/
4.	Adding a new comment
a.	/comment/

PUT API

1.	Modifying project details with id
a.	/project/<id>
2.	Modifying issues with id
a.	/issues/<id>


DELETE API

1.	Deleting a project with project id
a.	/project/<id>
2.	Deleting an issue with issue id
a.	/issues/<id>



API Structure for use

User api structure:

{
    "userName": "ramu",
    "email":"ramu@gmail.com",
    "phone":"65596"
}

Project api structure

{
    "projectName": "LY3000",
    "projectDescription":"Image is missing",
    "userId":"1"
}

Issue api structure:

{
    "issueName": "authentication needed",
    "issueType":"TASK",
    "projectId":"1",
    "assigneeId":"1",
    "reporterId":"2",
    "issueStatus":"1",
    "issueDescription":"Implement JWT authentication"
}

Comment api structure:

{
    "author": "Rashid",
    "authorId":"1",
    "issueId":"2",
    "text":"this is my comment",
    "createdOn":"2015, 10, 09, 23, 55, 59, 342380"
}


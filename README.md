**OnePTE**
Here, we design basic APIs and a database structure that supports a subset of the functionalities of OnePTE in a simplified form.


**Admin Credential:**
Username: remon
Password: asdf!@#$


**API Endpoints**

**Question List**
URL: /questions/
Method: GET
Description: Retrieves a list of all questions. You can filter questions by type (SST, RO, RMMCQ).

Query Parameters: 
  type (optional): Filter by question type (e.g., SST, RO, RMMCQ).


**Question Details**
URL: /questions/<id>/
Method: GET
Description: Retrieves details of a specific question by its ID.

Path Parameters:
id: The ID of the question.



**Submit Answer**
URL: /submit/
Method: POST
Description: Submit an answer for a question. The request body varies depending on the question type.



**Practice History**
URL: /history/
Method: GET
Description: Retrieves a user's practice history. You can filter by question type.

Query Parameters:
user_id (required): The ID of the user.
type (optional): Filter by question type (e.g., SST).






# OnePTE

This project is a simplified implementation of OnePTE, designed to provide basic APIs and a database structure that supports a subset of OnePTE's functionalities.

## Admin Credentials

- **Username**: remon
- **Password**: asdf!@#$

## API Testing with Postman

One can use Postman to test the functionality of the APIs. Follow the steps below:

### 1. Base URL

- The development server is assumed to be running at `http://127.0.0.1:8000/`.

### 2. Endpoints

#### List Questions

- **URL**: `GET /questions/`
- **Description**: Retrieves a list of all questions. You can filter by question type using a query parameter.
- **Example**: `GET http://127.0.0.1:8000/questions/?type=SST`

#### Question Details

- **URL**: `GET /questions/{id}/`
- **Description**: Retrieves details for a specific question by its ID.
- **Example**: `GET http://127.0.0.1:8000/questions/1/`

#### Submit Answer

- **URL**: `POST /submissions/`
- **Description**: Submits an answer for a specific question type.
- **Body**: Provide the `question_id` and your `answer` in the request body.
- **Example**:
    - **Content-Type**: `application/json`
    - **Request Body**:
      ```json
      {
        "question_id": 1,
        "answer": "This is a sample answer."
      }
      ```

#### Practice History

- **URL**: `GET /history/`
- **Description**: Retrieves the user's practice history with optional filtering by question type.
- **Example**: `GET http://127.0.0.1:8000/history/?type=SST`

### 3. Testing Steps in Postman

1. **Open Postman** and create a new request.
2. **Choose** the appropriate HTTP method (GET, POST) and enter the corresponding URL.
3. **Add** a JSON body under the "Body" tab if required.
4. **Send** the request.
5. **Check** the response to ensure that the API is working correctly.

## Admin Panel Usage

The Django admin panel allows you to manage your data easily.

### 1. Accessing the Admin Panel

- **URL**: `http://127.0.0.1:8000/admin/`
- **Login** using the superuser credentials provided above.

### 2. Managing Data

- **Add Data**: Click on the model name (e.g., `Questions`) and use the "Add" button to create new entries.
- **View Data**: Click on any existing data entry to view its details.
- **Edit Data**: Open any data entry, make changes, and save.
- **Delete Data**: Select one or more entries and use the "Delete" action.


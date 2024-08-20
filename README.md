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

- **URL**: `POST /submit/`
- **Description**: Submits an answer for a specific question type.

#### 1. **Summarize Spoken Text (SST)**
   - **Request**
     - **Method**: POST
     - **URL**: `http://127.0.0.1:8000/submit/`
     - **Headers**:
       - `Content-Type`: `application/json`
     - **Body**:
       ```json
       {
           "question": 1,
           "user_id": 101,
           "answer_text": "This is the summary of the spoken text."
       }
       ```

#### 2. **Re-Order Paragraph (RO)**
   - **Request**
     - **Method**: POST
     - **URL**: `http://127.0.0.1:8000/submit/`
     - **Headers**:
       - `Content-Type`: `application/json`
     - **Body**:
       ```json
       {
           "question": 2,
           "user_id": 101,
           "ordered_paragraphs": "3,1,2,4"
       }
       ```

#### 3. **Reading Multiple Choice (Multiple) (RMMCQ)**
   - **Request**
     - **Method**: POST
     - **URL**: `http://127.0.0.1:8000/submit/`
     - **Headers**:
       - `Content-Type`: `application/json`
     - **Body**:
       ```json
       {
           "question": 3,
           "user_id": 101,
           "selected_options": "1,3,4"
       }
       ```

#### Explanation:
- **question**: The ID of the question being answered.
- **user_id**: The ID of the user submitting the answer.
- **answer_text**: For SST questions, this is the text-based summary.
- **ordered_paragraphs**: For RO questions, this is a comma-separated string representing the order of paragraphs.
- **selected_options**: For RMMCQ questions, this is a comma-separated string of the selected options.

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


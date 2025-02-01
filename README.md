# FastAPI CRUD Application with MongoDB

Welcome to the **FastAPI CRUD Application**! This is a simple yet powerful API built with FastAPI, MongoDB, and Python. It allows you to perform CRUD (Create, Read, Update, Delete) operations on items stored in a MongoDB database.

## Features

- **Create**: Add new items to the database.
- **Read**: Get all items or search for an item by name.
- **Update**: Modify an existing item based on its name.
- **Delete**: Remove an item from the database by its name.

## Tech Stack

- **FastAPI**: FastAPI framework to build APIs quickly and efficiently.
- **MongoDB**: A NoSQL database to store items.
- **Python**: Backend programming language.
- **CORS Middleware**: Allowing cross-origin requests.

## Getting Started

### Prerequisites

- Python 3.x
- MongoDB running locally or through a cloud provider.
- Environment variables for MongoDB URL (stored in `.env` file).

### Clone the Repository

```bash
git clone https://github.com/Satyasuranjeet/CRUD_With_Fast_API.git
cd fastapi-crud-mongodb
```

### Install Dependencies

First, set up your environment:

```bash
pip install -r requirements.txt
```

### Set Up Environment Variables

Create a `.env` file in the root of your project and add your MongoDB connection URL:

```env
MONGO_URL=mongodb://your_mongo_connection_string
```

### Running the Application

To start the FastAPI application locally, use the following command:

```bash
uvicorn app:app --reload
```

Your app will be available at `http://127.0.0.1:8000`.

### Deployment

You can deploy this API to Vercel by simply creating a `vercel.json` file (shown below) and running the deployment command.

### API Endpoints

- **POST** `/item/` - Create a new item.
- **GET** `/item/` - Retrieve all items.
- **GET** `/item/name/{name}` - Retrieve an item by its name.
- **PUT** `/item/update` - Update an item by its name.
- **DELETE** `/item/{name}` - Delete an item by its name.

### Example

1. **Create Item**:

   ```bash
   POST /item/
   {
     "name": "Item1",
     "details": "Details of Item1",
     "price": 10.99
   }
   ```

2. **Get All Items**:

   ```bash
   GET /item/
   ```

3. **Get Item by Name**:

   ```bash
   GET /item/name/Item1
   ```

4. **Update Item**:

   ```bash
   PUT /item/update
   {
     "name": "Item1",
     "details": "Updated details of Item1",
     "price": 12.99
   }
   ```

5. **Delete Item**:

   ```bash
   DELETE /item/Item1
   ```

### Screenshot

Here is a screenshot of the application in action:

![FastAPI CRUD App Screenshot](https://i.ibb.co/4RXtDJDn/image.png)

## License

This project is open-source and available under the [MIT License](LICENSE).

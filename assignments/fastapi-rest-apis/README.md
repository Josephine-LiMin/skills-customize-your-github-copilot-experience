# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build RESTful APIs using the FastAPI framework. You will create endpoints to manage student extracurricular activities and validate request payloads.

**Skills practiced:** FastAPI, routing, path parameters, query parameters, request bodies, Pydantic validation

## 📝 Tasks

### 🛠️ Task 1: Initialize FastAPI App

#### Description
Create a basic FastAPI application instance and define a root route.

#### Requirements
Completed program should:
- Import `FastAPI` from `fastapi`
- Create an `app` instance of `FastAPI`
- Define a `@app.get("/")` route that returns a welcome message

### 🛠️ Task 2: CRUD Endpoints

#### Description
Define endpoints to retrieve and register new extracurricular activities.

#### Requirements
Completed program should:
- Define a `@app.get("/activities")` route to list all activities
- Define a `@app.post("/activities")` route to add a new activity using a Pydantic model for validation

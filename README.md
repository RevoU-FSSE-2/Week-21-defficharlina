# Twitter-like API using Flask
This project build a version of Twitter-like API using Flask includes of registration, posting tweets, following/unfollowing users, and retrieving user profiles.

## Flask
Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions.

## API Endpoints
### Registration
- **URL:** `/auth/registration`
- **Method:** `POST`
- **Request Body:**
  - `username` (string): The username.
  - `password` (string): The password.
  - `bio` (string): The short 'about me' summary.

### Example

  <p align="center">
    <img src="image/register.JPG" width="600">
  </p>

### Login
- **URL:** `/auth/login`
- **Method:** `POST`
- **Request Body:**
  - `username` (string): The username.
  - `password` (string): The password.

### Example

  <p align="center">
    <img src="image/login.JPG" width="600">
  </p>

  ### User Profile
- **URL:** `/user`
- **Method:** `GET`

### Example

  <p align="center">
    <img src="image/get user profile.JPG" width="600">
  </p>

  ### Post a Tweet
- **URL:** `/post/tweet`
- **Method:** `POST`
- **Request Body:**
  - `tweet` (string): The twitter message displayed on a user's profile page.

### Example

  <p align="center">
    <img src="image/post tweet.JPG" width="600">
  </p>

  ### Following
- **URL:** `/follow/id`
- **URL:** `/unfollow/id`
- **Method:** `POST`

### Example

  <p align="center">
    <img src="image/follow.JPG" width="600">
  </p>



  <p align="center">
    <img src="image/unfollow.JPG" width="600">
  </p>

## File .env
```sh
DATABASE_URL="postgresql://postgres:Deff1ch4rl1n4@db.nqvqyweykpusjmqbksug.supabase.co:5432/postgres"
SECRET_KEY="defficharlina"
```
  


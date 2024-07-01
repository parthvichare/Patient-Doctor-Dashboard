# Patient and Doctor Dashboard Application

## Overview

This project is a web application designed to provide separate dashboards for patients and doctors. It allows users to sign up, log in, and be redirected to their respective dashboards based on their user type (patient or doctor). The application ensures secure authentication and user management.

## Features

- **User Authentication**
  - Secure user signup and login
  - Password handling and storage
  - Redirection to respective dashboards upon successful login

- **User Profiles**
  - Additional information storage (profile picture, address, contact details)
  - Profiles linked to main user accounts

- **User Types**
  - Separate user types: Patients and Doctors
  - User type determined during signup
  - Redirection to appropriate dashboards based on user type

- **Dashboards**
  - Separate dashboards for patients and doctors
  - User-specific functionality and data display

## Technologies Used

- **Backend**
  - Django: High-level Python web framework
  - Django ORM: Database interactions and model definitions

- **Frontend**
  - HTML, CSS: User interface rendering
  - Django Templates: Dynamic HTML content generation

- **Database**
  - SQLite: Lightweight database for development and testing

- **User Management**
  - Django's built-in authentication system

## Models

1. **UserProfile**
   - Stores additional information for each user (profile picture, address, contact details)
   - Linked to the Django `User` model via a one-to-one relationship

2. **Patient**
   - Extends the `UserProfile` to include patient-specific fields
   - Linked to the `UserProfile` model via a one-to-one relationship

3. **Doctor**
   - Extends the `UserProfile` to include doctor-specific fields
   - Linked to the `UserProfile` model via a one-to-one relationship

## Forms

1. **SignUpForm**
   - Handles user registration and password confirmation

2. **UserProfileForm**
   - Manages additional user profile information

3. **PatientForm**
   - Handles patient-specific fields

4. **DoctorForm**
   - Handles doctor-specific fields

5. **LoginForm**
   - Manages user login credentials

## Views

1. **signup_view**
   - Handles user signup and profile creation
   - Redirects users to the appropriate dashboard based on user type

2. **login_view**
   - Manages user login and redirects to the appropriate dashboard

3. **patient_dashboard**
   - Renders the patient dashboard

4. **doctor_dashboard**
   - Renders the doctor dashboard

5. **profile_create_view**
   - Handles the creation and updating of user profiles

6. **logout_view**
   - Manages user logout and redirects to the login page

## Setup and Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/your-username/patient-doctor-dashboard.git
   cd patient-doctor-dashboard

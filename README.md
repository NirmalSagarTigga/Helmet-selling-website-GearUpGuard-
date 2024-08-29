GearUpGuard - A Django-based E-commerce Website
Welcome to Helmet Shop, a Django-based e-commerce platform dedicated to selling a wide variety of helmets. This project demonstrates how to build a fully functional online store using the Django web framework, complete with product listings, user authentication, shopping cart functionality, and order management.

Introduction
Helmet Shop is an online store built with Django, designed to sell helmets of various types and brands. The platform offers a user-friendly interface for customers to browse products, add them to their shopping cart, and complete purchases. It also includes an admin interface for managing products, orders, and user accounts.


Features
Product Management: Add, update, and delete helmet products, including images, descriptions, prices, and stock levels.
User Authentication: Sign up, log in, and manage user profiles.
Shopping Cart: Add, update, or remove products from the cart, and view the total price.
Order Management: Place orders, view order history, and receive order confirmation emails.
Admin Panel: Manage products, orders, and user accounts through Django's built-in admin interface.
Responsive Design: Mobile-friendly design for an optimal shopping experience on any device.

Technologies Used
Django: Backend framework for building a robust and scalable web application.
SQLite: Default database for development (can be switched to PostgreSQL, MySQL, etc., in production).
HTML/CSS/JavaScript: Frontend technologies for building the user interface.
Bootstrap: CSS framework for responsive design.

Installation
To run this project locally, follow these steps:

Clone the repository:
bash
Copy code
git clone https://github.com/yourusername/helmet-shop.git
cd helmet-shop
Create and activate a virtual environment:

bash
Copy code
python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Apply the database migrations:

bash
Copy code
python manage.py migrate
Create a superuser for the admin interface:

bash
Copy code
python manage.py createsuperuser
Run the development server:

bash
Copy code
python manage.py runserver
Open your web browser and go to http://127.0.0.1:8000/ to see the website.

Usage
Browse Products: Navigate through different helmet categories, view product details, and select desired items.
Add to Cart: Click on the "Add to Cart" button to include items in your shopping cart.
Checkout: View your cart and proceed to checkout to complete your purchase.
Admin Interface: Go to http://127.0.0.1:8000/admin/ and log in with your superuser account to manage the site.

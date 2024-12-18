# ecommerce
this is task from partnr
### This project contains basic part of eommerce website like CRUD operation on products, user authentication and Cart.

## How to run this project:
1. Setup a virtual environment in local ( follow this to setup https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/)
2. Clone this repo
3. Run `pip install -r requirements.txt`
4. Goto the project root folder
5. Run `python manage.py migrate`
6. Run `python manage.py runserver`

## API endpoints:
### Product API
1. Get all products: GET `http://127.0.0.1:8000/products/`
2. Add a new product: POST `http://127.0.0.1:8000/products/`
3. Get a specific product: GET `http://127.0.0.1:8000/products/product_id/`
4. Update a specific product: PUT `http://127.0.0.1:8000/products/product_id/`
5. Delete a product: DELETE `http://127.0.0.1:8000/products/product_id/`


### Cart API:
1. Get all cart items: GET `http://127.0.0.1:8000/api/user/cart/`
2. Add a new product to cart: POST `http://127.0.0.1:8000/api/user/cart/`


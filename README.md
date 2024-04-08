# Pizza-Restaurants
Below is a detailed README.md file template for this code challenge:

---

# Pizza Restaurants Code Challenge

Welcome to the Pizza Restaurants code challenge! This project is a Flask-based application that manages pizza restaurants and their menus. It allows users to view, add, and delete restaurants and pizzas.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Routes](#routes)
- [Models](#models)
- [Validation](#validation)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Installation

To run this application locally, follow these steps:

1. Clone the repository:

   git clone https://github.com/your-username/pizza-restaurants.git

2. Navigate into the project directory:
   cd pizza-restaurants


3. Create a virtual environment and activate it:
   python -m venv venv
   source venv/bin/activate  # for Linux/Mac
   venv\Scripts\activate  # for Windows


4. Install dependencies:

   pip install -r requirements.txt

5. Initialize the database:
   flask db init
   flask db migrate
   flask db upgrade

## Usage

To start the Flask development server, run:

flask run

By default, the server will run on http://127.0.0.1:5000.

## Routes

This application exposes the following routes:

- **GET /restaurants**: Returns a list of restaurants.
- **GET /restaurants/:id**: Returns details of a specific restaurant.
- **DELETE /restaurants/:id**: Deletes a restaurant.
- **GET /pizzas**: Returns a list of pizzas.
- **POST /restaurant_pizzas**: Adds a pizza to a restaurant's menu.

## Models

The application has three main models:

1. **Restaurant**: Represents a pizza restaurant.
2. **Pizza**: Represents a type of pizza available in restaurants.
3. **RestaurantPizza**: Represents a relationship between a restaurant and a pizza, including price information.

## Validation

The application performs validation on the following criteria:

- **Restaurant**: Name must be less than 50 characters and unique.
- **RestaurantPizza**: Price must be between 1 and 30.
- **Request Data**: All required fields (`price`, `pizza_id`, `restaurant_id`) must be provided.


## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).




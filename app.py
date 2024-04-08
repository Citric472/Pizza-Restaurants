from flask import Flask, jsonify, request
from flask_migrate import Migrate
from faker import Faker
from config import Config
from models import db, Restaurant, Pizza, RestaurantPizza

app = Flask(__name__)
app.config.from_object(Config)
fake = Faker()

migrate = Migrate(app, db)
db.init_app(app)

@app.route('/')
def index():
    # Generate a list of fake company names
    return "Welcome to Pizza Restaurants!"

@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    formatted_restaurants = []
    for restaurant in restaurants:
        formatted_restaurant = {
            'id': restaurant.id,
            'name': restaurant.name,
            'address': restaurant.address
        }
        formatted_restaurants.append(formatted_restaurant)
    return jsonify(formatted_restaurants)

@app.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    try:
        restaurant = Restaurant.query.get_or_404(id)
        pizzas = [{'id': rp.pizza.id, 'name': rp.pizza.name, 'ingredients': rp.pizza.ingredients} for rp in restaurant.restaurant_pizzas]
        return jsonify({'id': restaurant.id, 'name': restaurant.name, 'address': restaurant.address, 'pizzas': pizzas})
    except Exception as e:
        error_message = {'error': 'Restaurant not found'}
        return jsonify(error_message), 404

@app.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get_or_404(id, description="Restaurant not found")
    db.session.delete(restaurant)
    db.session.commit()
    return '', 204

@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    return jsonify([{'id': p.id, 'name': p.name, 'ingredients': p.ingredients} for p in pizzas])

@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    price = data.get('price')
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')

    # Validate request data
    if not all([price, pizza_id, restaurant_id]):
        return jsonify({'errors': ['price, pizza_id, and restaurant_id are required']}), 400

    # Validate price range
    if not (1 <= price <= 30):
        return jsonify({'errors': ['Price must be between 1 and 30']}), 400

    restaurant = Restaurant.query.get(restaurant_id)
    if not restaurant:
        return jsonify({'errors': ['Restaurant not found']}), 404

    pizza = Pizza.query.get(pizza_id)
    if not pizza:
        return jsonify({'errors': ['Pizza not found']}), 404

    restaurant_pizza = RestaurantPizza(price=price, restaurant_id=restaurant_id, pizza_id=pizza_id)
    db.session.add(restaurant_pizza)
    db.session.commit()

    # Return the ID of the newly created RestaurantPizza
    return jsonify({'id': restaurant_pizza.id}), 201

if __name__ == '__main__':
    app.run(debug=True)

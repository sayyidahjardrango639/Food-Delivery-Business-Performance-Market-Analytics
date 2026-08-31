--- Queries 1 : Find total Revenue --- 

SELECT SUM(order_value) FROM food_delivery;

--- Queries 2 : Find total Customers ---

SELECT COUNT(customer_id) FROM food_delivery;

--- Queries 3 : Find average Order Value ---

SELECT AVG(order_value) FROM food_delivery;

--- Queries 4 : City wise Revenue ---

SELECT city, order_value FROM food_delivery ORDER BY order_value;

--- Queries 5 : Find highest value orders ---

SELECT MAX(order_value) FROM food_delivery;

--- Queries 6 : Find Category wise Revenue ---

SELECT restaurant_category, order_value FROM food_delivery ORDER BY order_value;

--- Queries 7 : Find Top Performing cities

SELECT city, SUM(order_value) FROM food_delivery GROUP BY city;

--- Queries 8 : Find average Delivery Time by City ---

SELECT city, AVG(delivery_time) FROM food_delivery GROUP BY city;

--- Queries 9 : Find average Rating by Restaurant Category ---

SELECT restaurant_category, AVG(customer_rating) FROM food_delivery GROUP BY restaurant_category;

--- Queries 10 : Identify high value Customers ---
SELECT customer_id, SUM(order_value) FROM food_delivery GROUP BY customer_id;

--- Queries 11 : Find Monthly Revenue ---

SELECT MONTHNAME(order_date) AS month, SUM(order_value) AS monthly_revenue FROM food_delivery GROUP BY MONTH(order_date), MONTHNAME(order_date) ORDER BY MONTH(order_date);







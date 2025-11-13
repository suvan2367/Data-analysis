CREATE DATABASE online_sales;
USE online_sales;

CREATE TABLE online_sales.orders (
    order_id INT PRIMARY KEY,
    order_date DATE,
    amount DECIMAL(10, 2),
    product_id VARCHAR(10)
);

-- Insert sample data
INSERT INTO online_sales.orders (order_id, order_date, amount, product_id) VALUES
(1001, '2024-01-05', 120.00, 'P001'),
(1002, '2024-01-15', 250.00, 'P002'),
(1003, '2024-02-02', 80.00, 'P003'),
(1004, '2024-02-20', 150.00, 'P001'),
(1005, '2024-03-05', 200.00, 'P004'),
(1006, '2024-03-10', 300.00, 'P002'),
(1007, '2024-03-25', 180.00, 'P005'),
(1008, '2024-04-02', 90.00, 'P003'),
(1009, '2024-04-10', 170.00, 'P006'),
(1010, '2024-04-18', 220.00, 'P001');

-- Monthly Sales Trend Analysis in MySQL
SELECT 
    YEAR(order_date) AS year,
    MONTH(order_date) AS month,
    SUM(amount) AS total_revenue,
    COUNT(DISTINCT order_id) AS total_orders
FROM 
    online_sales.orders
GROUP BY 
    YEAR(order_date), MONTH(order_date)
ORDER BY 
    year, month;

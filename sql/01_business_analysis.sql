-- =====================================================
-- E-Commerce Sales Analytics
-- SQL Business Analysis
-- =====================================================


-- 1. Overall Business KPIs
SELECT
    COUNT(*) AS total_products,
    SUM(stock) AS total_stock,
    ROUND(AVG(price), 2) AS average_price,
    ROUND(AVG(rating), 2) AS average_rating,
    ROUND(AVG(discountPercentage), 2) AS average_discount
FROM products;


-- 2. Category Performance
SELECT
    category,
    COUNT(*) AS total_products,
    SUM(stock) AS total_stock,
    ROUND(AVG(price), 2) AS average_price,
    ROUND(AVG(rating), 2) AS average_rating,
    ROUND(AVG(discountPercentage), 2) AS average_discount
FROM products
GROUP BY category
ORDER BY total_products DESC;


-- 3. High Discount Products
SELECT
    title,
    category,
    price,
    discountPercentage
FROM products
WHERE discountPercentage >= 20
ORDER BY discountPercentage DESC;


-- 4. Low Stock Products
SELECT
    title,
    category,
    stock
FROM products
WHERE stock < 20
ORDER BY stock ASC;


-- 5. Highly Rated Products
SELECT
    title,
    category,
    rating
FROM products
WHERE rating >= 4
ORDER BY rating DESC;


-- 6. Availability Summary
SELECT
    availabilityStatus,
    COUNT(*) AS total_products
FROM products
GROUP BY availabilityStatus
ORDER BY total_products DESC;
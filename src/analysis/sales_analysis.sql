
-- 1. Overall Product KPIs
SELECT
    COUNT(*) AS total_products,
    SUM(stock) AS total_stock,
    ROUND(AVG(price), 2) AS average_price,
    ROUND(AVG(rating), 2) AS average_rating
FROM public.products_transformed;


-- 2. Category-wise Product Analysis
SELECT
    category,
    COUNT(*) AS total_products,
    ROUND(AVG(price), 2) AS average_price,
    SUM(stock) AS total_stock
FROM public.products_transformed
GROUP BY category
ORDER BY total_products DESC;


-- 3. Identify Low-Stock Products
SELECT
    id,
    title,
    category,
    stock,
    price
FROM public.products_transformed
WHERE stock < 50
ORDER BY stock ASC;


-- 4. Category-wise Low-Stock Analysis
SELECT
    category,
    COUNT(*) AS low_stock_products,
    SUM(stock) AS remaining_stock
FROM public.products_transformed
WHERE stock < 50
GROUP BY category
ORDER BY low_stock_products DESC;


-- 5. Low-Stock Percentage
SELECT
    COUNT(*) AS total_products,
    COUNT(*) FILTER (WHERE stock < 50) AS low_stock_products,
    ROUND(
        100.0 * COUNT(*) FILTER (WHERE stock < 50)
        / NULLIF(COUNT(*), 0),
        2
    ) AS low_stock_percentage
FROM public.products_transformed;

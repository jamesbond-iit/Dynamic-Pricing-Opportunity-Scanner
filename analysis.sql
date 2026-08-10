SELECT COUNT(*) transactions,SUM(units_sold) units_sold,ROUND(SUM(revenue),2) revenue,ROUND(SUM(gross_profit),2) gross_profit,ROUND(AVG(margin_pct),2) avg_margin_pct FROM pricing_sales;

SELECT category,SUM(units_sold) units,ROUND(SUM(revenue),2) revenue,ROUND(SUM(gross_profit),2) gross_profit,ROUND(AVG(margin_pct),2) avg_margin_pct,ROUND(AVG(baseline_elasticity),3) avg_elasticity FROM pricing_sales GROUP BY category ORDER BY revenue DESC;

SELECT product_id,category,ROUND(AVG(listed_price),2) avg_price,ROUND(AVG(competitor_price),2) avg_competitor_price,ROUND(AVG(price_gap_pct),2) avg_gap_pct,ROUND(AVG(margin_pct),2) avg_margin_pct FROM pricing_sales GROUP BY product_id,category HAVING AVG(price_gap_pct)<-5 ORDER BY avg_gap_pct;

WITH monthly AS (SELECT year_month,category,product_id,SUM(revenue) revenue FROM pricing_sales GROUP BY year_month,category,product_id) SELECT *,RANK() OVER(PARTITION BY year_month,category ORDER BY revenue DESC) category_rank FROM monthly ORDER BY year_month,category_rank;

SELECT customer_segment,ROUND(AVG(discount_pct),2) avg_discount_pct,ROUND(SUM(revenue),2) revenue,ROUND(AVG(margin_pct),2) avg_margin_pct FROM pricing_sales GROUP BY customer_segment ORDER BY revenue DESC;
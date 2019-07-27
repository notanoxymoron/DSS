## 3. The With Clause ##

WITH playlist_info AS
    (
     SELECT
        p.playlist_id,
        p.name playlist_name,
        t.name,
        (t.milliseconds / 1000) seconds  
        
     FROM playlist p    
     LEFT JOIN playlist_track pt ON pt.playlist_id = p.playlist_id
     LEFT JOIN track t ON t.track_id = pt.track_id
    )
        
SELECT 
    playlist_id, 
    playlist_name, 
    COUNT(name) number_of_tracks, 
    SUM(seconds) length_seconds

FROM playlist_info
GROUP BY playlist_id
ORDER BY playlist_id

## 4. Creating Views ##

CREATE VIEW chinook.customer_gt_90_dollars AS
    SELECT
        c.*
    FROM chinook.invoice i
    INNER JOIN chinook.customer c ON i.customer_id = c.customer_id
    GROUP BY 1
    HAVING SUM(i.total) > 90;

SELECT * FROM chinook.customer_gt_90_dollars;

## 5. Combining Rows With Union ##

SELECT * from customer_usa

UNION

SELECT * from customer_gt_90_dollars


    

## 6. Combining Rows Using Intersect and Except ##

with customer_info AS
    (
     SELECT * from customer_usa
     
     INTERSECT

     SELECT * from customer_gt_90_dollars    
    )

SELECT 
    e.first_name||" "||e.last_name employee_name,
    count(c.customer_id) customers_usa_gt_90
FROM employee e
LEFT JOIN customer_info c ON c.support_rep_id=e.employee_id
WHERE e.title is "Sales Support Agent"
GROUP BY 1
ORDER BY 1

## 7. Multiple Named Subqueries ##

WITH 
    India AS
        (
         SELECT * FROM customer 
         where country is 'India'    
        ),
    
    India_total AS
        (
         SELECT 
            *,
            SUM(i.total) totalsum 
         FROM India ia
         INNER JOIN invoice i ON i.customer_id=ia.customer_id
         GROUP BY i.customer_id
        )

SELECT 
    first_name||" "||last_name customer_name,
    totalsum total_purchases
FROM India_total 
ORDER BY customer_name

## 8. Challenge: Each Countrys Best Customer ##

SELECT
    country,
    first_name||" "||last_name customer_name,   
    MAX(i.totalsum) total_purchased
FROM customer c
INNER JOIN (
            SELECT 
                SUM(total) totalsum,
                customer_id
            FROM invoice
            GROUP BY customer_id
           ) i on i.customer_id=c.customer_id 
GROUP BY 1
ORDER BY 1
    
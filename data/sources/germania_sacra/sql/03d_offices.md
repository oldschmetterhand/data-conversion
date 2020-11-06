
## Offices table


### bezeichnung - column

```SQL

SELECT 
	bezeichnung,
    COUNT(*) AS grouped_count
FROM 
	offices
GROUP BY
	bezeichnung
ORDER BY
	grouped_count
DESC;
-- Kanoniker, Mönch, Vikar assigned by far most often


```
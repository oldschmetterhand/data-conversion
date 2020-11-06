

# GSN table


## deleted - column

```SQL

SELECT 
	deleted,
    COUNT(*) AS grouped_count,
    (SELECT COUNT(*) FROM gsn) AS total_gsn_count
FROM
	gsn
GROUP BY
	deleted
ORDER BY 
	grouped_count
DESC;
-- no gsn deleted 

```


## item_id - column

```SQL

SELECT 
	item_id,
  COUNT(*) AS grouped_count,
  (SELECT COUNT(*) FROM gsn) AS total_gsn_count
FROM
	gsn
GROUP BY
	item_id
ORDER BY 
	grouped_count
DESC;
-- all have item_id assigned.
-- 57 unique item ids assigned.

```


## item_mergedinto_id column

```SQL

SELECT 
  item_mergedinto_id,
  COUNT(*) AS grouped_count,
  (SELECT COUNT(*) FROM gsn) AS total_gsn_count
FROM
	gsn
GROUP BY
	item_mergedinto_id
ORDER BY 
	grouped_count
DESC;
-- only null


```


## nummer

```SQL

SELECT 
  nummer,
  COUNT(*) AS grouped_count,
  (SELECT COUNT(*) FROM gsn) AS total_gsn_count
FROM
	gsn
GROUP BY
	nummer
ORDER BY 
	grouped_count
DESC;

-- only unique numbers
-- 62 results




```
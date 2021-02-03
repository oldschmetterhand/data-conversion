
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


### Count weltliche offices 

```SQL

SELECT 
	COUNT(*)
FROM
	gs_datenbank.offices
WHERE
	art != 'geistlich'
-- 2306 are weltlich
-- 65827 are geistlich


```


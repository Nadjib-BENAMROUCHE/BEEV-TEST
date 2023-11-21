-- a - We want to find the total number of cars by model by country

SELECT "Country", "Model", SUM("Sales Volume") as "TotalCars"
FROM consumer
GROUP BY "Country", "Model"
ORDER BY "TotalCars";

-- b - We want to know which country has the most of each model

WITH RankedModels AS (
  SELECT
    "Country",
    "Model",
    SUM("Sales Volume") AS "TotalCars",
    RANK() OVER (PARTITION BY "Model" ORDER BY SUM("Sales Volume") DESC) AS "Rank"
  FROM
    consumer
  GROUP BY
    "Country", "Model"
)
SELECT
  "Country",
  "Model",
  "TotalCars"
FROM
  RankedModels
WHERE
  "Rank" = 1;

-- c - We want to know if any model is sold in the USA but not in France.

SELECT DISTINCT "Model"
FROM consumer
WHERE "Country" = 'USA'
  AND "Model" NOT IN (SELECT DISTINCT "Model" FROM consumer WHERE "Country" = 'France');

/* SELECT "Model"
FROM consumer
WHERE "Country" = 'USA'
EXCEPT
SELECT "Model"
FROM consumer
WHERE "Country" = 'France';
*/ 

-- d - We want to know how much the average car costs in every country by engine type. (rapport.pdf)

SELECT c."Country", cr."Engine Type", ROUND(AVG(cr."Price"), 2) AS "AveragePrice"
FROM consumer c
JOIN car cr ON c."Model" = cr."Model"
GROUP BY c."Country", cr."Engine Type";

-- e - We want to know the average ratings of electric cars vs thermal cars

SELECT c."Engine Type", ROUND(AVG(CAST(co."Review Score" AS DECIMAL(10, 3))), 3) AS "AverageRating"
FROM car c
JOIN consumer co ON c."Model" = co."Model"
GROUP BY c."Engine Type";
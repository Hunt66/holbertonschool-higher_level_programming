-- shows the number of people who have certain scores in second_table
SELECT score, count(*) AS number FROM second_table GROUP BY score ORDER BY score DESC

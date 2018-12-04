-- shows the number of people who have certain scores in second_table
SELECT score, cout(score) AS number FROM second_table GROUP BY score ORDER BY score DESC

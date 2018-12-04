-- ranks all people in the second_table with name and score by score
SELECT score, name FROM second_table WHERE name IS NOT null ORDER BY score DESC

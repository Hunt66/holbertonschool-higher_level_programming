-- Lists all genres and displays the number of shows linked to each
SELECT x.name AS genre, count(y.genre_id) AS number_of_shows FROM tv_genres x
JOIN tv_show_genres y ON x.id = y.genre_id GROUP BY y.genre_id ORDER BY
number_of_shows DESC

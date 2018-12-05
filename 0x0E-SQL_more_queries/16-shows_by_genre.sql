-- lists all shows and genres linked to that show from the database
SELECT x.title, z.name FROM tv_shows x LEFT JOIN tv_show_genres y ON
x.id = y.show_id LEFT JOIN tv_genres z ON y.genre_id = z.id ORDER BY x.title
ASC, z.name ASC

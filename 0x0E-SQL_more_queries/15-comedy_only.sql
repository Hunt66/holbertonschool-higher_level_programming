-- Lists all Comedy shows in hbtn_0d_tvshows
SELECT x.title FROM tv_shows x JOIN tv_show_genres y ON x.id = y.show_id JOIN
tv_genres z ON y.genre_id = z.id WHERE z.name = "Comedy" ORDER BY x.title ASC

-- lists all genres of show Dexter from hbtn_0d_tvshows
SELECT x.name FROM tv_genres x JOIN tv_show_genres y ON x.id = y.genre_id
JOIN tv_shows z ON z.id = y.show_id WHERE z.title = "Dexter" ORDER BY x.name
ASC

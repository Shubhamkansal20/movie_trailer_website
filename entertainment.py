

import fresh_tomatoes

# import fresh_tomatoes from library

import media

# import class

# first object created

Bahubali = media.Movies('Bahubali', 'The ancient kingdom of Mahishmati'
                        ,
                        'https://i.ytimg.com/vi/JS4drCVGIms/maxresdefault.jpg'
                        , 'https://www.youtube.com/watch?v=sw6VKIClRMY')

# second object created

Don = media.Movies('DON',
                   'Don 2 is a 2011 Indian action crime thriller film co-written and directed by Farhan Akhtar.'
                   ,
                   'https://upload.wikimedia.org/wikipedia/en/d/d2/Don_2_poster.jpg'
                   , 'https://www.youtube.com/watch?v=_cJRiAfr2PE')

# third object created

Padmavat = media.Movies('PADMAVAT',
                        'Padmavat (or Padmawat) is an epic poem written in 1540 by Sufi poet Malik Muhammad Jayasi'
                        ,
                        'https://upload.wikimedia.org/wikipedia/en/7/73/Padmaavat_poster.jpg'
                        , 'https://www.youtube.com/watch?v=8YaF2m7hCx0')

# making array of objects

movie = [Bahubali, Don, Padmavat]

# passing objects to fresh_tomatoes

fresh_tomatoes.open_movies_page(movie)


			

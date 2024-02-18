movies = {'Stutter Island':0,'Information':0,'Captain Miller':0,'The alcatraz redemption':0,'The pink mile':0}
list_rating = []
while True:
    title = input('Enter movie title')
    rating = float(input('Enter movie rating'))

    list_rating.append(rating)
    movies[title] = sum(list_rating)/len(list_rating)
    x = int(input('Enter 0 to exit, 1 to continue'))
    if x == 0:
        break


print(movies)

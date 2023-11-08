a_list = [4444, 8897, 9896, 4835, 4324, 10, 6445, 661, 1246, 1000, 7429, 1376, 8121,
            647, 1280, 3993, 4881, 9500, 6701, 1199, 6251, 4432]
ratings = ['4+', '4+', '4+', '9+', '12+', '12+', '17+', '17+']
content_ratings = {}
for rating in ratings:
    if rating in content_ratings:
        content_ratings[rating] += 1
    else:
        content_ratings[rating] = 1
print(content_ratings)            
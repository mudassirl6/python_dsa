def friendship_timeline(friends_added, friends_removed):
    
    friendships = []

    i = 0
    while i < len(friends_added):
        dict1 = friends_added[i]
        for j in range(len(friends_removed)):
            temp_dict = friends_removed[j]

            if dict1['user_ids'][0] == temp_dict['user_ids'][1] and dict1['user_ids'][1] == temp_dict['user_ids'][0]:
               templist = sorted(dict1['user_ids'])
               friendships.append({'user_id':templist,'start_date':dict1['created_at'],'end_date':temp_dict['created_at']})
               




        
        i += 1


    return friendships


friends_added = [
    {'user_ids': [1, 2], 'created_at': '2020-01-01'},
    {'user_ids': [3, 2], 'created_at': '2020-01-02'},
    {'user_ids': [2, 1], 'created_at': '2020-02-02'},
    {'user_ids': [4, 1], 'created_at': '2020-02-02'}]

friends_removed = [
    {'user_ids': [2, 1], 'created_at': '2020-01-03'},
    {'user_ids': [2, 3], 'created_at': '2020-01-05'},
    {'user_ids': [1, 2], 'created_at': '2020-02-05'}]

print(friendship_timeline(friends_added,friends_removed))
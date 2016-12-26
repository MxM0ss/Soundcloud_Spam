import soundcloud
client = soundcloud.Client(client_id='fDoItMDbsbZz8dY16ZzARCZmzgHBPotA')
user = client.get('/resolve', url='http://soundcloud.com/yungoffline')
tracks = client.get('/users/' +str(user.id) + '/tracks')
spam_count = 0
total_comments = 0
total_tracks = 0
for track in tracks:
    total_tracks += 1
    comments = (client.get('/tracks/' + str(track.id) + '/comments'))
    for comment in comments:
        total_comments += 1
        if 'goo.gl' in comment.body or 'music contest' in comment.body:
            spam_count += 1
            print ('Track: ' + track.title)
            print()
            print ('Comment: '+ comment.body)
            print()

print('Out of ' + str(total_tracks) + ' tracks,')
print('There were ' + str(spam_count) + ' spam comments')
percent_spam = spam_count/total_comments * 100
print("{0:.2f}% spam".format(percent_spam))
alient_0 = {'color': 'green', 'points': '5'}
print(alient_0['color'])
print(alient_0['points'])

alients = [{'color': 'green', 'points': '5'},\
            {'color': 'yellow', 'points': '10'},\
            {'color': 'red', 'points': '15'}]

shooted_alien = 'yellow'

for alient in alients:
    if alient['color'] == shooted_alien:
        print(f"You just earned {alient['points']} points!")


shooted_alien = 'red'
for i in range(0,len(alients)):
    if alients[i]['color'] == shooted_alien:
        print(f"You just earned {alient['points']} points!")



alient_0['x_position'] = 0
alient_0['y_position'] = 25
print(alient_0)


alient_0 = {}
alient_0['color'] = 'red'
alient_0['points'] = 15
print(alient_0)


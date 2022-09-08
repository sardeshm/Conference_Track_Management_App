from operator import itemgetter
import pandas as pd

def assign_time_slot():
    Test_input = [('Writing Fast Tests Against Enterprise Rails', 60), ('Overdoing it in Python',45), ('Lua for the Masses', 30), ('Ruby Errors from Mismatched Gem Versions', 45), ('Common Ruby Errors', 45), ('Rails for Python Developers' , 5), ('Communicating Over Distance', 60), ('Accounting-Driven Development',45), ('Woah', 30), ('Sit Down and Write',30), ('Pair Programming vs Noise',45), ('Rails Magic', 60), ('Ruby on Rails: Why We Should Move On',60), ('Clojure Ate Scala (on my project)',45), ('Programming in the Boondocks of Seattle',30), ('Ruby vs. Clojure for Back-End Development',30), ('Ruby on Rails Legacy App Maintenance', 60), ('A World Without HackerNews', 30), ('User Interface CSS in Rails Apps', 30)]
    data = sorted(Test_input, key = itemgetter(1))
    input_duration= ([x[1] for x in data])
    input_title= (([x[0] for x in data]))
    track1_from=[pd.Timestamp('09:00:00'),pd.Timestamp('10:00:00'), pd.Timestamp('10:45:00'), pd.Timestamp('11:15:00'), pd.Timestamp('12:00:00'), pd.Timestamp('13:00:00'), pd.Timestamp('14:00:00'), pd.Timestamp('14:45:00'), pd.Timestamp('15:30:00'), pd.Timestamp('16:00:00'), pd.Timestamp('16:30:00'), pd.Timestamp('17:00:00')]
    track1_to=[pd.Timestamp('10:00:00'), pd.Timestamp('10:45:00'), pd.Timestamp('11:15:00'), pd.Timestamp('12:00:00'), pd.Timestamp('13:00:00'), pd.Timestamp('14:00:00'), pd.Timestamp('14:45:00'), pd.Timestamp('15:30:00'), pd.Timestamp('16:00:00'), pd.Timestamp('16:30:00'), pd.Timestamp('17:00:00'), pd.Timestamp('18:00:00')]
    track2_from=[pd.Timestamp('09:00:00'), pd.Timestamp('10:00:00'), pd.Timestamp('11:00:00'), pd.Timestamp('11:30:00'), pd.Timestamp('12:00:00'),pd.Timestamp('13:00:00'), pd.Timestamp('13:45:00'), pd.Timestamp('14:30:00'), pd.Timestamp('15:00:00'), pd.Timestamp('16:00:00'), pd.Timestamp('16:05:00'), pd.Timestamp('17:00:00')]
    track2_to=[pd.Timestamp('10:00:00'), pd.Timestamp('11:00:00'), pd.Timestamp('11:30:00'), pd.Timestamp('12:00:00'),pd.Timestamp('13:00:00'), pd.Timestamp('13:45:00'), pd.Timestamp('14:30:00'), pd.Timestamp('15:00:00'), pd.Timestamp('16:00:00'), pd.Timestamp('16:05:00'), pd.Timestamp('17:00:00'), pd.Timestamp('18:00:00')]
    track1 = pd.DataFrame(columns=['track_from'], data= track1_from)
    track1['track_to']=track1_to
    track1['duration']=(track1.track_to - track1.track_from).astype('timedelta64[m]')
    track2 = pd.DataFrame(columns=['track_from'], data= track2_from)
    track2['track_to']=track2_to
    track2['duration']=(track2.track_to - track2.track_from).astype('timedelta64[m]')
    track1['Track']=1
    track2['Track']=2
    track_timeslot=(track1.merge(track2, how='outer'))
    stationary=['Lunch', 'Lunch', 'Break', 'Networking event', 'Networking event' ]
    schdule = track_timeslot.iloc[[4,16, 22, 11, 23],:]
    schdule['Title']= stationary
    track_timeslot=track_timeslot.drop([4,16, 22, 11, 23], axis=0)
    for (Duration, Title) in zip(input_duration, input_title):
        timeslot_ix=(track_timeslot.loc[track_timeslot['duration']== Duration]).index.values.tolist()
        timeslot=track_timeslot.loc[track_timeslot['duration']== Duration]
        timeslot=timeslot[:1]
        timeslot['Title']= Title
        schdule=schdule.append(timeslot)
        track_timeslot=track_timeslot.drop([timeslot_ix[0]], axis=0)
    return schdule

assign_time_slot()
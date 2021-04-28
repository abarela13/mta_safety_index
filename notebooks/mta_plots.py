import seaborn as sns

def hourlyLinePlots(data, station):
    filtered_station = data[data.STATION == station]

    filtered_station_weekdays_df = filtered_station[filtered_station.DAYTYPE == 'WEEKDAY']
    filtered_station_weekdays_df = filtered_station_weekdays_df.groupby(['DATE', 'TIMEOFDAY', 'WEEKDAY'], as_index=False).TRAFFIC.sum().sort_values('TRAFFIC', ascending=False)
    filtered_station_weekdays_df = filtered_station_weekdays_df.groupby(['TIMEOFDAY'], as_index=False).TRAFFIC.mean().sort_values('TRAFFIC', ascending=False)

    filtered_station_weekends_df = filtered_station[filtered_station.DAYTYPE == 'WEEKEND']
    filtered_station_weekends_df = filtered_station_weekends_df.groupby(['DATE', 'TIMEOFDAY', 'WEEKDAY'], as_index=False).TRAFFIC.sum().sort_values('TRAFFIC', ascending=False)
    filtered_station_weekends_df = filtered_station_weekends_df.groupby(['TIMEOFDAY'], as_index=False).TRAFFIC.mean().sort_values('TRAFFIC', ascending=False)

    ax = sns.lineplot(x='TIMEOFDAY', y='TRAFFIC', data=filtered_station_weekdays_df, label='weekday')
    ax = sns.lineplot(x='TIMEOFDAY', y='TRAFFIC', data=filtered_station_weekends_df, label='weekend')
    ax.set_title(f'{station} station')
    ax.set_xlabel('Time of Day')
    ax.set_ylabel('Traffic')
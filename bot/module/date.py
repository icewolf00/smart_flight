import datetime

class Date:
    def date_format(date):
        time = datetime.datetime.now()
        date_copy = date
        date_new = ''
        for row in date:
            if row.isnumeric():
                date_new = date_new + row
            else:
                pass
        #print(date_new)
        year = date_new[:4]
        month = ''
        date = ''
        if len(date_new) == 6:
            month = date_new[4:5]
            date = date_new[5:6]
        elif len(date_new) == 7:
            date_copy = date_copy[4:]
            for row in range(len(date_copy)):
                if date_copy[row].isnumeric():
                    month = month + date_copy[row]
                else:
                    if month != '':
                        for row2 in range(row+1, len(date_copy)):
                            if date_copy[row2].isnumeric():
                                date = date + date_copy[row2]
                        break  
        elif len(date_new) == 8:
            month = date_new[4:6]
            date = date_new[6:8]
        elif len(date_new) == 4:
            year = '2017'
            month = date_new[:2]
            date = date_new[2:]
            if (int(month) < time.month) or (int(month) == time.month and int(date) < time.day):
                year = '2018'
        elif len(date_new) == 3:
            year = '2017'
            for row in range(len(date_copy)):
                if date_copy[row].isnumeric():
                    month = month + date_copy[row]
                else:
                    for row2 in range(row+1, len(date_copy)):
                        if date_copy[row2].isnumeric():
                            date = date + date_copy[row2]
                    break
            if (int(month) < time.month) or (int(month) == time.month and int(date) < time.day):
                year = '2018' 
        elif len(date_new) == 2:
            year = '2017'
            month = date_new[:1]
            date = date_new[1:]
            if (int(month) < time.month) or (int(month) == time.month and int(date) < time.day):
                year = '2018'
        elif len(date_new) == 0:
            year = time.year
            month = time.month
            date = time.day
        else:
            year = '2018'
            month = '1'
            date = '1'
        data = '%s-%s-%s' % (year, month, date)
        print(data)
        return(data)

age = int(input('enter your age in years: '))
months = age * 12
days = 365 * age
minutes = 525600 * age
seconds = 31536000 * age
print('you are aprroximately ' + str(months) + ' moths old, or ' + str(days) + ' days old, or ' + str(minutes) + ' minutes old, or ' + str(seconds) + ' seconds old.')

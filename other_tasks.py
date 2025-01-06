# https://www.youtube.com/watch?v=fbBIR8zDySE&ab_channel=%D0%92%D0%B8%D0%B2%D1%87%D0%B0%D1%94%D0%BC%D0%BEPython%D1%80%D0%B0%D0%B7%D0%BE%D0%BC%2C%D1%83%D1%80%D0%BE%D0%BA%D0%B8python

# snail
# A snail climbs a well 3 feet during the day, and during night, 
# it slips 2 feet. If the well is 30 feet deep, how long will it take for the snail to climb?
# answer: 28

# well_height=float(input('enter the height of well, ft: '))
# snail_progress_per_day=float(input('enter the snail moved up, ft: '))
# snail_regress_per_night=float(input('enter the snail moved down, ft: '))

def get_days_to_reach_the_point(well_height,snail_progress_per_day,snail_regress_per_night):
  current_point=0.0
  day=0.0
  while(True):
    current_point+=snail_progress_per_day
    if (current_point)>=well_height:
      return round(day+((well_height-(current_point-snail_progress_per_day))/snail_progress_per_day)/2,2)
    else:
      current_point-=snail_regress_per_night
      day+=1


# print(get_days_to_reach_the_point(well_height,snail_progress_per_day,snail_regress_per_night))

# =================================================================================================================
# If sum of 3 digits === 20 --> ticket is lucky

abc=int(input('enter a real number of 3 digits: '))

def get_sum_of_digits(abc):
  a=abc//100
  bc=abc-a*100
  b=bc//10
  c=abc-(a*100+b*10)
  rez=a+b+c
  if (rez==20):
    print('your ticket is lucky!')
  return rez

print(get_sum_of_digits(abc))

# =================================================================================================================
# =================================================================================================================
# =================================================================================================================
# =================================================================================================================
# =================================================================================================================
# =================================================================================================================
# =================================================================================================================
# =================================================================================================================
# =================================================================================================================
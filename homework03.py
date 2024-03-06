import datetime
from datetime import datetime
def get_days_from_today(date):
    try:
          current_datetime = datetime.today().date()
          #current_date=current_datetime.date()
          certain_datetime=datetime.strptime(date,"%Y-%m-%d")
          certain_date = certain_datetime.date()
          amount_days = current_datetime - certain_date
          return amount_days.days
    except ValueError:
          return f"Please, enter the right date in format YYYY-MM-DD "
print(get_days_from_today("2000-04-06"))
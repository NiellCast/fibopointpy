from datetime import date, timedelta


class Date:
	def __init__(self) -> None:
		self._date = date.today()
		
	def get_start_date(self, days: int) -> str:
		"""
		param days: Get the number of days to subtract and calculate date - days.
		:return: Returns the previous day's date in string format (day/month/year).
		"""

		days_to_subtract = timedelta(days=days)

		start_date = self._date - days_to_subtract
		start_date = start_date.strftime('%d/%m/%Y')
		
		return start_date
		
	def get_current_date(self) -> str:
		"""
		:return: Returns the current date in string type (day/month/year).
		"""
		return self._date.strftime('%d/%m/%Y')

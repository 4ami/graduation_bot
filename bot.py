from datetime import date

class Tweet:
    def __init__(self)->None:
        self.message_len = 30
        self.date = date.today()
        self.grad_date = date(2025, 4, 18)
        self.remaining_days = (self.grad_date - self.date).days
        self.remaining_percentage = 1 - (self.remaining_days / 365)
        
    def generate(self) -> str:
        passed = int(30 * self.remaining_percentage)
        remain = 30 - passed
        progress_filled = '▓' * passed
        progress_unfilled = '▒' * remain
        if self.remaining_days != 0:
            message = f"Remaining days for Khalid's Graduation 🎓 {self.remaining_days} day/s.\nGraduation Progress: [{progress_filled}{progress_unfilled}].\n"
        else:
            message = f"Khalid Now Is Officially Graduated!\nSoftware Engineer.Khalid 🥳\n الحمدلله على التمام"   
        return message        
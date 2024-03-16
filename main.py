import time
class My_day:
    def __init__(self,me,wake_up_t,exercise_t,breakfast_t,school,
                 lunch_t,extra_lesson_t,entertainment_t,
                 dinner_t,study_t,bed_t):
        self.me = me
        self.wake_up_t = wake_up_t
        self.exercise_t = exercise_t
        self.breakfast_t = breakfast_t
        self.school = school
        self.lunch_t = lunch_t
        self.extra_lesson_t = extra_lesson_t
        self.entertainment_t = entertainment_t
        self.dinner_t = dinner_t
        self.study_t = study_t
        self.bed_t = bed_t
    def morning(self):
        return (f"{self.me} always wake up at {self.wake_up_t} and do some sports at {self.exercise_t} after this, "
                f"{self.me} have a breakfast at {self.breakfast_t} and "
                f"eventually {self.me} go to the school at {self.school}")

    def afternoon(self):
        return (f"After {self.me} have a lunch at {self.lunch_t}, "
                f"{self.me} go to the extra lessons at {self.extra_lesson_t}"
                f" but at {self.entertainment_t}  {self.me} play video games in my spare time")

    def evening(self):
        return (f"In th evening {self.me} have a dinner at {self.dinner_t}with my family and"
                f" {self.me} pay attention to study at {self.study_t}, last job is going to bed at {self.bed_t}")

day  = My_day("I","6:00","6:20","7:00", "7:30","12:00","13:30",
              "16:00", "18:30","19:30","23:00")
print(day.morning())
print(day.afternoon())
print(day.evening())





























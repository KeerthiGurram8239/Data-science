

>>> def translate(grade):
...     grade = grade.upper()
...     grade_dict = {
...         'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0,
...         'B-': 2.7, 'C+': 2.3, 'C': 2.0, 'C-': 1.7,
...         'D+': 1.3, 'D': 1.0, 'F': 0.0
...     }
...     return grade_dict.get(grade, 0.0)

>>> def main():
...    num_classes = int(input("Enter the number of classes: "))
...    total_points = 0.0
...    total_credits = 0
  
>>> for i in range(num_classees):
...     grade = input(f"Enter grade for class {i+1}:")
...     credits = int(input(f"Enter credits for class {i+1}:"))
...     total_points += translate(grade) * credits




        

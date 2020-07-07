from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.

class demographics(models.Model):
    Gender = (
    ("1", "Male"),
    ("2", "Female"),
    ("3", "Non-Binary")

    )

    Age = (
    ("4", "18-24"),
    ("5", "25-34"),
    ("6", "35-44"),
    ("7", "45-54"),
    ("7", "55-65+")
    )

    Height = (
    ("8", "<4'7/140 cm"),
    ("9", "4'8 - 4'11/ 141-150cm"),
    ("10", "4'11 - 5'3/ 151-160cm"),
    ("11", "5'3 - 5'7/ 161-170cm"),
    ("12", "5'7 - 5'11/ 171-180cm"),
    ("13", "5'11 - 6'3/ 181-190cm"),
    ("14", "<6'3 /190cm ")
    )

    Weight = (
    ("15", "100-120 pounds"),
    ("16", "120-140 pounds"),
    ("17", "140-160 pounds"),
    ("18", "160-180 pounds"),
    ("19", "180-200 pounds"),
    ("20", "200-220 pounds"),
    ("21", "220-240 pounds"),
    ("22", "240-260+ pounds")
    )

    Activity_Level = (
    ("23", "I excercise 1-2 days a week"),
    ("24", "I excercise 2-4 days a week"),
    ("25", "I excercise 4-6 days a week")
    )

    Level_of_excerise = (
    ("26", "Light- walking, jogging, etc..."),
    ("27", "Moderate- dancing, biking, use weights, etc..."),
    ("28", "Hard - swimming, running, etc...")
    )

    Do_you_smoke = (
    ("29", "Yes"),
    ("30", "No")
    )

    Do_you_take_non_presribed_drugs = (
    ("29", "Yes"),
    ("30", "No")
    )

    Do_you_often_participate_in_sports = (
    ("31", "Yes"),
    ("32", "No")
    )

    Do_you_have_a_labor_intensive_job = (
    ("33", "Yes"),
    ("34", "No")
    )
    SYMPTOMS_CHOICES = (
    ('35', 'Depression/or other mental health conditions'),
    ('36', 'Respiratory Illnesses'),
    ('37', 'Heart Condition(s)'),
    ('38', 'Have dependencies'),
    ('39', 'Take prescription drugs'),
    ('40', 'Diabetes'),
    ('41', 'Physical condition(s)'),
    ('42', 'Chronic Condition(s)'),
    ('43', 'Disabled'),
    ('44', 'Serious illnesses and disorders(HIV/Aids, Cancer ,Influenza, Scoliosis, Epilepsy, etc..)')
    )

    Gender = models.CharField(max_length=500, default='Unspecified', choices=Gender)
    Age = models.CharField(max_length=500, default='Unspecified', choices=Age)
    Height = models.CharField(max_length=500, default='Unspecified', choices=Height)
    Weight = models.CharField(max_length=500, default='Unspecified', choices=Weight)
    Activity_Level = models.CharField(max_length=500, default='Unspecified', choices=Activity_Level)
    Level_of_excerise = models.CharField(max_length=500, default='Unspecified', choices=Level_of_excerise)
    Do_you_smoke = models.CharField(max_length=500, default='Unspecified', choices=Do_you_smoke)
    Do_you_take_non_presribed_drugs = models.CharField(max_length=500, default='Unspecified', choices=Do_you_take_non_presribed_drugs)
    Do_you_often_participate_in_sports = models.CharField(max_length=500, default='Unspecified', choices=Do_you_often_participate_in_sports)
    Do_you_have_a_labor_intensive_job = models.CharField(max_length=500, default='Unspecified', choices= Do_you_have_a_labor_intensive_job)
    #SYMPTOMS
    Please_choose_all_that_apply = MultiSelectField(max_length= 100, default='Unspecified', choices=SYMPTOMS_CHOICES)

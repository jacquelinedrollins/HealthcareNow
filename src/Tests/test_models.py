import pytest 
from chooseplan.models import *
pytestmark = pytest.mark.django_db

def test_gender():
    b = questions.objects.create(
        Gender= "1"
    )
    assert b.Gender == "1"

def test_age():
    b = questions.objects.create(
        Age= "5"
    )
    assert b.Age == "5"

def test_Are_you_currently_taking_pescribed_medication():
    b = questions.objects.create(
        Are_you_currently_taking_pescribed_medication= "8GD"
    )
    assert b.Are_you_currently_taking_pescribed_medication == "8GD"

def test_Do_you_receive_regular_physicals_and_health_screenings():
    b = questions.objects.create(
        Do_you_receive_regular_physicals_and_health_screenings= "10DT"
    )
    assert b. Do_you_receive_regular_physicals_and_health_screenings == "10DT"

def test_Do_you_get_routine_vaccines_or_flu_shots():
    b = questions.objects.create(
        Do_you_get_routine_vaccines_or_flu_shots= "12PC"
    )
    assert b.Do_you_get_routine_vaccines_or_flu_shots == "12PC"

def test_Do_you_often_come_in_for_routine_checkups():
    b = questions.objects.create(
        Do_you_often_come_in_for_routine_checkups= "14PC"
    )
    assert b.Do_you_often_come_in_for_routine_checkups == "14PC"


def test_Do_you_need_prenatal_maternity_services():
    b = questions.objects.create(
        Do_you_need_prenatal_maternity_services= "16P"
    )
    assert b.Do_you_need_prenatal_maternity_services == "16P"

def test_Do_you_need_treatement_for_HIV_or_Aids():
    b = questions.objects.create(
        Do_you_need_treatement_for_HIV_or_Aids= "18GD"
    )
    assert b.Do_you_need_treatement_for_HIV_or_Aids == "18GD"

def test_Do_you_often_deal_with_skin_conditions():
    b = questions.objects.create(
        Do_you_often_deal_with_skin_conditions= "20S"
    )
    assert b.Do_you_often_deal_with_skin_conditions == "20S"

def test_Do_you_often_participate_in_sports():
    b = questions.objects.create(
        Do_you_often_participate_in_sports= "24IMARS"
    )
    assert b.Do_you_often_participate_in_sports == "24IMARS"


def test_Are_you_diagnosed_with_heart_disease():
    b = questions.objects.create(
        Are_you_diagnosed_with_heart_disease= "26OSSNC"
    )
    assert b.Are_you_diagnosed_with_heart_disease == "26OSSNC"


def test_Are_you_diagnosed_with_cancer():
    b = questions.objects.create(
        Are_you_diagnosed_with_cancer= "28SNC"
    )
    assert b.Are_you_diagnosed_with_cancer == "28SNC"

def test_Are_you_pregnant():
    b = questions.objects.create(
        Are_you_pregnant= "30P"
    )
    assert b.Are_you_pregnant == "30P"

def test_Are_you_diabetic():
    b = questions.objects.create(
        Are_you_diabetic= "32S"
    )
    assert b.Are_you_diabetic == "32S"

def test_Do_you_need_help_with_substance_abuse():
    b = questions.objects.create(
        Do_you_need_help_with_substance_abuse= "34OSIS"
    )
    assert b.Do_you_need_help_with_substance_abuse == "34OSIS"

def test_Do_you_have_a_labor_intensive_job():
    b = questions.objects.create(
        Do_you_have_a_labor_intensive_job= "36IMA"
    )
    assert b.Do_you_have_a_labor_intensive_job == "36IMA"

def test_Do_you_often_feel_chronic_pain():
    b = questions.objects.create(
        Do_you_often_feel_chronic_pain= "38RS"
    )
    assert b.Do_you_often_feel_chronic_pain == "38RS"

def test_Are_you_diagnosed_with_a_mental_health_condition():
    b = questions.objects.create(
        Are_you_diagnosed_with_a_mental_health_condition= "40OSIS"
    )
    assert b.Are_you_diagnosed_with_a_mental_health_condition == "40OSIS"

def test_Do_you_come_in_for_annual_mammogram_or_prostate_exams():
    b = questions.objects.create(
        Do_you_come_in_for_annual_mammogram_or_prostate_exams= "42DT"
    )
    assert b.Do_you_come_in_for_annual_mammogram_or_prostate_exams == "42DT"

def test_Are_you_a_candidate_for_cataract_surgery():
    b = questions.objects.create(
        Are_you_a_candidate_for_cataract_surgery= "44OS"
    )
    assert b.Are_you_a_candidate_for_cataract_surgery == "44OS"

def test_Are_you_a_candidate_for_knee_replacement():
    b = questions.objects.create(
        Are_you_a_candidate_for_knee_replacement= "46HHC"
    )
    assert b.Are_you_a_candidate_for_knee_replacement == "46HHC"

def test_Are_you_a_candidate_for_hip_replacement():
    b = questions.objects.create(
        Are_you_a_candidate_for_hip_replacement= "48HHC"
    )
    assert b.Are_you_a_candidate_for_hip_replacement == "48HHC"

















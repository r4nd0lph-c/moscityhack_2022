import os
from moscityhack_2022.settings import MODEL_ROOT
import pandas as pd
from catboost import CatBoostRegressor
from analysis_app.services import choices


def data_transform(raw: dict) -> dict:
    prepared = {}
    prepared["flag_man"] = [True] if raw["gender"] == "male" else [False]
    prepared["flag_woman"] = [not prepared["flag_man"][0]]
    prepared["flag_own_realty"] = [raw["flag_own_realty"]]
    prepared["flag_own_car"] = [raw["flag_own_car"]]
    prepared["flag_phone"] = [raw["flag_personal_phone"]]
    prepared["flag_work_phone"] = [raw["flag_work_phone"]]
    prepared["flag_email"] = [raw["flag_email"]]
    prepared["flag_employed"] = [raw["flag_employed"]]
    prepared["businessman_flag"] = [raw["flag_businessman"]]
    prepared["flag_is_pensioner"] = [raw["flag_is_pensioner"]]
    prepared["flag_resident"] = [raw["flag_is_resident"]]
    prepared["flag_non_resident"] = [not prepared["flag_resident"][0]]
    prepared["birth_date"] = [int(raw["birth_year"])]
    prepared["city"] = [raw["city"].name]
    prepared["level_education"] = [choices.CHOICES_EDUCATION_TYPE[int(raw["education_type"])][1]]
    prepared["salary"] = [raw["salary"]]
    prepared["annual_income"] = [raw["income_total"]]
    prepared["family_status"] = [choices.CHOICES_FAMILY_STATUS[int(raw["family_status"])][1]]
    prepared["amount_children"] = [raw["cnt_children"]]
    prepared["family_income"] = [raw["family_income"]]
    return prepared


def predict(data: dict) -> float:
    df = pd.DataFrame(data)
    model = CatBoostRegressor()
    model.load_model(MODEL_ROOT, format="json")
    return float(model.predict(data=df))


# def gen_redundant_data(salary: int):
#     return [round(salary / 100 * 2 * i) for i in range(50 + 1)]

def gen_10to2() -> list:
    res = []
    for i in range(31, -1, -1):
        binary = "{0:05b}".format(i)
        res.append([int(item) for item in binary])
    return res


if __name__ == "__main__":
    pass

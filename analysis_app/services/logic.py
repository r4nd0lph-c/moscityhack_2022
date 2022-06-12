from analysis_app.services import choices


def data_transform(raw: dict) -> dict:
    prepared = {}
    prepared["flag_man"] = True if raw["gender"] == "male" else False
    prepared["flag_woman"] = not prepared["flag_man"]
    prepared["flag_own_realty"] = raw["flag_own_realty"]
    prepared["flag_own_car"] = raw["flag_own_car"]
    prepared["flag_phone"] = raw["flag_personal_phone"]
    prepared["flag_work_phone"] = raw["flag_work_phone"]
    prepared["flag_email"] = raw["flag_email"]
    prepared["flag_employed"] = raw["flag_employed"]
    prepared["businessman_flag"] = raw["flag_businessman"]
    prepared["flag_is_pensioner"] = raw["flag_is_pensioner"]
    prepared["flag_resident"] = raw["flag_is_resident"]
    prepared["flag_non_resident"] = not prepared["flag_resident"]
    prepared["birth_date"] = int(raw["birth_year"])
    prepared["city"] = raw["city"].name
    prepared["level_education"] = choices.CHOICES_EDUCATION_TYPE[int(raw["education_type"])][1]
    prepared["salary"] = raw["salary"]
    prepared["annual_income"] = raw["income_total"]
    prepared["family_status"] = choices.CHOICES_FAMILY_STATUS[int(raw["family_status"])][1]
    prepared["amount_children"] = raw["cnt_children"]
    prepared["family_income"] = raw["family_income"]
    return prepared


if __name__ == "__main__":
    pass

import pandas as pd
import numpy as np
import random
import catboost
from catboost import CatBoostRegressor
from sklearn.model_selection import train_test_split

RAND = 10
'''
Для обучения ожижается 
    df.csv 
    С колонками
        client_id
        flag_man
        flag_woman
        flag_own_realty
        flag_own_car
        flag_work_phone
        flag_email
        flag_employed
        flag_is_pensioner
        flag_resident
        flag_non_resident
        birth_date
        city
        level_education
        salary
        annual_income
        family_status
        amount_children
        family_income
    
    card_type_name_df.csv
        card_name
        monthly_maintenance           ежемесячное обслуживание
        cashback                      возврат наличных
        percent_age_of_purchases      процент от покупок
        percent_age_money_account     процент на остаток
        procent_on_the_balance        процент на балансе
        flag_debit                    (0, 1)
        monthly_service_credit_card   ежемесячное обслуживание кредитки
        loan_interest                 процент по кредиту
        
        target.csv                    оценка прибыльности клиента

'''


def feature_claint(column):
    return [df[column].loc[df['client_id'] == i].iloc[0] for i in train.client_id]


def rand_generate_feature(start, stop, amount):
    return np.array([(random.randint(start, stop)) for i in range(amount)])


def count_target():
    all_metric_array = []
    for i in train.client_id:
        all_sum_open = 0
        all_sum_close = 0
        for len_id in range(len(df.loc[df['client_id'] == i])):
            contract_sum = df['contract_sum'].loc[df['client_id'] == i].iloc[len_id]
            fact_close_date = df['start_date'].loc[df['client_id'] == i].iloc[len_id]
            current_balance_avg_sum = df['current_balance_avg_sum'].loc[df['client_id'] == i].iloc[len_id]
            current_debit_turn_sum = df['current_debit_turn_sum'].loc[df['client_id'] == i].iloc[len_id]
            current_credit_turn_sum = df['current_credit_turn_sum'].loc[df['client_id'] == i].iloc[len_id]
            card_type = df['card_type'].loc[df['client_id'] == i].iloc[len_id]
            card_type_name = df['card_type_name'].loc[df['client_id'] == i].iloc[len_id]

            monthly_maintenance = \
            card_type_name_df['monthly_maintenance'].loc[card_type_name_df['name'] == card_type_name].to_frame().iloc[
                0][0]
            cashback = \
            card_type_name_df['cashback'].loc[card_type_name_df['name'] == card_type_name].to_frame().iloc[0][0]
            percentage_of_purchases = card_type_name_df['percentage_of_purchases'].loc[
                card_type_name_df['name'] == card_type_name].to_frame().iloc[0][0]
            percentage_money_account = card_type_name_df['percentage_money_account'].loc[
                card_type_name_df['name'] == card_type_name].to_frame().iloc[0][0]
            procent_on_the_balance = card_type_name_df['procent_on_the_balance'].loc[
                card_type_name_df['name'] == card_type_name].to_frame().iloc[0][0]
            flag_debit = \
            card_type_name_df['flag_debit'].loc[card_type_name_df['name'] == card_type_name].to_frame().iloc[0][0]
            loan_interest = \
            card_type_name_df['loan_interest'].loc[card_type_name_df['name'] == card_type_name].to_frame().iloc[0][0]
            procent_credit = \
            card_type_name_df['procent_credit'].loc[card_type_name_df['name'] == card_type_name].to_frame().iloc[0][0]

            if fact_close_date == '0':  # счет открыт
                if card_type == 'dc' or card_type == 'cc':
                    all_sum_open += monthly_maintenance + (
                                current_debit_turn_sum * (percentage_of_purchases - cashback) * flag_debit + (
                                    current_credit_turn_sum * (
                                        percentage_of_purchases - cashback) + current_credit_turn_sum * procent_credit) * (
                                            1 - flag_debit)) / 100
                else:
                    all_sum_open += contract_sum * procent_credit / 100
            else:
                if card_type == 'dc' or card_type == 'cc':
                    all_sum_close += monthly_maintenance + (
                                current_debit_turn_sum * (percentage_of_purchases - cashback) * flag_debit + (
                                    current_credit_turn_sum * (
                                        percentage_of_purchases - cashback) + current_credit_turn_sum * procent_credit) * (
                                            1 - flag_debit)) / 100
                else:
                    all_sum_close += contract_sum * procent_credit / 100 / 12
        all_metric_array.append((all_sum_open, all_sum_close))
    return all_metric_array


RAND = 10
df = pd.read_csv('./df.csv').fillna(0)
train = pd.DataFrame()
train['client_id'] = df.client_id.unique()
train['flag_man'] = feature_claint('flag_man')
train['flag_woman'] = feature_claint('flag_woman')
train['flag_own_realty'] = feature_claint('flag_own_realty')
train['flag_own_car'] = feature_claint('flag_own_car')
train['flag_work_phone'] = feature_claint('flag_work_phone')
train['flag_email'] = feature_claint('flag_email')
train['flag_employed'] = feature_claint('flag_employed')
train['flag_is_pensioner'] = feature_claint('flag_is_pensioner')
train['flag_resident'] = feature_claint('flag_resident')
train['flag_non_resident'] = feature_claint('flag_non_resident')
train['birth_date'] = feature_claint('birth_date')
train['city'] = feature_claint('city')
train['level_education'] = feature_claint('level_education')
train['salary'] = feature_claint('salary')
train['annual_income'] = feature_claint('annual_income')
train['family_status'] = feature_claint('family_status')
train['amount_children'] = feature_claint('amount_children')
train['family_income'] = feature_claint('family_income')

target = False
if target:
    train['target'] = pd.read_csv('./target.csv')
else:
    card_type_name_df = pd.read_csv('./card_type_name_df.csv').fillna(0)
    train['target'] = count_target()

train = train.drop('client_id', axis=1)

y = train.target
X = train.drop('target', axis=1)

cat_features = ['city', 'birth_date', 'family_status', 'level_education']

X_train, X_validation, y_train, y_validation = train_test_split(X, y, train_size=0.8, random_state=RAND)

model = CatBoostRegressor(loss_function='MAE',
                          iterations=2000,
                          learning_rate=0.1,
                          depth=6,
                          random_seed=RAND,
                          use_best_model=True,
                          early_stopping_rounds=20
                          )
train_dataset = Pool(
    data=X_train,
    label=y_train,
    cat_features=cat_features
)

eval_dataset = Pool(
    data=X_validation,
    label=y_validation,
    cat_features=cat_features
)

model.fit(train_dataset,
          use_best_model=True,
          verbose=1,
          eval_set=eval_dataset,
          )
model.save_model('model.json', format='json')
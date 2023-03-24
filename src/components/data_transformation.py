import os
import sys
import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from dataclasses import dataclass
from src.utils import save_object
from src.exception import CustomException
from src.logger import logging

@dataclass
class data_transformation_config():
    preprocessor_obj_filepath = os.path.join('artifact', 'preproccessor.pkl')

class dataTransformation():
    def __init__(self):
        self.data_transformation_config = data_transformation_config()

    def get_data_tranformer_obj(self):
        # sourcery skip: inline-immediately-returned-variable
        try:
            numerical_features = ['writing_score', 'reading_score']

            categorical_features = ['gender', 
                                    'race_ethnicity', 
                                    'parental_level_of_education', 
                                    'lunch', 'test_preparation_course']

            num_pipeline = Pipeline(
                steps= [

                    ("imputer", SimpleImputer(strategy='median')),
                    ('scaler', StandardScaler(with_mean=False))
                ]
            )
            cat_pipeline = Pipeline(
                steps= [

                    ("imputer", SimpleImputer(strategy='most_frequent')),
                    ("one_hot_encoder", OneHotEncoder()),
                    ('scaler', StandardScaler(with_mean=False))
                ]
            )
            logging.info('Numerical columns standaer scaling completed')
            logging.info('Categorical columns standaer scaling completed')

            logging.info(f'Numerical columns: {numerical_features}')
            logging.info(f'Categorical columns: {categorical_features}')
            preprocessor = ColumnTransformer(
                [
                (
                'numerical_pipleline', num_pipeline, numerical_features
                ),
                ('categorical_pipeline', cat_pipeline, categorical_features)
                ]
            )
            return preprocessor

        except Exception as e:
            raise CustomException(e,sys) from e
        
    
    def initiate_data_tranformation(self, train_path, test_path):

        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info('read train and test data')
            logging.info('obtaining preprocessing object')
            preprocessor_obj = self.get_data_tranformer_obj()
            target_column = 'math_score'
            target_feature_train_df = train_df[target_column]
            train_df.drop(columns=target_column, axis=1 ,inplace=True)
            input_feature_train_df = train_df
            target_feature_test_df = test_df[target_column]
            test_df.drop(columns=target_column, axis=1, inplace =True)
            input_feature_test_df = test_df

            logging.info('Applying preprocessing object on train data')
            input_feature_train_arr = preprocessor_obj.fit_transform(input_feature_train_df)
            logging.info('Applying preprocessing object on test data')
            input_feature_test_arr = preprocessor_obj.transform(input_feature_test_df)


            train_arr = np.hstack((input_feature_train_arr, np.array(target_feature_train_df).reshape(-1, 1)))
            test_arr = np.hstack((input_feature_test_arr, np.array(target_feature_test_df).reshape(-1, 1)))

            logging.info('Saved preprocessing obj')
            save_object(file_path=self.data_transformation_config.preprocessor_obj_filepath, obj=preprocessor_obj)

            

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_filepath
            )
        except Exception as e:
            raise CustomException(e,sys) from e
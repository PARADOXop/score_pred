import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.metrics import r2_score
import os
import sys
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
from src.logger import logging
from catboost import CatBoostRegressor
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor, GradientBoostingRegressor
from src.exception import CustomException
from dataclasses import dataclass
from src.utils import save_object

@dataclass

class model_trainer_config():
    modelTrainer_obj_filepath = os.path.join('artifact', 'train_model.pkl')

class model_Trainer():
    def __init__(self):
        self.model_trainer_config = model_trainer_config()

    def model_trainer_obj(self):
        try:
            pass

        except Exception as e:
            raise CustomException(e, sys) from e

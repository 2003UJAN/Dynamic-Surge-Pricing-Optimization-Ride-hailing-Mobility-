# -*- coding: utf-8 -*-
"""Welcome To Colab

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/github/2003UJAN/Dynamic-Surge-Pricing-Optimization-Ride-hailing-Mobility/blob/main/q_learning.ipynb
"""

import numpy as np
import joblib

class QLearningSurgePricing:
    def __init__(self):
        self.q_table = np.zeros((24, 10, 4, 2, 5))
        self.alpha = 0.1
        self.gamma = 0.9

    def get_price_multiplier(self, hour, traffic, weather, events):
        state = (hour, traffic - 1, weather - 1, events)
        action = np.argmax(self.q_table[state])
        return 1 + (action * 0.2)

    def update_q_table(self, state, action, reward):
        max_future_q = np.max(self.q_table[state])
        self.q_table[state][action] = (1 - self.alpha) * self.q_table[state][action] + self.alpha * (reward + self.gamma * max_future_q)

joblib.dump(QLearningSurgePricing(), "q_learning_model.pkl")
print("Q-Learning model initialized and saved.")
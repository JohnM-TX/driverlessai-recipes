#!/usr/bin/env python
# coding: utf-8

import typing
import numpy as np
from h2oaicore.metrics import CustomScorer
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

class fbeta(CustomScorer):
    _description = "Fbeta(4))`"
    _binary = True
    _multiclass = True
    _maximize = True
    _perfect_score = 1
    _display_name = "F4 Score"
    _threshold = 0.5  

    def score(self,
              actual: np.array,
              predicted: np.array,
              sample_weight: typing.Optional[np.array] = None,
              labels: typing.Optional[np.array] = None) -> float:
        lb = LabelEncoder()
        labels = lb.fit_transform(labels)
        actual = lb.transform(actual)
        method = "binary"
        if len(labels) > 2:
            predicted = np.argmax(predicted, axis=1)
            method = "micro"
        else:
            predicted = (predicted > self._threshold)
        precision =  precision_score(actual, predicted, labels=labels, average=method, sample_weight=sample_weight)
        recall = recall_score(actual, predicted, labels=labels, average=method, sample_weight=sample_weight)
    
        numerator = precision*recall
        denominator = (16)*precision + recall
        f4_score =  (17)*numerator/denominator                           
                                    
        return f4_score
    







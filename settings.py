#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 09:50:43 2018

@author: rosiewang
"""

DATA_DIR = 'data'
PROCESSED_DIR = 'processed'
MINIMUM_TRACKING_QUARTERS = 4
TARGET = 'foreclosure_status'
NON_PREDICTORS = [TARGET, 'id']
CV_FOLDS = 3
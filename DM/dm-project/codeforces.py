#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 22:05:47 2021

@author: pranshu
"""


import codeforces_api

api_key = '5edd15ea06285efde045ca66d290b6890a4696af'
secret = 'c37ef5b210d3552e00d7f03dc924bc29bcd43de7'
cf_api = codeforces_api.CodeforcesApi (api_key, secret) # Authorized access.
anonim_cf_api = codeforces_api.CodeforcesApi() 

probs = anonim_cf_api.problemset_problems(tags=['implementation'])


problems = probs['problems']

for p in problems:
    print(p.name, p.points, p.rating, p.tags)
    



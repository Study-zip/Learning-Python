#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import numbers
import os, sys
from turtle import heading

class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        # super().__init__() 다중 상속시 전부 언급하기
        Unit.__init__(self)
        Flyable.__init__(self)
    
# 드랍쉽
dropship = FlyableUnit()

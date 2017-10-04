# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm

# Create your models here.


class Submision(models.Model):
    '''A class defining how submission is to be handled

    '''
    INDIVIDUAL = 'IN'
    COMPANY = 'CO'
    Ownership_choice = (
        (INDIVIDUAL,'Individual'),
        (COMPANY,'Company'),
    )

    YES = 'Y'
    NAY = 'N'
    Yay_Nay = (
        (YES,'Yes'),
        (NAY,'No'),
    )

    CONCEPT = 'CON'
    DESIGN = 'DES'
    INNOVAION = 'INN'
    PRODUCT = 'PRO'
    ALPHAORBEAT = 'ALP'
    PRODUCTION = 'PDN'
    TEASER = 'TEA'
    FULL = 'FLD'
    Innovation_stage = (
        (CONCEPT,'Concept'),
        (DESIGN,'Design'),
        (INNOVAION,'Innovation'),
        (PRODUCT,'Product'),
        (ALPHAORBEAT,'Alpha/Beta testing'),
        (PRODUCTION,'Production testing'),
        (TEASER,'Teaser Marketing'),
        (FULL,'Full Development'),
    )
    individual_Name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    individualBD = models.DateField(default='')
    current_address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    probelemStatement = models.CharField(max_length=200)
    background = models.CharField(max_length=200)
    concept = models.CharField(max_length=20)
    ownership = models.CharField(max_length=200, choices=Ownership_choice, default="")
    company_regDate = models.DateField(default='')
    
    individual_NIN = models.CharField(max_length=14)
    BusinessPlan = models.CharField(max_length=255)
    FeasibilityStudy = models.CharField(max_length=3, choices=Yay_Nay, default="")
    StudyUpload = models.FileField(upload_to='uploads/feasibility/%Y/%m/%d/')
    ActionStatement = models.CharField(max_length=255)
    EstimatedCost = models.IntegerField()
    Innov_Stage = models.CharField(max_length=100, choices=Innovation_stage, default="")
    Stage_Description = models.CharField(max_length=255)
    Amount_invested = models.IntegerField()
    Market_Study = models.CharField(max_length=14, choices=Yay_Nay, default="")
    Market_Std_Descrip = models.CharField(max_length=255)
    Market_STd_file = models.FileField(upload_to='uploads/mkt_study/%Y/%m/%d/')
    Market = models.CharField(max_length=255)
    Value_Added = models.CharField(max_length=255)
    Time_to_product = models.CharField(max_length=255)
    End_User_Invol = models.CharField(max_length=255)
    Monitoring = models.CharField(max_length=255)
    Fund_Raise = models.CharField(max_length=500)
    Problems = models.CharField(max_length=300)
    Impacts = models.CharField(max_length=300)
    Remedies = models.CharField(max_length=255)
    Safety = models.CharField(max_length=255)
    Locations = models.CharField(max_length=255)
    Sustainability = models.CharField(max_length=255)
    MultiCultural = models.CharField(max_length=255)

    def getindividual_Name(self):
        return self.individual_Name
    def getgender(self):
        return self.gender
    def getcurrent_address(self):
        return self.current_address
    def getphone_number(self):
        return self.phone_number
    def getemail(self):
        return self.email

    def whichtitle(self):
        '''Method to return the innovation title '''
        return self.title

    def problemstate(self):
        '''Method to return the problem statement of an innovation '''
        return self.probelemStatement

    def whichbackground(self):
        '''Mthod that returns innovation background '''
        return self.background

    def whichconcept(self):
        return self.concept
        
    def whichownership(self):
        return str(self.ownership)

    def whichregdate(self):
        return self.company_regDate

    def whichindividualbirth(self):
        return self.individualBD

    def whichnin(self):
        return self.individual_NIN

    def whichBusPlan(self):
        return self.BusinessPlan

    def whichFeasibilityStudy(self):
        return str(self.FeasibilityStudy)

    def whichStudyUpload(self):
        return self.StudyUpload

    def whichActionStatement(self):
        return self.ActionStatement

    def whichEstimatedCost(self):
        return self.EstimatedCost

    def whichInnov_Stage(self):
        return str(self.Innov_Stage)

    def whichStage_Description(self):
        return self.Stage_Description

    def whichAmount_invested(self):
        return str(self.Amount_invested)

    def whichMarket_Study(self):
        return self.Market_Study

    def whichMarket_Std_Descrip(self):
        return self.Market_Std_Descrip

    def whichMarket_STd_file(self):
        str(self.Market_STd_file)

    def whichMarket(self):
        return self.Market

    def whatValueAdded(self):
        return self.Value_Added

    def whatTime_to_product(self):
        return self.Time_to_product

    def whatEndUserInvol(self):
        return self.End_User_Invol

    def whichMonitoring(self):
        return self.Monitoring

    def WhichFund_Raise(self):
        return self.Fund_Raise

    def WhatProblems(self):
        return self.Problems

    def whichImpacts(self):
        return self.Impacts

    def whichRemedies(self):
        return self.Remedies

    def whatSafety(self):
        return self.Safety

    def whichLocations(self):
        return self.Locations
    
    def whichSustainability(self):
        return self.Sustainability

    def HowMultiCultural(self):
        return self.MultiCultural

class member(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)

    def __str__(self):
        return '{}  {}'.format(self.first_name, self.last_name)

    def getemail(self):
        return self.email

    def getphonenumber(self):
        return str(self.phone_number)
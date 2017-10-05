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

class vote(models.Model):
    PROBLEM = 'What problem Does the innovation seek to address?'
    WHY = 'Why this Innovation? Do simillar Products exist?'
    NEW = 'Is it a new concept or an existing one? If new? Have you applied for any Intellectual property rights'
    INDIVIDUAL = 'Is the innovation done by an individual or a company'
    BUSINESSPLAN = 'Summary of Business Plan'
    FEASIBILITY = 'Was any technical or economic feasilbity carried out?'
    PLAN = 'How do you plan to develop after Innovation?'
    COSTS = 'How do you plan to develop the product after innovation'
    INNOSTAGE = 'concept stage; design stage; invovation development ; product development; alpha / beta testing; production testing; teaser marketing;or full development'
    FINANCES = 'Finances already invested in the product'
    MARKETSTUDY = 'Was any market study/ customer feedback or market research done? If so details?'
    IMPROVE = 'How exactly does the innovation improves the lives of citizens?'
    TARGETMKT = 'What is the Target Market?'
    DESIGN2PRDN = 'Estimated time for design to production ? (If at design stage else time from that stage to production)'
    INVOLVEMENT = 'Who is part of the design prototyping, implementing, monitoring and evaluating?'
    PROGRESS = 'How will the progress be monitored to obtain quick feedback to further spur development?'
    POTENTIAL = 'Have you identified potential locations or use ICT ministrys site for devlopment?'
    FINANCE = 'How will you intend to raise finance and how the same be utilised?'
    SCALABILITY = 'How do you plan to scale upwards  and outwards and how will this scaling be sustainable?'
    BOUNDARIES = 'is your product able to meet demands/needs outside the boundaries of uganda and if so, where?'
    PROBLEMS = 'Detail potential problems youll face, the Impacts and remedies to said problems?'
    SAFETY = 'Identify any safety issues for the end users  while using the innovation product?'

    Question_Voted = (
        (PROBLEM, 'Problem'),
        (WHY, 'Why'),
        (NEW, 'New'),
        (INDIVIDUAL, 'Individual'),
        (BUSINESSPLAN, 'Business Plan'),
        (FEASIBILITY, 'Feasibility'),
        (PLAN, 'Plan'),
        (COSTS, 'Costs'),
        (INNOSTAGE, 'Innovation Stage'),
        (FINANCES, 'Finances'),
        (MARKETSTUDY, 'MarketStudy'),
        (IMPROVE, 'Improve'),
        (TARGETMKT, 'Target Market'),
        (DESIGN2PRDN, 'Design to Production'),
        (INVOLVEMENT, 'Involved'),
        (PROGRESS, 'Progress'),
        (POTENTIAL, 'Potential Locations'),
        (FINANCE, 'Raise Finance'),
        (SCALABILITY, 'Scalability'),
        (BOUNDARIES, 'Beyond Uganda'),
        (PROBLEMS, 'Problems'),
        (SAFETY, 'Safety'),
    )

    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    Question_Vote = (
        (ONE, 'One'),
        (TWO, 'Two'),
        (THREE, 'Three'),
        (FOUR, 'Four'),
        (FIVE, 'Five'),
        (SIX, 'Six'),
        (SEVEN, 'Seven'),
        (EIGHT, 'Eight'),
        (NINE, 'Nine'),
        (TEN, 'Ten'),
    )
    mem_who_voted = models.ForeignKey('member', related_name="Member", on_delete=models.CASCADE)
    innovation_voted = models.ForeignKey('Submision', related_name="Innovation", on_delete=models.CASCADE)
    field_voted = models.CharField(max_length=255, choices=Question_Voted, default='which')
    Vote_given = models.CharField(max_length=255, choices=Question_Vote, default="")

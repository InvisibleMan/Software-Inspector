# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
"""
class KnownSoftware(models.Model):
	iProgramID = models.PositiveIntegerField()
	#тут тип надо сделать целый, с внешним ключом на KnownVendors.ID
	iVendorID = models.PositiveIntegerField()
	sProgramName = models.CharField(max_length=50)
	sVersion = models.CharField(max_length=50)
	sLanguage = models.CharField(max_length=50)
	sProductPage = models.URLField(verify_exists=False, null=True, blank=True)
	sProgramDownloadURL = models.URLField(verify_exists=False, null=True, blank=True)
	#изменить тип на булево значение
	bHidden = models.CharField(max_length=50)
	#изменить тип на булево значение
	bRemoved = models.CharField(max_length=50)
	#изменить тип на булево значение
	bFreeware = models.CharField(max_length=50)
	#изменить тип на булево значение
	bTrialVerion = models.CharField(max_length=50)
	#изменить тип на булево значение
	bOpenSource = models.CharField(max_length=50)
	#изменить тип на булево значение
	bObsolete = models.CharField(max_length=50)
	sExtraInfo1 = models.CharField(max_length=50)
	sExtraInfo2 = models.CharField(max_length=50)
	sExtraInfo3 =	models.CharField(max_length=50)

	def __unicode__(self):
		return self.name

class KnownVendors(models.Model):
	ID = models.PositiveIntegerField()
	sName = models.CharField(max_length=50)
	sWebSiteURL = models.URLField(verify_exists=False, null=True, blank=True)

	def __unicode__(self):
		return self.name

class KnownSoftwareRelations(models.Model):
	#тут тип надо сделать целый, с внешним ключом на KnownSoftware.iProgramID
	iWorseProgramID = models.PositiveIntegerField()
	sRelationType = models.CharField(max_length=50)
	#тут тип надо сделать целый, с внешним ключом на KnownSoftware.iProgramID
	iBetterProgramID = models.PositiveIntegerField()
	sComment = models.CharField(max_length=50)

	def __unicode__(self):
		return self.name

class Users(models.Model):
	#тут тип надо сделать целый, с внешним ключом на KnownSoftware.iProgramID
	ID = models.PositiveIntegerField()
	sLoginName = models.CharField(max_length=50)
	sFirstName = models.CharField(max_length=50)
	sLastName = models.CharField(max_length=50)
	sHostname1 = models.CharField(max_length=50)
	sHostname2 = models.CharField(max_length=50)
	sHostname3 = models.CharField(max_length=50)
	sEmail = models.CharField(max_length=50)
	sOpenIDServer =	models.CharField(max_length=50)
	sOpenIDAccount = models.CharField(max_length=50)
	sPasswordHash = models.CharField(max_length=50)
	#тут тип надо сделать целый, с внешним ключом на Professions.ID
	iProfessionID1 = models.PositiveIntegerField()
	#тут тип надо сделать целый, с внешним ключом на Professions.ID
	iProfessionID2 = models.PositiveIntegerField()
	#тут тип надо сделать целый, с внешним ключом на Professions.ID
	iProfessionID3 = models.PositiveIntegerField()
	sLanguage = models.CharField(max_length=50)
	sCountry = models.CharField(max_length=50)

	def __unicode__(self):
		return self.name

class Users(models.Model):
	#тут тип надо сделать целый, с внешним ключом на KnownSoftware.iProgramID
	ID = models.PositiveIntegerField()
	sDescEng = models.CharField(max_length=50)

	def __unicode__(self):
		return self.name
"""

"""
class SoftVersion(models.Model):
	name = models.CharField(max_length=50)
	soft = models.ForeignKey(Soft)
	url = models.URLField(verify_exists=False, null=True, blank=True)
	download_url = models.URLField(verify_exists=False, null=True, blank=True)
	price =	models.DecimalField(max_digits=5, decimal_places=2)
	version = models.CharField(max_length=10)
	user_version = models.CharField(max_length=10)
	# платформа
	platform = models.PositiveIntegerField()
	
	def __unicode__(self):
		return self.name

class SoftItem(models.Model):
	user = models.ForeignKey(User)
	soft_version = models.ForeignKey(SoftVersion)
"""

#тестовый вариант для загрузки
class SoftLine(models.Model):
	name = models.CharField(max_length=50)
	version = models.CharField(max_length=50)
	user = models.ForeignKey(User)

	def __unicode__(self):
		return self.name
	

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the 
#desired behavior
#   * Remove ` ` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Countries_of_interest = models.ForeignKey('Countries', models.DO_NOTHING, db_column='Country',blank=True,null=True,default=None)
    Products_of_interest = models.ForeignKey('Commodities', models.DO_NOTHING, db_column='product',blank=True,null=True,default=None)
    Parameters_of_interest = models.ForeignKey('RegulatoryParameters', models.DO_NOTHING, db_column='parameter',blank=True,null=True,default=None)
    Parameter_types_of_interest = models.ForeignKey('TypeOfParameters', models.DO_NOTHING, db_column='type',blank=True,null=True,default=None)
    def clean(self):
        if ((self.Products_of_interest or self.Parameters_of_interest or self.Countries_of_interest) and self.Parameter_types_of_interest):
            raise ValidationError('....')

    class Meta:
        verbose_name_plural = "USER INTERESTS"
        verbose_name = "User Interest"
        unique_together = (('Countries_of_interest', 'Products_of_interest', 'Parameters_of_interest'),('Parameter_types_of_interest',),)

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

# class AuthGroup(models.Model):
#     name = models.CharField(unique=True, max_length=150)

#     class Meta:
#         db_table = 'auth_group'


# class AuthGroupPermissions(models.Model):
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#     permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

#     class Meta:
         
#         db_table = 'auth_group_permissions'
#         unique_together = (('group', 'permission'),)


# class AuthPermission(models.Model):
#     name = models.CharField(max_length=255)
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
#     codename = models.CharField(max_length=100)

#     class Meta:
         
#         db_table = 'auth_permission'
#         unique_together = (('content_type', 'codename'),)


# class AuthUser(models.Model):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.IntegerField()
#     username = models.CharField(unique=True, max_length=150)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=150)
#     email = models.CharField(max_length=254)
#     is_staff = models.IntegerField()
#     is_active = models.IntegerField()
#     date_joined = models.DateTimeField()

#     class Meta:
         
#         db_table = 'auth_user'


# class AuthUserGroups(models.Model):
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

#     class Meta:
         
#         db_table = 'auth_user_groups'
#         unique_together = (('user', 'group'),)


# class AuthUserUserPermissions(models.Model):
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)        

#     class Meta:
         
#         db_table = 'auth_user_user_permissions'
#         unique_together = (('user', 'permission'),)


class ComCountryRelation(models.Model):
    commodity = models.OneToOneField('Commodities', models.DO_NOTHING, db_column='commodity', primary_key=True)
    country = models.ForeignKey('Countries', models.DO_NOTHING, db_column='country')
    published_commodity = models.TextField(db_column='Published_commodity', blank=True, null=True)  # Field name made lowercase.
    definition_commodity_field = models.TextField(db_column='Definition_commodity_', blank=True, null=True)  # Field name made lowercase. Field renamed because it ended with '_'.
    Yes='YES'
    No='NO'
    undefined_published_commodity_choices=((Yes,'YES'),(No,'NO'),)
    
    undefined_published_commodity = models.CharField(db_column='Undefined_published_commodity', max_length=3,choices=undefined_published_commodity_choices,default=No)  # Field name made lowercase.

    class Meta:
         
        db_table = 'com_country_relation'
        unique_together = (('commodity', 'country'),)
        verbose_name_plural = "Rules Associated with country and products"
        verbose_name = "Country-Product Relationship"
        # permissions=(
        #     ('read_Country_product_relationships','Can read specific information related to any product with any country'),
        # )



class Commodities(models.Model):
    com_name = models.CharField(primary_key=True, max_length=255)
    Ra='RAW AGRICULTURAL'
    Proc='PROCESSED'
    com_type_choices=((Ra,'RAW AGRICULTURAL'),(Proc,'PROCESSED'),)
    com_type = models.CharField(db_column='com-type', max_length=16,choices=com_type_choices,null=True)  # Field renamed to remove unsuitable characters.

    def __str__(self):
        return self.com_name

    class Meta:
         
        db_table = 'commodities'
        verbose_name_plural = "List of Commodities"
        verbose_name = "Commodity"
        # permissions=(
        #     ('read_commodities','Can read commodities supported by platform'),
        # )



class Countries(models.Model):
    country_name = models.CharField(primary_key=True, max_length=45)
    note_for_country_regulations = models.TextField(db_column='Note_for_country_regulations')  # Field name made lowercase.
    pdf_note = models.FileField(upload_to='pdf', blank=True, null=True)
    def __str__(self):
        return self.country_name

    class Meta:
         
        db_table = 'countries'
        verbose_name_plural = "List of Countries"
        verbose_name = "Country"
        # permissions=(
        #     ('read_countries','Can read countries supported by platform'),
        # )


# class DjangoAdminLog(models.Model):
#     action_time = models.DateTimeField()
#     object_id = models.TextField(blank=True, null=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.PositiveSmallIntegerField()
#     change_message = models.TextField()
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, 
# blank=True, null=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)

#     class Meta:
         
#         db_table = 'django_admin_log'


# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)

#     class Meta:
         
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)


# class DjangoMigrations(models.Model):
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()

#     class Meta:
         
#         db_table = 'django_migrations'


# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()

#     class Meta:
         
#         db_table = 'django_session'
class Authorities(models.Model):
    Authority_Name = models.CharField(primary_key=True, max_length=20)
    country = models.ForeignKey(Countries, models.DO_NOTHING, db_column='Country', blank=True, null=True)
    info_note = models.TextField(db_column='Remarks', blank=True, null=True)
    def __str__(self):
        return self.Authority_Name

    class Meta:
        verbose_name = "Authority"
        verbose_name_plural = "Regulatory Authorities"
        # permissions=(
        #     ('read_parameter_types','Can read parameter types supported by platform'),
        # )


class Master(models.Model):
    ID= models.IntegerField(db_column='IDX',primary_key=True, editable=False)
    country = models.ForeignKey(Countries, models.DO_NOTHING, db_column='Country')  # Field name made lowercase.
    product = models.ForeignKey(Commodities, models.DO_NOTHING, db_column='Product')  # Field name made lowercase.
    parameter = models.ForeignKey('RegulatoryParameters', models.DO_NOTHING, 
db_column='Parameter')  # Field name made lowercase.
    Maximum_Limit = models.FloatField(db_column='Maximum_Limit', max_length=10,blank=True,null=True)  # Field name made lowercase.
    Minimum_Limit = models.FloatField(db_column='Minimum_Limit', max_length=10, default=0)
    Unit = models.CharField(db_column='Unit', max_length=20, blank=True, null=True)
    # Constants in Model class
    Default='Default'
    General='General'
    Organic_MRLs='Organic MRLs'
    Not_defined='Not defined'

    mrl_type_choices = (
        (Default, 'Default'),
        (General, 'General'),
        (Organic_MRLs,'Organic MRLs'),
        (Not_defined,'Not defined')
        )
    
    Limit_type = models.CharField(db_column='MRL_type', max_length=20,choices=mrl_type_choices,default=Default)  # Field 
#name made lowercase.
    effective_date = models.DateField(db_column='Effective_Date', blank=True, null=True)  # Field name made lowercase.
    expire_date = models.DateField(db_column='Expire_Date', blank=True, null=True)  # Field name made lowercase.
    Proposed='Proposed'
    Fixed='Fixed'
    status_of_expire_date_choices=((Proposed,'Proposed'),(Fixed,'Fixed'),)
    
    status_of_expire_date = models.CharField(db_column='Status_of_expire_date', max_length=8, blank=True, null=True,choices=status_of_expire_date_choices,default=None)  # Field name made lowercase.        
    Yes='YES'
    No='NO'
    import_tolerance_choices=((Yes,'YES'),(No,'NO'),)
    import_tolerance = models.CharField(max_length=3,choices=import_tolerance_choices,default=No)
    info_on_regulations = models.CharField(db_column='Info_on_regulations', max_length=255, blank=True, null=True)  # Field name made lowercase.
    Compliance_Authority= models.ForeignKey(Authorities, models.DO_NOTHING, db_column='Authority_Name', null=True, blank=True)
    parameter_definition = models.CharField(db_column='Residue_definititon', max_length=255, blank=True, null=True)  # Field name made lowercase.
    source_document = models.TextField(blank=True, null=True)
    date_of_publishing_source = models.DateField(db_column='Date_of_publishing_source', blank=True, null=True)  # Field name made lowercase.
    Ma='MANDATORY'
    Mo='MONITORING'
    pd='PROPOSED DRAFT'
    criticality_of_maintaining_choices=((Ma,'MANDATORY'),(Mo,'MONITORING'),(pd,'PROPOSED DRAFT'),)
    criticality_of_maintaining = models.CharField(db_column='Criticality_of_maintaining', max_length=20,choices=criticality_of_maintaining_choices,default=Ma)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.

    class Meta:
         
        db_table = 'master'
        verbose_name_plural = "Main Table"
        verbose_name = "Regulation Detail"
        unique_together = (('country', 'product', 'parameter','criticality_of_maintaining',))
        ordering = ['country', 'product','criticality_of_maintaining', 'parameter']
        # permissions=(
        #     ('read_master','Can read specific MRL related to various countries and commodities supported by platform'),
        # )


class RegulatoryParameters(models.Model):
    name_of_parameter = models.CharField(db_column='Name_of_parameter', primary_key=True, max_length=255)  # Field name made lowercase.
    type_of_parameter = models.ForeignKey('TypeOfParameters', models.DO_NOTHING, db_column='Type_of_parameter')  # Field name made lowercase.

    def __str__(self):
        return self.name_of_parameter

    class Meta:
         
        db_table = 'regulatory_parameters'
        verbose_name = "PARAMETER"
        verbose_name_plural = "List of Parameters"
        
        # permissions=(
        #     ('read_parameters','Can read parameters supported by platform'),
        # )


# class Authorities(models.Model):
#     Authority_Name = models.CharField(primary_key=True, max_length=20)
#     country = models.ForeignKey(Countries, models.DO_NOTHING, db_column='Country', blank=True, null=True)

#     def __str__(self):
#         return self.type

#     class Meta:
#         verbose_name = "Authority"
#         verbose_name_plural = "Authorities"
#         # permissions=(
        #     ('read_parameter_types','Can read parameter types supported by platform'),
        # )

class TypeOfParameters(models.Model):
    type = models.CharField(primary_key=True, max_length=40)

    def __str__(self):
        return self.type

    class Meta:
        db_table = 'type_of_parameters'
        verbose_name = "TYPE OF PARAMETER"
        verbose_name_plural = "List of TYPES OF PARAMETERS"
        # permissions=(
        #     ('read_parameter_types','Can read parameter types supported by platform'),
        # )
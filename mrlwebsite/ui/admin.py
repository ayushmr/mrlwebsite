from django.contrib import admin
from .filters import *
from django_admin_multiple_choice_list_filter.list_filters import MultipleChoiceListFilter
from django.db.models import Q
# Register your models here.
from .models import Master, RegulatoryParameters, TypeOfParameters,Countries,Commodities,ComCountryRelation, Profile,Authorities
from django.contrib.auth.models import Permission
# admin.site.register(Permission)
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from django.contrib.admin import AdminSite
from django.http import HttpResponse

from django.contrib.admin.sites import site as default_site

from related_admin import RelatedFieldAdmin
from related_admin import getter_for_related_field




admin.site.site_header = "ITC's Global Regulatory Database Admin Portal| KITES PROJECT"

@admin.register(Profile)
class ProfilesAdmin(admin.ModelAdmin):
    list_display = ('user', 'Countries_of_interest','Products_of_interest','Parameters_of_interest','Parameter_types_of_interest',)


#admin.site.register(Master)
#admin.site.register(RegulatoryParameters)
#admin.site.register(TypeOfParameters)
#admin.site.register(Countries)
#admin.site.register(Commodities)
#admin.site.register(ComCountryRelation)
class ComCountryRelationInline(admin.TabularInline):
    model = ComCountryRelation

# class StatusListFilter(MultipleChoiceListFilter):
#     title = 'Priority'
#     parameter_name = 'criticality_of_maintaining'

#     def lookups(self, request, model_admin):
#         return Master.criticality_of_maintaining_choices


# # Define the admin class

# class countriesListFilter(admin.SimpleListFilter):
    
#     """
#     This filter will always return a subset of the instances in a Model, either filtering by the
#     user choice or by a default value.
#     """
#     # Human-readable title which will be displayed in the
#     # right admin sidebar just above the filter options.
#     title = 'Countries'

#     # Parameter for the filter that will be used in the URL query.
#     parameter_name = 'country'

#     default_value = None

#     def lookups(self, request, model_admin):
#         """
#         Returns a list of tuples. The first element in each
#         tuple is the coded value for the option that will
#         appear in the URL query. The second element is the
#         human-readable name for the option that will appear
#         in the right sidebar.
#         """
#         list_of_countries = []
#         queryset = Countries.objects.all()
#         for countries in queryset:
#             list_of_countries.append(
#                 (str(countries.country_name), countries.country_name)
#             )
#         return sorted(list_of_countries, key=lambda tp: tp[1])

#     def queryset(self, request, queryset):
#         """
#         Returns the filtered queryset based on the value
#         provided in the query string and retrievable via
#         `self.value()`.
#         """
#         # Compare the requested value to decide how to filter the queryset.
#         if self.value():
#             return queryset.filter(country__country_name=self.value())
#         return queryset

#     def value(self):
#         """
#         Overriding this method will allow us to always have a default value.
#         """
#         value = super(countriesListFilter, self).value()
#         if value is None:
#             if self.default_value is None:
#                 # If there is at least one Species, return the first by name. Otherwise, None.
#                 first_countries = Countries.objects.order_by('country_name').first()
#                 value = None if first_countries is None else first_countries.country_name
#                 self.default_value = value
#             else:
#                 value = self.default_value
#         return str(value)
class RegulatoryParametersResource(resources.ModelResource):
    
    class Meta:
        model = RegulatoryParameters
        import_id_fields=['name_of_parameter']


class CountryResource(resources.ModelResource):
    
    class Meta:
        model = Countries
        import_id_fields=['country_name']

class MasterResource(resources.ModelResource):
    
    class Meta:
        model = Master
        import_id_fields=['country','product','parameter','criticality_of_maintaining']
        exclude=('ID',)
        fieldsets = (
        (None, {
            'fields': ('country', 'product', 'parameter',('Maximum_Limit','Minimum_Limit','Unit','criticality_of_maintaining','parameter_definition','import_tolerance'))
        }),
        ('Additional Details about timeline of rule', {
            'fields': ('effective_date', 'expire_date','status_of_expire_date')
        }),
        ('Information on source and rules', {
            'fields': ('info_on_regulations','Limit_type','source_document','date_of_publishing_source','remarks')
        }),
    )

    
# class MasterAdmin(admin.ModelAdmin):
    # list_display = ('country', 'product', 'parameter', 'mrl','criticality_of_maintaining','mrl_type','effective_date','expire_date','status_of_expire_date','import_tolerance','date_of_publishing_source','info_on_regulations','residue_definition','source_document','remarks')
    # list_filter = (('product', admin.RelatedOnlyFieldListFilter),('parameter', admin.RelatedOnlyFieldListFilter),('country', admin.RelatedOnlyFieldListFilter),'criticality_of_maintaining',)
    # search_fields=('country__country_name','parameter__name_of_parameter','product__com_name',)
    # def get_ordering(self, request):
    #     if request.user.is_superuser:
    #         return ['country', 'product','parameter']
    #     else:
    #         return ['country']

    # blog_list = Master.objects.filter( country__country_name = 'Canada' ).order_by( '-id' )
    # list_select_related=('product','parameter',)
    
    # def country(self,obj):
    #     return obj.country.country_name
    # country.admin_order_field='country'
    # # multiple_selection_list_filter = ('country', 'product','parameter','criticality_of_maintaining',)
    # fields=['country','product', ('parameter', 'mrl','residue_definition','criticality_of_maintaining'),('info_on_regulations','source_document'),'remarks']    
# Register the admin class with the associated model
    # fieldsets = (
    #     (None, {
    #         'fields': ('country', 'product', 'parameter',('mrl','criticality_of_maintaining','residue_definition','import_tolerance'))
    #     }),
    #     ('Additional Details about timeline of rule', {
    #         'fields': ('effective_date', 'expire_date','status_of_expire_date')
    #     }),
    #     ('Information on source and rules', {
    #         'fields': ('info_on_regulations','mrl_type','source_document','date_of_publishing_source','remarks')
    #     }),
    # )
    # def get_readonly_fields(self, request, obj=None):
    #     if not request.user.is_superuser and request.user.has_perm('master.read_master'):
    #         return [(f.product,f.country,f.parameter,f.mrl,f.mrl_type) for f in self.model._meta.fields]        
    #     return super(MasterAdmin, self).get_readonly_fields(
    #         request, obj=obj
    #     )

class MasterAdmin(ImportExportModelAdmin,RelatedFieldAdmin):
    resource_class = MasterResource
    list_display = ('country', 'product', 'parameter','parameter__type_of_parameter', 'Maximum_Limit','Minimum_Limit','Unit','criticality_of_maintaining','Limit_type','effective_date','expire_date','status_of_expire_date','import_tolerance','source_document','date_of_publishing_source','info_on_regulations','parameter_definition','remarks')
    # list_display = ('country', 'product', 'parameter', 'mrl','criticality_of_maintaining','mrl_type','effective_date','expire_date','status_of_expire_date','import_tolerance','date_of_publishing_source','info_on_regulations','residue_definition','source_document','remarks')
    list_filter = (('product', admin.RelatedOnlyFieldListFilter),'parameter__type_of_parameter',('country', admin.RelatedOnlyFieldListFilter),'criticality_of_maintaining',)
    search_fields=('country__country_name','parameter__name_of_parameter','product__com_name','parameter__type_of_parameter','info_on_regulations','parameter_definition','Limit_type','effective_date','expire_date','status_of_expire_date' ,'source_document','date_of_publishing_source','info_on_regulations','remarks')
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        master_instance=Profile.objects.filter(user=request.user)
        # print(qs.filter(parameter__type_of_parameter='Physico-chemical'))
        Final=Q()
        for i in master_instance:
            Temp=Q()
            
            if(i.Parameter_types_of_interest==None):
                if(i.Countries_of_interest==None):
                    if(i.Products_of_interest==None):
                        if(i.Parameters_of_interest==None):
                            Final=Final|(Temp)
                            continue
                        else:
                            Temp=Temp|Q(parameter=i.Parameters_of_interest)
                    else:
                        Temp=Temp|Q(product=i.Products_of_interest)
                        if(i.Parameters_of_interest==None):
                            Final=Final|(Temp)
                            continue
                        else:
                            Temp=(Temp&Q(parameter=i.Parameters_of_interest))
                else:
                    Temp=Temp|Q(country=i.Countries_of_interest)
                    if(i.Products_of_interest==None):
                        if(i.Parameters_of_interest==None):
                            Final=Final|(Temp)
                            continue
                        else:
                            Temp=(Temp&Q(parameter=i.Parameters_of_interest))
                    else:
                        Temp=(Temp&Q(product=i.Products_of_interest))
                        if(i.Parameters_of_interest==None):
                            Final=Final|(Temp)
                            continue
                        else:
                            Temp=(Temp&Q(parameter=i.Parameters_of_interest))
            else:
                Temp=Temp|Q(parameter__type_of_parameter=i.Parameter_types_of_interest)
             
            Final=Final|(Temp)
           
        return qs.filter(Final)


    def get_ordering(self, request):
        if request.user.is_superuser:
            return ['country', 'product','parameter']
        else:
            return ['country']
    fieldsets = (
        (None, {
            'fields': ('country', 'product', 'parameter',('Minimum_Limit','Maximum_Limit','Unit','criticality_of_maintaining','parameter_definition','import_tolerance'))
        }),
        ('Additional Details about timeline of rule', {
            'fields': ('effective_date', 'expire_date','status_of_expire_date')
        }),
        ('Information on source and rules', {
            'fields': ('info_on_regulations','Compliance_Authority','Limit_type','source_document','date_of_publishing_source','remarks')
        }),
    )
    
# admin.site.unregister(Master)
admin.site.register(Master, MasterAdmin)

class RegulatoryParametersInline(admin.TabularInline):
    model = RegulatoryParameters


# @admin.register(RegulatoryParameters)
class RegulatoryParametersAdmin(ImportExportModelAdmin):
    list_display = ('name_of_parameter', 'type_of_parameter')
    resource_class = RegulatoryParametersResource
    list_filter=('type_of_parameter',)
admin.site.register(RegulatoryParameters,RegulatoryParametersAdmin)

# Register the Admin classes for BookInstance using the decorator
@admin.register(TypeOfParameters) 
class TypeOfParametersAdmin(admin.ModelAdmin):
    list_display = ('type',)
    inlines=[RegulatoryParametersInline]

#@admin.register(Countries) 
# class CountriesAdmin(admin.ModelAdmin):
#     list_display = ('country_name','note_for_country_regulations')
#     inlines = [ComCountryRelationInline]

class AuthoritiesAdmin(ImportExportModelAdmin):
    list_display = ('Authority_Name','country','info_note')
    # inlines = [MasterInline]
    list_filter=('country',)
    resource_class = CountryResource
    # def get_queryset(self, request):
    #     qs = super().get_queryset(request)
    #     if request.user.is_superuser:
    #         return qs
    #     return qs.filter(country_name__in=Profile.objects.filter(user=request.user).values_list('Countries_of_interest',flat=True))

admin.site.register(Authorities,AuthoritiesAdmin)

class CountriesAdmin(ImportExportModelAdmin):
    list_display = ('country_name','note_for_country_regulations','pdf_note')
    inlines = [ComCountryRelationInline]
    resource_class = CountryResource
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(country_name__in=Profile.objects.filter(user=request.user).values_list('Countries_of_interest',flat=True))

admin.site.register(Countries,CountriesAdmin)

@admin.register(Commodities) 
class CommoditiesAdmin(admin.ModelAdmin):
    list_display = ('com_name', 'com_type')
    inlines = [ComCountryRelationInline]


# @admin.register(ComCountryRelation) 
class ComCountryRelationAdmin(ImportExportModelAdmin):
    list_display = ('commodity', 'country', 'published_commodity', 'definition_commodity_field')
    list_filter=('country',)
admin.site.register(ComCountryRelation, ComCountryRelationAdmin)


from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Unregister the provided model admin
admin.site.unregister(User)

# Register out own model admin, based on the default UserAdmin
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    pass


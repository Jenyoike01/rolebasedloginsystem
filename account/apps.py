from django.apps import AppConfig
#from allauth.account.apps import AccountConfig
#from allauth.socialaccount.apps import SocialAccountConfig


class AccountConfig(AppConfig):
   name = 'account'


#class AccountConfig(AppConfig):
 #   name = "allauth.account"
  #  verbose_name = ("Accounts")
   # default_auto_field = 'django.db.models.AutoField'   # new


#class SocialAccountConfig(AppConfig):
 #   name = "allauth.socialaccount"
  #  verbose_name = ("Social Accounts")
   # default_auto_field = 'django.db.models.AutoField'   # new


#class ModifiedAccountConfig(AccountConfig):
 #   default_auto_field = 'django.db.models.AutoField'


#class ModifiedSocialAccountConfig(SocialAccountConfig):
 #   default_auto_field = 'django.db.models.AutoField'


#class ModifiedExampleDependencyConfig(AppConfig):
 #   name = 'exampledependency'  # the python module
  #  default_auto_field = 'django.db.models.AutoField'

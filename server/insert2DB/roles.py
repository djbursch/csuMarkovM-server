from improved_permissions.roles import Role
from insert2DB.models import Data, ModelData

class Consumer(Role):
    verbose_name = 'Department Consumer'
    models = [ModelData]
    allow = []
    inherit = True
    inherit_allow = ['insert2DB.can_read_dpt']

'''
class DepartmentProvider(Role):
    verbose_name = 'Department Provider'
    models = [Data,ModelData]
    allow = []
    inherit = True
    inherit_allow = [
    				'insert2DB.can_read_dpt','insert2DB.can_write_dpt'
    				]

class CollegeConsumer(Role):
    verbose_name = 'College Consumer'
    models = [ModelData]
    allow = []
    inherit = True
    inherit_allow = [
    				'insert2DB.can_read_dpt','insert2DB.can_read_clg',
    				]

class CollegeProvider(Role):
    verbose_name = 'College Provider'
    models = [Data,ModelData]
    allow = []
    inherit = True
    inherit_allow = [
    				'insert2DB.can_read_dpt','insert2DB.can_read_clg',
    				'insert2DB.can_write_dpt','insert2DB.can_write_clg',
    				]

class UniversityConsumer(Role):
    verbose_name = 'University Consumer'
    models = [ModelData]
    allow = []
    inherit = True
    inherit_allow = [
    				'insert2DB.can_read_dpt','insert2DB.can_read_clg',
    				'insert2DB.can_read_uni',
    				]

class UniversityProvider(Role):
    verbose_name = 'University Provider'
    models = [Data,ModelData]
    allow = []
    inherit = True
    inherit_allow = [
    				'insert2DB.can_read_dpt','insert2DB.can_read_clg',
    				'insert2DB.can_write_dpt','insert2DB.can_write_clg',
    				'insert2DB.can_write_uni','insert2DB.can_write_uni',
    				]

class SystemProvider(Role):
    verbose_name = 'System Provider'
    models = [Data,ModelData]
    allow = []
    inherit = True
    inherit_allow = [
    				'insert2DB.can_read_dpt','insert2DB.can_read_clg',
    				'insert2DB.can_write_dpt','insert2DB.can_write_clg',
    				'insert2DB.can_write_uni','insert2DB.can_read_uni',
    				'insert2DB.can_write_sys','insert2DB.can_read_sys',
    				]

class SystemConsumer(Role):
    verbose_name = 'System Consumer'
    models = [ModelData]
    allow = []
    inherit = True
    inherit_allow = [
    				'insert2DB.can_read_dpt','insert2DB.can_read_clg',
    				'insert2DB.can_read_uni','insert2DB.can_read_sys',
    				]
'''
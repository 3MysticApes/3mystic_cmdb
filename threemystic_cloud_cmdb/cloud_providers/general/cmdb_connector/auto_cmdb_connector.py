from threemystic_cloud_cmdb.cloud_providers.general.cmdb_connector.base_class.base import cloud_cmdb_general_cmdb_connector_base as base


class cloud_cmdb_general_cmdb_connector_auto(base):
  def __init__(self, *args, **kwargs):
    super().__init__(logger_name= "cloud_cmdb_general_cmdb_connector_auto", *args, **kwargs)
  

  def get_connector(self, *args, **kwargs):
    
    if not self.has_cloud_share_configured():
      return None
    
    if self.get_cloud_share_config_value(config_key= "type") == "ms365":
      from threemystic_cloud_cmdb.cloud_providers.general.cmdb_connector.ms365 import cloud_cmdb_general_cmdb_connector_ms365 as connector
      return connector()
  


  
    
    
  

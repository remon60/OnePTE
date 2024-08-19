class RelatedFieldMixin:
    def get_id(self, obj):
        return obj.id.id_field
    
    def get_title(self, obj):
        return obj.title.title_field
    
    def get_type(self, obj):
        return obj.type.type_field
    
    def get_id_display(self, obj):
        return self.get_id(obj)
    
    def get_title_display(self, obj):
        return self.get_title(obj)
    
    def get_type_display(self, obj):
        return self.get_type(obj)
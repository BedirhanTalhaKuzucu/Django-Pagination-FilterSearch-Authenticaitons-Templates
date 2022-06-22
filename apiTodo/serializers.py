from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')
    
    todo_detail = serializers.HyperlinkedIdentityField(view_name="todo-detail")
    class Meta:
        model= Todo
        fields = ("id", 'owner', "task","description","priority", "done", "todo_detail" ,  "updateDate", "createdDate" )
        

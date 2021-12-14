import json

# from django.shortcuts import render
from django.http import JsonResponse
from django.views import View

from owner.models import Owner, Dog


# views here.

class OwnersView(View):
    def post(self, request):
        data = json.loads(request.body)
        '''
        data = {
            name = '강현구',
            email = 'gusrn015@mgmail.com',
            age = 30
        }
        '''
        owners = Owner.objects.create(
            name = data['name'],
            email = data['email'],
            age = data['age']
        )
        
        return JsonResponse({'message' : 'created'}, status=201)

    def get(self, request):
        owners = Owner.objects.all()
        result = []

        for owner in owners:
            dogs = Dog.objects.filter(owner_id = owner.id) # Dog의 쿼리셋.
            dog_list = []        
            for dog in dogs: # 쿼리셋에서 dog의 정보 
                dog_info = {
                    "name" : dog.name,
                    "age" : dog.age
                }
                dog_list.append(dog_info)
            result.append({
                "name" : owner.name,
                "email" : owner.email,
                "age" : owner.age,
                "dogs" : dog_list
            })
        
        return JsonResponse({"result" : result}, status=200)



class DogsView(View):
    def post(self, request):
        data = json.loads(request.body)
        '''
        data = {
            name = '아지',
            age = 7,
            owner = '강현구'
        }
        '''
        dogs = Dog.objects.create(
            name = data['name'],
            age = data['age'],
            owner = Owner.objects.get(name = data['owner'])
        )

        return JsonResponse ({'message' : 'created'}, status=201)

    def get(self, request):
        dogs = Dog.objects.all() # name, age, owner_id
        result = []

        for dog in dogs:
            result.append({
                "name" : dog.name,
                "age" : dog.age,
                "owner" : Owner.objects.get(id = dog.owner_id).name
            })
        
        return JsonResponse({"result" : result}, status=200)
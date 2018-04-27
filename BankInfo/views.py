from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from .models import Bank, Branch
from .serializers import BranchSerializer

# Create your views here.

def index (request):
    return render (request, 'BankInfo/index.html')

class BranchList (APIView):

    def get (self, request):
        # branches = None
        # print (request.GET)
        branches = None
        try:
            ifsc_code = request.GET['ifsc']
            branches = Branch.objects.filter (ifsc = ifsc_code)
            # print ("IFSC:", ifsc_code)
            serializer = BranchSerializer (branches, many = True)
            return Response (serializer.data)
        except:
            try:
                # for k, v in request.GET.items ():
                #     print (k, v)
                bank_name = request.GET['bank']
                # print ("Bank:", bank_name)
                city_name = request.GET['city']
                # print ("Bank:", bank_name, "City:", city_name)
                try:
                    bank_id = None
                    bank_id = Bank.objects.get(name=bank_name)
                    # while (bank_id is None):
                    #     pass
                    branches = Branch.objects.filter (bank_id = bank_id, city = city_name)
                    serializer = BranchSerializer (branches, many = True)
                    return Response (serializer.data)
                except Bank.DoesNotExist:
                    branches = []
                    serializer = BranchSerializer (branches, many = True)
                    return Response (serializer.data)
            except Exception as e:
                # print (str (e))
                # return render (request, 'BankInfo/index.html')
                # hint = '<a href="BankInfo/index.html" >Click here</a> for details'
                return Response(None, status=status.HTTP_400_BAD_REQUEST)

    def post (self, request, bank_name = None, city_name = None):
        pass


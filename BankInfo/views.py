from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from .models import Bank, Branch
from .serializers import BranchSerializer
import itertools

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
                print (str (e))
                return render (request, 'BankInfo/index.html')

    def post (self, request, bank_name = None, city_name = None):
        pass

def add_banks_from_file (request):
    print ("Add banks from file")
    filename = 'banks.txt'
    fh = open (filename, "r")
    count = 0
    print ('================ starting adding banks to database =======================')
    for line in fh:
        words = line.split ()
        if (len (words)) >= 2:
            try:
                bank_id = int (words[-1])
                bank_name = " ".join (words[:-1])
                bank = Bank (bank_id, bank_name)
                bank.save ()
                count += 1
                # print (bank_id, bank_name)
                print ('Number of banks added:', count)
            except Exception as e:
                print (str (e))
    print ('=================', count, 'banks added to database ========================')
    return render (request, 'BankInfo/index.html')

def add_branches_from_file (request):
	print ("Add branches from file")
    # bankinfo_branch (ifsc, bank_id, branch, address, city, district, state) FROM stdin;
	count = 0
	lines_to_skip = 0

	with open ('num_lines_to_skip.txt', 'r') as f:
		for line in f:
			lines_to_skip = int (line)
			break
    
	filename = 'branches.txt'
	fh = open (filename, "r")
    
	print ('================ starting adding branches to database =======================')
	for line in itertools.islice (fh, lines_to_skip, None):
		words = line.split ('\t')
		if (len (words)) >= 7:
			try:
				ifsc_code = words[0]
				bank_id = int (words[1])
				branch_name = words[2]
				address = words[3]
				city = words[4]
				district = words[5]
				state = words[6]
				b = Branch (ifsc_code, bank_id, branch_name, address, city, district, state)
				b.save ()
				count += 1
				print ('Number of branches added:', count)
				if count >= 500:
					break
			except Exception as e:
				print (str (e))
                
	with open ('num_lines_to_skip.txt', 'w') as f:
		f.write (str (lines_to_skip + count))
                
	print ('=================', count, 'branches added to database ========================')
	return render (request, 'BankInfo/index.html')

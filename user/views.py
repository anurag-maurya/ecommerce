# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# # from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework.decorators import api_view
# from django.contrib.auth.models import User
# from rest_framework import status

# class Home(APIView):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         content = {'message': 'Hello, World!'}
#         return Response(content)
    

# @api_view(["POST",])
# def user_register(request):
#     """
#     username
#     password
#     """
#     if not request.data["username"] or not request.data["password"]:
#         return Response({"error": "username and password are required fields"},
#                         status = status.HTTP_400_BAD_REQUEST)
#     user = User(username = request.data["username"])
#     user.save()
#     user.set_password(request.data["password"])
#     user.save()
    
from django.shortcuts import render
from products.models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User   
from .models import Cart

@api_view(["POST", "GET"])
def add_and_get_cart(request):
    if request.method == "POST":
        request.user= User.objects.get(pk=request.data["user_id"])
        user = request.user
        if not user:
            return Response({"error": "User is not valid"}, status=status.HTTP_400_BAD_REQUEST)
        product  = Product.objects.get(pk=request.data["product_id"])
        
        if Cart.objects.filter(user=request.user, product__id = request.data["product_id"]).exists():
            existing_cart = Cart.objects.filter(user=request.user, product =product)
            existing_cart["quentity"]+=request.data["quentity"]
            data = existing_cart.save()
            return Response({"data": data}, status=status.HTTP_201_CREATED)
        else:
            cart = Cart(user=request.user,
                        product = product,
                        quentity = request.data["quentity"]
                        )
            data = cart.save()
            return Response({"data": data}, status=status.HTTP_201_CREATED)
    else:
        # return Response(Cart.objects.filter(user=request.user))
        return Response(Cart.objects.all().values())